import sys

# first get the dimensions of the world we need to map
max_x = 0
max_y = 0
min_x = sys.maxsize
min_y = sys.maxsize

# 503,4 -> 502,4 -> 502,9 -> 494,9

with open('C:/Users/Danielle/AOC2022/Day14/input.txt') as f:
    for line in f:
        line = line.strip()
        tokens = line.split()
        for t in tokens:
            if t == "->":
                continue
            (curr_x,curr_y) = map(int,t.split(','))
            if curr_x>max_x:
                max_x = curr_x
            if curr_x<min_x:
                min_x = curr_x
            if curr_y>max_y:
                max_y = curr_y
            if curr_y<min_y:
                min_y = curr_y

# part two - there's an infinite floor at location y = max_y+2
# this means no abyss - sand will always find a resting place
# how much x-space do we need for this? let's try 500 + max_y * 2 since it seems to rest on a 1:1 diagonal slope

floor = max_y+2

grid = [[0 for x in range(500+2*floor)] for y in range(floor+1)]

# read the input again and mark the squares that are rocks
with open('C:/Users/Danielle/AOC2022/Day14/input.txt') as f:
    for line in f:
        line = line.strip()
        tokens = line.split()
        prev_x = None
        prev_y = None
        for t in tokens:
            if t == "->":
                continue
            (curr_x,curr_y) = map(int,t.split(','))
            if prev_x == None:
                prev_x = curr_x
                prev_y = curr_y
            else:
                # draw (mark) a line from prev_x, prev_y to x,y
                for x in range(prev_x,curr_x+1):
                    for y in range(prev_y,curr_y+1):
                        grid[y][x] = 1
                # and the other way around for good measure (must be a better way to do this)
                for x in range(curr_x,prev_x+1):
                    for y in range(curr_y,prev_y+1):
                        grid[y][x] = 1
                prev_x = curr_x
                prev_y = curr_y

    # mark the floor
    for x in range(len(grid[0])):
        grid[floor][x] = 1

answer = 0

reached_sand_source = False # sand has filled the spot at y=0 x=500

# sand falls one grain at a time until it reaches the floor
while not reached_sand_source:

    # new grain of sand starts here
    sand_x = 500
    sand_y = 0

    # find resting place for this grain of sand by moving it through free squares
    reached_resting_spot = False
    while not reached_resting_spot:

        # try to fall down 
        if grid[sand_y+1][sand_x] == 0:
            # we can move here
            sand_y += 1
        # can't fall down, try down-left
        elif grid[sand_y+1][sand_x-1] == 0:
            # we can move here
            sand_x -= 1
            sand_y += 1
        # can't fall down-left, try down-right
        elif grid[sand_y+1][sand_x+1] == 0:
            # we can move here
            sand_x += 1
            sand_y += 1
        else:
            # we're at our resting place, mark it and count this grain of sand
            grid[sand_y][sand_x] = 1
            reached_resting_spot = True
            answer +=1
            if sand_y == 0 and sand_x == 500:
                reached_sand_source = True

print("units of sand that come to rest before sand source is blocked:", answer)