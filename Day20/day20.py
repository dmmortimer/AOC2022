input_file = 'C:/Users/Danielle/AOC2022/Day20/input.txt'
test = False
if test:
    input_file = 'C:/Users/Danielle/AOC2022/Day20/test-input.txt'

class NumberNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

def get_values_as_list(node):
    curr = node
    values = []
    while curr is not None:
        values.append(curr.value)
        curr = curr.next
        if curr == node:
            break
    return values
    
# exercise the backwards links
def get_values_as_list_backwards(node):
    curr = node
    values = []
    while curr is not None:
        values.insert(0,curr.value)
        curr = curr.prev
        if curr == node:
            break
    return values

def mix(node,modulus):
    n = node.value
    #n_reduced = abs(n)%modulus
    n_reduced = abs(n)%(modulus-1)  # had to resort to reddit to fix this bug. still think the problem def was confusing. what does it mean to skip over x numbers when it wraps?
    # I guess you consider that you pick the number up - it no longer exists in the rotation - and count movements from there without the number being moved
    if n_reduced == 0:
        return
    if n>0:
        move_ahead(node,n_reduced)
    else:
        move_back(node,n_reduced)
    return

def move_ahead(node_to_move,n):

    # find the node we're moving after
    move_after = node_to_move
    for i in range(n):
        move_after = move_after.next

    # these two changes remove the node we've moving
    node_to_move.prev.next = node_to_move.next
    node_to_move.next.prev = node_to_move.prev

    # now insert it into its new position - forward links
    save = move_after.next
    move_after.next = node_to_move
    node_to_move.next = save

    # backward links
    node_to_move.prev = move_after
    node_to_move.next.prev = node_to_move

    return

def move_back(node_to_move,n):

    # find the node we're moving before
    move_before = node_to_move
    for i in range(n):
        move_before = move_before.prev

    # these two changes remove the node we've moving
    # todo refactor move_ahead and move_back to share more code
    node_to_move.prev.next = node_to_move.next
    node_to_move.next.prev = node_to_move.prev

    # now insert it into its new position - backward links
    save = move_before.prev
    move_before.prev = node_to_move
    node_to_move.prev = save

    # forward links
    node_to_move.next = move_before
    node_to_move.prev.next = node_to_move

    return

# using the zero node as the entry point of the decrypted list
def calc_answer(zero):
    # the grove coordinates can be found by looking at the 1000th, 2000th, and 3000th numbers after the value 0, wrapping around the list as necessary.
    ans = 0
    node = zero
    for i in range(3000):
        node = node.next
        i += 1
        if i in (1000,2000,3000):
            print(i,"th number after 0 is",node.value)
            ans += node.value
    return ans

zero = None # useful entry point to linked list

# static list with ordering for the mix operations
nodes_to_mix = []

with open(input_file) as f:

    head = None # start of linked list
    curr = None # most recently-added number node

    for line in f:
        value = int(line.strip())
        node = NumberNode(value)
        nodes_to_mix.append(node)
        if value == 0:
            assert(zero == None)    # make sure only one zero
            zero = node
        if head == None:
            head = node
        else:
            curr.next = node
        node.prev = curr
        curr = node
    
    # finally, close the circle
    head.prev = curr
    curr.next = head

assert(zero.value==0)   # make sure zero exists

num_numbers = len(nodes_to_mix)
print("There are",num_numbers,"numbers to mix")

# do the decryption/mixing node-by-node
for node in nodes_to_mix:
    mix(node,num_numbers)

answer = calc_answer(zero)
print("Sum of three numbers that form the grove coordinates:", answer)