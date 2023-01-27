input_file = 'C:/Users/Danielle/AOC2022/Day23/input.txt'
test = True
if test:
    input_file = 'C:/Users/Danielle/AOC2022/Day23/test-input.txt'

# data
# list of elves, storing each elf's position as a x,y pair
# relative to what? we'll use 0,0 to be the upper left of the input data. across is x, down is y.
elves = []    # each element is (x,y) tuple

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
    return (x,y-1) in elves or (x,y+1) in elves \
            or (x-1,y) in elves or (x-1,y+1) in elves or (x-1,y-1) in elves \
            or (x+1,y) in elves or (x+1,y+1) in elves or (x+1,y-1) in elves
            
def has_adjacent_elves_in_direction(elf,elves,direction):
    (x,y) = elf
    match direction:
        case 0:
            # North
            return (x-1,y-1) in elves or (x,y-1) in elves or (x+1,y-1) in elves
        case 1:
            # South
            return (x-1,y+1) in elves or (x,y+1) in elves or (x+1,y+1) in elves
        case 2:
            # West
            return (x-1,y) in elves or (x-1,y+1) in elves or (x-1,y-1) in elves
        case 3:
            # East
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

def get_direction_as_string(direction):
    match direction:
        case 0:
            # North
            return 'N'
        case 1:
            # South
            return 'S'
        case 2:
            # West
            return 'W'
        case 3:
            # East
            return 'E'

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
        elves[elf_id] = (x,y)

    return

with open(input_file) as f:

    y = 0

    for line in f:
        x = 0
        for c in line.strip():
            if c == '#':
                elves.append((x,y))
            x += 1
        y += 1

print ("There are", len(elves),"elves")

if test:
    print("Initial state")
    ans = count_empty_tiles(elves,True)

num_rounds = 10

direction_index = 0
for round in range(num_rounds):
    do_round(elves,direction_index)
    if test:
        print("==End of round",round+1)
        ans = count_empty_tiles(elves,True)
    else:
        ans = count_empty_tiles(elves,False)
    direction_index = (direction_index+1)%4


print("After",num_rounds,"rounds, there are",ans,"empty tiles in the smallest rectangle that contains every elf")

# part one complete. ran kind of slowly though. let's see what part two brings...