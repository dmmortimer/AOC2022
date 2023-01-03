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

closest_beacon = dict()    # map of sensor coordinates to closest beacon coordinates
closest_beacon_distance = dict()    # map of sensor coordinates to closest beacon coordinates

beacons = set() # in case this is useful

with open(input_file) as f:

    p = re.compile("Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")

    for line in f:
        m = p.match(line.strip())
        sensor_x = int(m.group(1))
        sensor_y = int(m.group(2))
        beacon_x = int(m.group(3))
        beacon_y = int(m.group(4))
        closest_beacon[(sensor_x,sensor_y)] = (beacon_x,beacon_y)
        beacons.add((beacon_x,beacon_y))
        d = manhattan_distance(sensor_x,sensor_y,beacon_x,beacon_y)
        closest_beacon_distance[(sensor_x,sensor_y)] = d

    # for each sensor, check all points 1 beyond the distance to its nearest sensor
    # for each point to check, see if it's in the exclusion zone of any other sensor
    pos_x = None
    pos_y = None

    for sensor,d in closest_beacon_distance.items():
        print("checking points outside exclusion zone of sensor", sensor, "at distance",d)
        d_to_check = d+1
        points_to_check = set()
        sensor_x = sensor[0]
        sensor_y = sensor[1]
        for y in range(sensor_y-d_to_check,sensor_y+d_to_check+1):
            if y < 0 or y > max_pos:
                continue
            something = abs(y-sensor_y)
            start = sensor_x-d_to_check+something
            if start>=0 and start<=max_pos:
                points_to_check.add((start,y))
            end = sensor_x+d_to_check-something
            if end>= 0 and end<=max_pos:
                points_to_check.add((end,y))
            pass
        for (x,y) in points_to_check:
            if (x,y) in closest_beacon:
                # skip this point, it's a beacon, can't be an unknown sensor
                continue
            # is point eliminated by any sensor
            point_is_a_beacon = True
            for sensor2,d2 in closest_beacon_distance.items():
                # if the distance between the point we're checking and the sensor we're checking
                # is less than this sensor's closest beacon, this point can't be a beacon
                if manhattan_distance(x,y,sensor2[0],sensor2[1]) <= d2:
                    # can't be a beacon
                    point_is_a_beacon = False
                    break
            if point_is_a_beacon:
                pos_x = x
                pos_y = y
                break
        pass

    answer = pos_x * 4000000 + pos_y
    print("beacon must be at x=",pos_x,"y=",pos_y)
    print("tuning frequency", answer)

# test data: 6 beacons, 14 sensors
# full data: 8 beacons, 33 sensors