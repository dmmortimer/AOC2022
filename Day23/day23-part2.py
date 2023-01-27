import cProfile

input_file = 'C:/Users/Danielle/AOC2022/Day23/input.txt'
test = True
if test:
    input_file = 'C:/Users/Danielle/AOC2022/Day23/test-input.txt'

# data
# list of elves, storing each elf's position as a x,y pair
# relative to what? we'll use 0,0 to be the upper left of the input data. across is x, down is y.
elves = []    # each element is (x,y) tuple

# feels like we also need a grid so we can easily check for neighbours
# a 2-d array with 1s and 0s
# but what to use as index. can't have negative indexes.
# make it huuuuuuge? adjust when coordinates go negative?
# checked ranges, grow slowly e.g. x: -8 .. 80 y: -7 .. 80
# try offset of 20 and 200x200? and wait for index errors if we go out of bounds
grid = [[0 for x in range(200)] for y in range(200)]
# index [y+20][x+20]
offset = 20

# state: ordering of directions to consider moving in

# operations
# first half of round: look around and if needed, propose new position
# second half of round: try moving to proposed position, succeeds only if no other elf would move there
# to end the round, update list of directions

# continue for 10 rounds 

# helpful: function to print current elf positions bounded by rectangle that encompasses all elves
# or, print the same number of rows as in the sample data, for easier visual comparison

# to calculate answer, count empty tiles in this rectangle
def count_empty_tiles(elves,print_grid):
    n = 0
    min_x = None
    min_y = None
    max_x = None
    max_y = None
    for (x,y) in elves:
        if min_x == None or x<min_x:
            min_x = x
        if min_y == None or y<min_y:
            min_y = y
        if max_x == None or x>max_x:
            max_x = x
        if max_y == None or y>max_y:
            max_y = y
    for j in range(min_y,max_y+1):
        s = ''
        for i in range(min_x,max_x+1):
            if (i,j) not in elves:
                n += 1
                if print_grid:
                    s += '.'
            else:
                if  print_grid:
                    s += '#'
        if print_grid:
            print(s)
    return n

def has_adjacent_elves(elf,elves):
    (x,y) = elf
    x_adjusted = x+offset
    y_adjusted = y+offset
    return grid[y_adjusted-1][x_adjusted] == 1 or grid[y_adjusted+1][x_adjusted] == 1 \
            or grid[y_adjusted][x_adjusted-1] == 1 or grid[y_adjusted+1][x_adjusted-1] == 1 or grid[y_adjusted-1][x_adjusted-1] == 1 \
            or grid[y_adjusted][x_adjusted+1] == 1 or grid[y_adjusted+1][x_adjusted+1] == 1 or grid[y_adjusted-1][x_adjusted+1] == 1
    return (x,y-1) in elves or (x,y+1) in elves \
            or (x-1,y) in elves or (x-1,y+1) in elves or (x-1,y-1) in elves \
            or (x+1,y) in elves or (x+1,y+1) in elves or (x+1,y-1) in elves
            
def has_adjacent_elves_in_direction(elf,elves,direction):
    (x,y) = elf
    x_adjusted = x+offset
    y_adjusted = y+offset
    match direction:
        case 0:
            # North
            return grid[y_adjusted-1][x_adjusted-1] == 1 or grid[y_adjusted-1][x_adjusted] == 1 or grid[y_adjusted-1][x_adjusted+1] == 1
            return (x-1,y-1) in elves or (x,y-1) in elves or (x+1,y-1) in elves
        case 1:
            # South
            return grid[y_adjusted+1][x_adjusted-1] == 1 or grid[y_adjusted+1][x_adjusted] == 1 or grid[y_adjusted+1][x_adjusted+1] == 1
            return (x-1,y+1) in elves or (x,y+1) in elves or (x+1,y+1) in elves
        case 2:
            # West
            return grid[y_adjusted][x_adjusted-1] == 1 or grid[y_adjusted+1][x_adjusted-1] == 1 or grid[y_adjusted-1][x_adjusted-1] == 1
            return (x-1,y) in elves or (x-1,y+1) in elves or (x-1,y-1) in elves
        case 3:
            # East
            return grid[y_adjusted][x_adjusted+1] == 1 or grid[y_adjusted+1][x_adjusted+1] == 1 or grid[y_adjusted-1][x_adjusted+1] == 1
            return (x+1,y) in elves or (x+1,y+1) in elves or (x+1,y-1) in elves

def move_in_direction(elf,direction):
    (x,y) = elf
    match direction:
        case 0:
            # North
            return (x,y-1)
        case 1:
            # South
            return (x,y+1)
        case 2:
            # West
            return (x-1,y)
        case 3:
            # East
            return (x+1,y)

# returns the number of elves that moved
def do_round(elves,starting_direction):

    # 0 1 2 3 N S W E

    proposed_moves = [] # stores proposed position for an elf that will move. identify elf by its index into the main elves list
    # so, stores elf_id and new (x,y)

    for idx,elf in enumerate(elves):
        if not has_adjacent_elves(elf,elves):
            # do nothing
            continue    # continue for loop with next elf
        # look until we find the direction with no neighbours
        for direction in (starting_direction,(starting_direction+1)%4,(starting_direction+2)%4,(starting_direction+3)%4):
            if not has_adjacent_elves_in_direction(elf,elves,direction):
                # found our direction
                new_position = move_in_direction(elf,direction)
                proposed_moves.append((idx,new_position))
                break # out of for, move on to next elf (outer for)
        
    # remove collisions
    valid_moves = []

    for proposed_move in proposed_moves:
        elf_id = proposed_move[0]
        (x,y) = proposed_move[1]
        dupe = False
        for m in proposed_moves:
            if m[0] != elf_id and m[1] ==  (x,y):
                dupe = True
                break
        if not dupe:
            valid_moves.append(proposed_move)

    for move in valid_moves:
        elf_id = move[0]
        (x,y) = move[1]
        (old_x,old_y) = elves[elf_id]
        grid[old_y+offset][old_x+offset] = 0
        elves[elf_id] = (x,y)
        grid[y+offset][x+offset] = 1

    return len(valid_moves)


def doit():
    with open(input_file) as f:

        y = 0

        for line in f:
            x = 0
            for c in line.strip():
                if c == '#':
                    elves.append((x,y))
                    grid[y+offset][x+offset] = 1
                x += 1
            y += 1

    print ("There are", len(elves),"elves")

    num_rounds = 10
    round = 0

    direction_index = 0
    movement = True
    while movement:
        movement = do_round(elves,direction_index)
        round += 1
        # premature termination to get some stats
        if False and round == 100:
            movement = False
        direction_index = (direction_index+1)%4
        #print("In round",round, movement, "elves moved")


    print("The first round where no elf moves is round",round)

cProfile.run('doit()')

# speed up has_adjacent_elves and has_adjacent_elves_in_direction
'''
    25580    1.878    0.000    1.878    0.000 day23-part2.py:55(has_adjacent_elves)
    87752    3.476    0.000    3.476    0.000 day23-part2.py:61(has_adjacent_elves_in_direction)
'''