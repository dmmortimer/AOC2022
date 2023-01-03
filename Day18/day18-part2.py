import sys

input_file = 'C:/Users/Danielle/AOC2022/Day18/input.txt'
test = False
if test:
    input_file = 'C:/Users/Danielle/AOC2022/Day18/test-input.txt'

cubes = set()  # each cube is a 3-tuple x,y,z

# cube has 6 sides, call them front, back, top, bottom, left, right

# returns true if cube1 is adjacent to cube2
def adjacent(cube1,cube2):
    a = False
    # cube1 is beside cube2 on x-axis
    if abs(cube1[0]-cube2[0]) == 1 and cube1[1] == cube2[1] and cube1[2] == cube2[2]:
        a = True
    # cube1 is in front of or behind cube2 on y-axis
    elif abs(cube1[1]-cube2[1]) == 1 and cube1[0] == cube2[0] and cube1[2] == cube2[2]:
        a = True
    # cube1 is on top of or below cube2 on z-axis
    elif abs(cube1[2]-cube2[2]) == 1 and cube1[0] == cube2[0] and cube1[1] == cube2[1]:
        a = True
    return a

def exposed_sides(cubes):

    n = 0   # total exposed sides

    for cube1 in cubes:
        n += 6
        n1 = 6  # exposed sides for this cube
        for cube2 in cubes:
            if adjacent(cube1,cube2):
                n -= 1
                n1 -= 1
                if n1 == 0:
                    # found 6 adjacent cubes, no need to keep checking (not sure if this helps perf)
                    break
    return n

# returns None if it's not an air pocket
# air_pocket has the list of air cubes so far
# position must be an air cube
# droplet is our water cubes from the input
def find_air_pocket(air_pocket,position,droplet):

    # walk from starting position until find a droplet piece or exit the world
    (x,y,z) = position

    air_cubes.add((x,y,z))  # keeping track of the air cubes we've already looked at

    new_x = x+1
    if new_x>max_x:
        # exceeded bounds of the droplet, are beyond the world of interest, no air pocket
        return None

    # still in air?
    if (new_x,y,z) not in cubes and (new_x,y,z) not in air_pocket:
        air_pocket.add((new_x,y,z))
        air_pocket = find_air_pocket(air_pocket,(new_x,y,z),droplet)
        if air_pocket == None:
            return None

    # repeat for each direction (possible refactoring opp here)
    new_x = x-1
    if new_x<0:
        return None

    if (new_x,y,z) not in cubes and (new_x,y,z) not in air_pocket:
        air_pocket.add((new_x,y,z))
        air_pocket = find_air_pocket(air_pocket,(new_x,y,z),droplet)
        if air_pocket == None:
            return None

    new_y = y+1
    if new_y>max_y:
        return None

    if (x,new_y,z) not in cubes and (x,new_y,z) not in air_pocket:
        air_pocket.add((x,new_y,z))
        air_pocket = find_air_pocket(air_pocket,(x,new_y,z),droplet)
        if air_pocket == None:
            return None

    new_y = y-1
    if new_y<0:
        return None

    if (x,new_y,z) not in cubes and (x,new_y,z) not in air_pocket:
        air_pocket.add((x,new_y,z))
        air_pocket = find_air_pocket(air_pocket,(x,new_y,z),droplet)
        if air_pocket == None:
            return None

    new_z = z+1
    if new_z>max_z:
        return None

    if (x,y,new_z) not in cubes and (x,y,new_z) not in air_pocket:
        air_pocket.add((x,y,new_z))
        air_pocket = find_air_pocket(air_pocket,(x,y,new_z),droplet)
        if air_pocket == None:
            return None

    new_z = z-1
    if new_z<0:
        return None

    if (x,y,new_z) not in cubes and (x,y,new_z) not in air_pocket:
        air_pocket.add((x,y,new_z))
        air_pocket = find_air_pocket(air_pocket,(x,y,new_z),droplet)
        if air_pocket == None:
            return None

    # we're done exploring in all 6 directions, return the air pocket we found
    return air_pocket

max_x = 0
max_y = 0
max_z = 0
min_x = sys.maxsize
min_y = sys.maxsize
min_z = sys.maxsize

with open(input_file) as f:

    for line in f:
        (x,y,z) = list(map(int,line.strip().split(',')))
        assert(x>=0)
        assert(y>=0)
        assert(z>=0)
        if x>max_x: max_x = x
        if y>max_y: max_y = y
        if z>max_z: max_z = z
        if x<min_x: min_x = x
        if y<min_y: min_y = y
        if z<min_z: min_z = z
        cubes.add((x,y,z))

#n = exposed_sides(cubes)
n = 3364
if test:
    n = 64

print("droplet size in cubes", len(cubes))
print("droplet surface area - number of exposed cube sides", n)

total_air_pocket_size = 0
air_cubes = set()

# look for air pockets
for x in range(max_x+1):
    for y in range(max_y+1):
        for z in range(max_z+1):
            if (x,y,z) not in cubes and (x,y,z) not in air_cubes:
                air_pocket = {(x,y,z)}
                air_pocket = find_air_pocket(air_pocket,(x,y,z),cubes)
                if air_pocket != None:
                    air_pocket_surface = exposed_sides(air_pocket)
                    air_pocket_size = len(air_pocket)
                    print("Found an air pocket of size",air_pocket_size,"connected to",(x,y,z),"with surface", air_pocket_surface)
                    if air_pocket_size>1 and air_pocket_size<10:
                        print(air_pocket)
                    n -= air_pocket_surface
                    total_air_pocket_size += air_pocket_size
                pass

print("total air pocket volume in cubes",total_air_pocket_size)
print("droplet surface area excluding interior sides",n)

# total surface area (in and out) is 3364
# program calculates 1760 outside edges, but it's too low
# try 1178 (the huge air pocket) plus 1760??  no, 2938 is too high
# kevan found my bug!

# day 21 is the next one I'll do based on stats