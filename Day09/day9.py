# Are head and tail touching
def touching(head_x,head_y,tail_x,tail_y):
    return abs(head_x-tail_x)<=1 and abs(head_y-tail_y)<=1

assert(touching(0,0,1,1))
assert(touching(0,0,0,0))
assert(not touching(0,0,2,0))

positions_visited = set()

# starting position
head_x=0
head_y=0
tail_x=0
tail_y=0

positions_visited.add((tail_x,tail_y))

with open('C:/Users/Danielle/AOC2022/Day09/input.txt') as f:
    
    for line in f:
        tokens = line.strip().split()
        direction = tokens[0]
        n = int(tokens[1])

        # might be useful
        curr_head_x = head_x
        curr_head_y = head_y

        for i in range(n):
            # move head
            match direction:
                case 'R':
                    head_x += 1
                case 'L':
                    head_x -= 1
                case 'U':
                    head_y += 1
                case 'D':
                    head_y -= 1
            if not touching(head_x,head_y,tail_x,tail_y):
                # move tail
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
                # todo perhaps the above can be consolidated and in many ways since we're guaranteed to be at most 1 away

                positions_visited.add((tail_x,tail_y))

print("Number of positions visited by the tail:", len(positions_visited))

'''
R 4
U 4
L 3
D 1
'''