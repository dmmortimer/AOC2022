import re
import sys

test = True
input_file = 'C:/Users/Danielle/AOC2022/Day15/input.txt'
row_to_count = 2000000
max_pos = 4000000
if test:
    input_file = 'C:/Users/Danielle/AOC2022/Day15/test-input.txt'
    row_to_count = 10
    max_pos = 20

def manhattan_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

# take 3 just look in the row of interest
# no_beacon_positions is a set
# part two range we care about is 0..max_pos
# would it be better to remove positions as they are ruled out?
def mark_no_beacon_positions_in_row(sensor,beacon,row_to_count,no_beacon_positions,max_pos):
    sensor_x = sensor[0]
    sensor_y = sensor[1]
    beacon_x = beacon[0]
    beacon_y = beacon[1]
    d = manhattan_distance(sensor_x,sensor_y,beacon_x,beacon_y)
    something = abs(row_to_count-sensor_y)
    start = min(0,sensor_x-d+something)
    if start<0:
        start = 0
    end = min(sensor_x+d+1-something,max_pos+1)
    if end<0: 
        end = 0
    for x in range(start,end):
        #don't count the beacon itself
        #should this check whether this is any beacon, not just this one?
        #yet, I got the right answer for part 1
        # for now, comment out this check by adding or True...
        if True or (x,row_to_count) != beacon:
            no_beacon_positions.add(x)

closest_beacons = dict()    # map of sensor coordinates to closest beacon coordinates

beacons = set() # in case this is useful

# dimensions of the world we need to map - including all no-beacon zones for our sensors
max_x = 0
max_y = 0
min_x = sys.maxsize
min_y = sys.maxsize

with open(input_file) as f:

    p = re.compile("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

    for line in f:
        m = p.match(line.strip())
        sensor_x = int(m.group(1))
        sensor_y = int(m.group(2))
        beacon_x = int(m.group(3))
        beacon_y = int(m.group(4))
        closest_beacons[(sensor_x,sensor_y)] = (beacon_x,beacon_y)
        beacons.add((beacon_x,beacon_y))
        d = manhattan_distance(sensor_x,sensor_y,beacon_x,beacon_y)
        curr_x_lo = sensor_x-d
        curr_x_hi = sensor_x+d
        curr_y_lo = sensor_y-d
        curr_y_hi = sensor_y+d
        if curr_x_hi>max_x:
            max_x = curr_x_hi
        if curr_x_lo<min_x:
            min_x = curr_x_lo
        if curr_y_hi>max_y:
            max_y = curr_y_hi
        if curr_y_lo<min_y:
            min_y = curr_y_lo

# 4 million rows to check (or stop when done)
for row in range(0,max_pos+1):
    no_beacon_positions = set()
    for sensor in closest_beacons:
        mark_no_beacon_positions_in_row(sensor,closest_beacons[sensor],row, no_beacon_positions, max_pos)
    # we looked at max_pos+1 locations and ruled out some of them
    # if we ruled out all but one of unknown locations - the known locations are sensors or beacons - then we found the spot
    if len(no_beacon_positions) == max_pos:
        # we're done
        # find the one number not in the set
        for col in range(0,max_pos+1):
            if col not in no_beacon_positions:
                answer = col * 4000000 + row
                print("beacon must be at x=",col,"y=",row)
                print("tuning frequency", answer)
        break

# we're interested in rows where there are max_pos no-beacon positions (could be 0-max_pos inclusive)

# part two
# find the only spot that could contain a beacon
# with part 1 we know how to rule out positions in a row
# repeat that 4million times? looking for a row where only one number between 1 and 4million does not appear on the ruled-out list?

# test data: 6 beacons, 14 sensors
# full data: 8 beacons, 33 sensors

# pause for now ... need a reset