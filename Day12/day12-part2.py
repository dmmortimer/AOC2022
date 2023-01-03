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

# using Dijkstra from Wikipedia
def do_dijkstra(heightmap,start,end,min):

    # current shortest distance from start to this point, initialized to infinity
    dist = [[sys.maxsize for y in range(len(heightmap[0]))] for x in range(len(heightmap))]
    dist[start[0]][start[1]] = 0

    # flag set to 1 after node is visited
    visited = [[0 for y in range(len(heightmap[0]))] for x in range(len(heightmap))]

    # path backwards to form the shortest path; each element is a tuple
    # todo this seems optional, maybe leave it out for performance
    prev = [[None for y in range(len(heightmap[0]))] for x in range(len(heightmap))]

    # we'll stop by breaking when we've visited the endpoint
    while True:

        # choose next node
        (x,y) = next_node_to_visit(dist,visited)
        if x == None or y == None:
            return None
        visited[x][y] = 1 

        curr_height = heightmap[x][y]
        alt = dist[x][y] + 1
        if alt > min:
            # don't bother continuing
            # todo this isn't helping...
            return None

        # check reachable neighbours of this node and update their distance
        # up
        if x>0 and not visited[x-1][y]:
            h = heightmap[x-1][y]
            if h <= curr_height+1:  # we can step to one-higher letter or any lower letter
                if alt<dist[x-1][y]:
                    dist[x-1][y] = alt
                    prev[x-1][y] = [x,y]
        # down
        if x < len(heightmap)-1 and not visited[x+1][y]:
            h = heightmap[x+1][y]
            if h <= curr_height+1:
                if alt<dist[x+1][y]:
                    dist[x+1][y] = alt
                    prev[x+1][y] = [x,y]
        # left
        if y>0 and not visited[x][y-1]:
            h = heightmap[x][y-1]
            if h <= curr_height+1:
                if alt<dist[x][y-1]:
                    dist[x][y-1] = alt
                    prev[x][y-1] = [x,y]
        # right
        if y < len(heightmap[0])-1 and not visited[x][y+1]:
            h = heightmap[x][y+1]
            if h <= curr_height+1:
                if alt<dist[x][y+1]:
                    dist[x][y+1] = alt
                    prev[x][y+1] = [x,y]

        # termination condition - we just visited the endpoint
        if x == end[0] and y == end[1]:
            break
        # todo somehow make use of previous min to also stop looking

    return dist[x][y]

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
# we can stop looking once a path exceeds any previous path from an 'a' e.g. the answer to part 1

min = sys.maxsize
for x in range(len(heightmap)):
    for y in range(len(heightmap[0])):
        if heightmap[x][y] == ord('a'):
            start[0] = x
            start[1] = y
            print("Finding shortest path from", start)
            new_min = do_dijkstra(heightmap,start,end,min)
            if new_min != None and new_min < min:
                min = new_min

print("Shortest path starting from any 'a'",min)

# what if we set the start to be 'E' and with our dist data structure, read off the distances for any 'a' node