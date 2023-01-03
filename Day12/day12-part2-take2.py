import sys

heightmap = []  # 2-d array each element is a row on the map and each point is a letter

start = None  # x,y coordinates of starting point
end = None    # ditto for endpoint. x is row, y is col

# we visit the next unvisited node that has the lowest distance
def next_node_to_visit(dist,visited):
    min = sys.maxsize
    min_x = None
    min_y = None
    for x in range(len(dist)):
        for y in range(len(dist[0])):
            if visited[x][y] == 0 and dist[x][y] < min:
                min = dist[x][y]
                min_x = x
                min_y = y
    return (min_x,min_y)

def shortest_a(dist):
    min = sys.maxsize
    for x in range(len(dist)):
        for y in range(len(dist[0])):
            if heightmap[x][y] == ord('a') and dist[x][y] < min:
                min = dist[x][y]
    return min

def can_step_from(curr_elevation, dest_elevation):
    # part two, reverse criteria from part 1 as we're going backwards. we can go up, stay the same, or go down by one
    return dest_elevation >= curr_elevation-1 

# using Dijkstra from Wikipedia
def do_dijkstra(heightmap,end):

    # current shortest distance from start to this point, initialized to infinity
    dist = [[sys.maxsize for y in range(len(heightmap[0]))] for x in range(len(heightmap))]
    dist[end[0]][end[1]] = 0

    # flag set to 1 after node is visited
    visited = [[0 for y in range(len(heightmap[0]))] for x in range(len(heightmap))]

    # we'll stop by breaking when we've visited all possible nodes
    while True:

        # choose next node
        (x,y) = next_node_to_visit(dist,visited)
        if x == None or y == None:
            # we're done!
            break
        visited[x][y] = 1 

        curr_height = heightmap[x][y]
        alt = dist[x][y] + 1

        # check reachable neighbours of this node and update their distance
        # up
        if x>0 and not visited[x-1][y]:
            h = heightmap[x-1][y]   # h is height of neighbour and potential next step; curr_height is height of current position
            if can_step_from(curr_height,h):
                if alt<dist[x-1][y]:
                    dist[x-1][y] = alt
        # down
        if x < len(heightmap)-1 and not visited[x+1][y]:
            h = heightmap[x+1][y]
            if can_step_from(curr_height,h):
                if alt<dist[x+1][y]:
                    dist[x+1][y] = alt
        # left
        if y>0 and not visited[x][y-1]:
            h = heightmap[x][y-1]
            if can_step_from(curr_height,h):
                if alt<dist[x][y-1]:
                    dist[x][y-1] = alt
        # right
        if y < len(heightmap[0])-1 and not visited[x][y+1]:
            h = heightmap[x][y+1]
            if can_step_from(curr_height,h):
                if alt<dist[x][y+1]:
                    dist[x][y+1] = alt

        # part two - don't break when reaching start or end - keep going to get all the distances for 'a's

    # find 'a' with shortest path
    return shortest_a(dist)

# read in the heightmap
with open('C:/Users/Danielle/AOC2022/Day12/input.txt') as f:
    num_a = 0
    for x,line in enumerate(f):
        line = line.strip()
        row = []
        for y,c in enumerate(line):
            # Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.
            if c == 'S':
                start = [x,y]
                c = 'a'
                print("start", start)
            elif c == 'E':
                end = [x,y]
                c = 'z'
                print("end", end)
            if c == 'a':
                num_a += 1
            row.append(ord(c))
        heightmap.append(row)

print("Number of points with elevation 'a'", num_a)
# for part two we need to consider paths to E starting from any position at elevation a
# the test data has 6 'a' points
# the real data has 1842
# what if we set the start to be 'E' and with our dist data structure, read off the distances for any 'a' node

min = do_dijkstra(heightmap,end)

print("Shortest path starting from any 'a'",min)