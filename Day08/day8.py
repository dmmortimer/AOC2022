trees = []  # Tree heights
# trees[row][col]

# Visible if can be seen from at least one direction
# Can be seen if there all trees in the way are strictly shorter than it
def is_visible(row,col,numrows,numcols):

    if row == 0 or col == 0 or row == numrows-1 or col == numcols-1:
        # outer trees, always visible
        return True

    h = trees[row][col] # the height of the tree we care about

    # assume visible until a blocking tree is found
    visible_from_left = True
    visible_from_right = True
    visible_from_above = True
    visible_from_below = True

    # look left
    for i in range(col):
        if trees[row][i] >= h:
            visible_from_left = False

    # look right
    for i in range(col+1,numcols):
        if trees[row][i] >= h:
            visible_from_right = False
    
    # look up
    for i in range(row):
        if trees[i][col] >= h:
            visible_from_above = False
    
    # look down
    for i in range(row+1,num_rows):
        if trees[i][col] >= h:
            visible_from_below = False

    return visible_from_left or visible_from_right or visible_from_above or visible_from_below

def scenic_score(row,col,numrows,numcols):

    if row == 0 or col == 0 or row == numrows-1 or col == numcols-1:
        # outer trees, not scenic at all
        return 0

    # viewing distance in each direction
    up = 0
    down = 0
    left = 0
    right = 0

    h = trees[row][col]

    # look up
    # stop at edge or first tree that is same height or taller
    for i in reversed(range(row)):
        up += 1
        if trees[i][col] >= h:
            break
            
   # look down
    for i in range(row+1,num_rows):
        down += 1
        if trees[i][col] >= h:
            break

    # look left
    # need to look backwards!
    for i in reversed(range(col)):
        left += 1
        if trees[row][i] >= h:
            break

    # look right
    for i in range(col+1,numcols):
        right += 1
        if trees[row][i] >= h:
            break

    return up*down*left*right

with open('C:/Users/Danielle/AOC2022/Day08/input.txt') as f:
    
    for line in f:
        row_of_trees = []
        for t in line.strip():
            row_of_trees.append(int(t))
        trees.append(row_of_trees)

num_cols = len(trees)
num_rows = len(trees[0])

'''
assert(is_visible(1,1,num_rows,num_cols))   # top left 5
assert(not is_visible(1,3,num_rows,num_cols))
assert(is_visible(1,2,num_rows,num_cols))   # top middle 5
assert(is_visible(2,1,num_rows,num_cols))   # left middle 5
assert(is_visible(2,3,num_rows,num_cols))   # right middle 3
assert(is_visible(3,2,num_rows,num_cols))   # bottom middle 5
'''

n = 0
max_scenic_score = 0
max_x = 0
max_y = 0
max_h = 0

#assert(scenic_score(1,2,num_rows,num_cols) == 4)

for rowidx,row_of_trees in enumerate(trees):
    for colidx,t in enumerate(row_of_trees):
        if is_visible(rowidx,colidx,num_rows,num_cols):
            n += 1
        s = scenic_score(rowidx,colidx,num_rows,num_cols)
        if s > max_scenic_score:
            max_scenic_score = s
            max_x = rowidx
            max_y = colidx
            max_h = trees[rowidx][colidx]

print("Trees visible from outside the grid:", n)
print("Max scenic score", max_scenic_score, "for tree at", max_x, max_y, "of height", max_h)