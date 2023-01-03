input_file = 'C:/Users/Danielle/AOC2022/Day18/input.txt'
test = False
if test:
    input_file = 'C:/Users/Danielle/AOC2022/Day18/test-input.txt'

cubes = []  # each cube is a 3-tuple x,y,z

# cube has 6 sides, call them front, back, top, bottom, left, right

# returns true if cube1 is adjacent to cube2
def adjacent(cube1,cube2):
    a = False
    # cube1 is beside cube2 on x-axis
    if abs(cube1[0]-cube2[0]) == 1 and cube1[1] == cube2[1] and cube1[2] == cube2[2]:
        a = True
    # cube1 is in front of or behind cube2 on y-axis
    if abs(cube1[1]-cube2[1]) == 1 and cube1[0] == cube2[0] and cube1[2] == cube2[2]:
        a = True
    # cube1 is on top of or below cube2 on z-axis
    if abs(cube1[2]-cube2[2]) == 1 and cube1[0] == cube2[0] and cube1[1] == cube2[1]:
        a = True
    return a

assert(adjacent((1,1,1),(2,1,1)))

with open(input_file) as f:

    for line in f:
        (x,y,z) = list(map(int,line.strip().split(',')))
        cubes.append((x,y,z))

n = 0

for cube1 in cubes:
    n += 6
    for cube2 in cubes:
        if cube2 == cube1:
            continue
        if adjacent(cube1,cube2):
            n -= 1

print("droplet surface area - number of exposed cube sides", n)