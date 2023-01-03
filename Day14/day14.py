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

assert min_x>=0 and min_y>=0    # make sure we don't need negative indices
# the +2 is because we need an extra allowance for lateral check
grid = [[0 for x in range(max_x+2)] for y in range(max_y+1)]

# how many rows in this grid? should be max_y
# how many columns? should be max_x
# how to index the grid? is it [x][y] or [y][x]? first index picks the row, second picks the column - so [y][x]
# which is confusing as heck

pass

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
    pass

answer = 0

reached_abyss = False

# sand falls one grain at a time until it falls past max_y; after that there's nothing to stop it
while not reached_abyss:

    # new grain of sand starts here
    sand_x = 500
    sand_y = 0

    # find resting place for this grain of sand by moving it through free squares
    reached_resting_spot = False
    while not reached_resting_spot:

        if sand_y >= max_y:
            reached_abyss = True
            break

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

print("units of sand that come to rest before the rest fall into the void:", answer)