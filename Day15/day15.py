import re
import sys

def manhattan_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

# take 2, grid is a dictionary
def mark_no_beacon_zone(sensor,beacon,grid):
    sensor_x = sensor[0]
    sensor_y = sensor[1]
    beacon_x = beacon[0]
    beacon_y = beacon[1]
    d = manhattan_distance(sensor_x,sensor_y,beacon_x,beacon_y)
    # up/down from sensor - fix x, vary y
    # we need to fill in a diamond shape. each row gets a varying number of marks in columns centered around sensor x
    for y in range(sensor_y-d,sensor_y+d+1):
        #for x in range(sensor_x-(sensor_y-d-y),sensor_x+(sensor_y-d-y)+1):
        something = abs(y-sensor_y)
        for x in range(sensor_x-d+something,sensor_x+d+1-something):
            grid[(x,y)] = 1
    grid[(beacon_x,beacon_y)] = 0  # can't be a no-beacon position because it is a beacon
    return

# take 3 just look in the row of interest
# no_beacon_positions is a set
def mark_no_beacon_positions_in_row(sensor,beacon,row_to_count,no_beacon_positions):
    sensor_x = sensor[0]
    sensor_y = sensor[1]
    beacon_x = beacon[0]
    beacon_y = beacon[1]
    d = manhattan_distance(sensor_x,sensor_y,beacon_x,beacon_y)
    something = abs(row_to_count-sensor_y)
    for x in range(sensor_x-d+something,sensor_x+d+1-something):
        #don't count the beacon itself
        if (x,row_to_count) != beacon:
            no_beacon_positions.add(x)

input_file = 'C:/Users/Danielle/AOC2022/Day15/input.txt'
row_to_count = 2000000
test = False
if test:
    input_file = 'C:/Users/Danielle/AOC2022/Day15/test-input.txt'
    row_to_count = 10

closest_beacons = dict()    # map of sensor coordinates to closest beacon coordinates

# dimensions of the world we need to map - including all no-beacon zones for our sensors
max_x = 0
max_y = 0
min_x = sys.maxsize
min_y = sys.maxsize

with open(input_file) as f:
    # todo replace with code to read in line, extract sensor and beacon coordinates and store them, and compute min/max x/y
    #Sensor at x=2, y=18: closest beacon is at x=-2, y=15

    p = re.compile("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

    for line in f:
        m = p.match(line.strip())
        sensor_x = int(m.group(1))
        sensor_y = int(m.group(2))
        beacon_x = int(m.group(3))
        beacon_y = int(m.group(4))
        closest_beacons[(sensor_x,sensor_y)] = (beacon_x,beacon_y)
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

# problem we can't index with x,y because we have negative indices
# offset everything? make it a dictionary where the key is the coordinates as a tuple? let's try this
'''
grid_d = dict()
for x in range(min_x,max_x+1):
    for y in range(min_y,max_y+1):
        grid_d[(x,y)] = 0
'''

# this is way too slow with the real data
# maybe we just need to keep a list of the no-beacon coordinates
# that have y = row_to_count

# mark the no-beacon zones on the grid 
answer = 0
no_beacon_positions = set()
for sensor in closest_beacons:
    #mark_no_beacon_zone(sensor,closest_beacons[sensor],grid_d)
    mark_no_beacon_positions_in_row(sensor,closest_beacons[sensor],row_to_count, no_beacon_positions)
answer = len(no_beacon_positions)

'''
answer = 0
for x in range(min_x,max_x+1):
    answer += grid_d[(x,row_to_count)]
'''

print("in row where y=",row_to_count,"positions that cannot contain a beacon:", answer)