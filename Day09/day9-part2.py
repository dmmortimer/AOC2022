# Are two points touching
def touching(head,tail):
    return abs(head[0]-tail[0])<=1 and abs(head[1]-tail[1])<=1

# Returns new coordinates
def move_lead_knot(curr_pos, direction):
    new_pos = curr_pos.copy()
    match direction:
        case 'R':
            new_pos[0] += 1
        case 'L':
            new_pos[0] -= 1
        case 'U':
            new_pos[1] += 1
        case 'D':
            new_pos[1] -= 1
    return new_pos

# Returns new coordinates for following knot
def move_following_knot(lead_pos, curr_following_pos):
    new_pos = curr_following_pos.copy()
    # todo this can probably be consolidated a lot
    head_x = lead_pos[0]
    head_y = lead_pos[1]
    tail_x = curr_following_pos[0]
    tail_y = curr_following_pos[1]
    if head_x == tail_x:
        # head and tail are on a vertical line, move tail up/down towards head
        if tail_y>head_y:
            tail_y -= 1
        else:
            tail_y += 1
    elif head_y == tail_y:
        # head and tail are on a horizontal line, move tail left/right towards head
        if tail_x>head_x:
            tail_x -= 1
        else:
            tail_x += 1
    else:
        # diagonal and at most one away, move tail diagonally towards head
        if tail_y>head_y:
            tail_y -= 1
        else:
            tail_y += 1
        if tail_x>head_x:
            tail_x -= 1
        else:
            tail_x += 1
    new_pos[0] = tail_x
    new_pos[1] = tail_y
    return new_pos

positions_visited = set()

#num_knots = 2   # let's get the initial case working first
num_knots = 10
# starting position
# now there's 10 points, not two.
# so we need a list of 10 coordinates
# 0th is the head and 9th is the tail
knot_positions = [[0,0] for i in range(num_knots)]

positions_visited.add((knot_positions[num_knots-1][0],knot_positions[num_knots-1][1]))

with open('C:/Users/Danielle/AOC2022/Day09/input.txt') as f:
    
    for line in f:
        tokens = line.strip().split()
        direction = tokens[0]
        n = int(tokens[1])

        for i in range(n):
            # move head
            knot_positions[0] = move_lead_knot(knot_positions[0],direction)
            for k in range(num_knots-1):
                if not touching(knot_positions[k],knot_positions[k+1]):
                    # move following knot
                    knot_positions[k+1] = move_following_knot(knot_positions[k],knot_positions[k+1])

            # count the tail position
            positions_visited.add((knot_positions[num_knots-1][0],knot_positions[num_knots-1][1]))

print("Number of positions visited by the tail:", len(positions_visited))

'''
R 4
U 4
L 3
D 1
'''