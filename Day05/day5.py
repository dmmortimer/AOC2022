import re

# move 1 from 2 to 1
p = re.compile("move (\d+) from (\d+) to (\d+)")

# spaces are significant
"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
"""

# current state of crates as a list of lists
# operation removes from the top (end) of a list and adds to the top (end) of another list

stacks = []

# todo can we pass stacks in? Is it pass by reference or pass by value? For now just treat it as a global
# move 1 from 2 to 1
def move_n(n,source,dest):
    source_crate_idx = source-1
    dest_crate_idx = dest-1
    for i in range(n):
        # maybe todo check for empty source stack?
        crate_id = stacks[source_crate_idx].pop()
        stacks[dest_crate_idx].append(crate_id)
    return

# part 2, move multiple crates at a time
def move_n2(n,source,dest):
    source_crate_idx = source-1
    dest_crate_idx = dest-1
    copy_source_idx = len(stacks[source_crate_idx])-n
    for i in range(n):
        crate_id = stacks[source_crate_idx].pop(copy_source_idx)    # always taking from the same index
        stacks[dest_crate_idx].append(crate_id)
    return

with open('C:/Users/Danielle/AOC2022/Day05/input.txt') as f:
    for  line in f:
        if "[" in line:
            # stacks
            idx = 0
            crate_num = 1
            crate_idx = 0
            while idx<len(line):
                if line[idx] == "[":
                    crate_id = line[idx+1] # single letter crate identifier
                    if len(stacks)<crate_idx+1:
                        # add empty lists as needed
                        for x in range(len(stacks),crate_idx+1):
                            stacks.append([])
                    stacks[crate_idx].insert(0,crate_id)
                # skip to next crate location within line
                idx += 4
                crate_num += 1
                crate_idx += 1
            pass
        elif len(line.strip()) == 0:
            # skip blank line separating stacks from instructions
            continue
        else:
            m = p.match(line.strip())
            if m:
                move_n2(int(m.group(1)),int(m.group(2)),int(m.group(3)))

final_configuration = []
for stack in stacks:
    if len(stack)>0:
        final_configuration.append(stack[-1])

print("Final configuration has these crates on top", ''.join(final_configuration))