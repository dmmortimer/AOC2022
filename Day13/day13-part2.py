import json
from functools import cmp_to_key

from enum import Enum
class ComparisonStatus(Enum):
    IN_ORDER = -1
    OUT_OF_ORDER = 1
    DONT_KNOW_YET = 0
# not using the enum any more, it messed up the sorted compare function with this error:
# TypeError: '<' not supported between instances of 'ComparisonStatus' and 'int'

def compare_packets(left, right):

    if type(left) != list and type(right) != list:
        # we have two numbers, go ahead and compare them and return
        result = None
        left = int(left)
        right = int(right)
        if left<right:
            result = -1
        elif left>right:
            result = 1
        else:
            result = 0
        return result

    # convert as needed so both are lists
    if type(left) != list:
        left = [left]
    if type(right) != list:
        right = [right]
    
    for idx,x in enumerate(left):
        if len(right)<=idx:
            # ran out of elements to compare - left has more than right
            result = 1
        else:
            result = compare_packets(x,right[idx])
        if result == 0:
            continue    # move on to next element in the list
        return result

    # Got here without a conclusive result, finally check list len
    if len(left)<len(right):
        result = -1
    else:
        result = 0

    return result

packets = []

with open('C:/Users/Danielle/AOC2022/Day13/input-part2.txt') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0:
            # blank line separating pairs, ignore
            pass
        else:
            packets.append(json.loads(line))

# part two - sort the packets - we have 300 packets in the real input
# look up a good sort algorithm ... and plop our compare function into it
# kind of wishing I'd called my enum LESS_THAN and GREATER_THAN
# but treat IN_ORDER as LESS_THAN and OUT_OF_ORDER as GREATER_THAN

# python sorted with a key
# we have to define a class with lt function? no, easier than that...

sorted_packets = sorted(packets, key=cmp_to_key(compare_packets))

# find the positions of the separator packets
decoder_key = 1
for idx,p in enumerate(sorted_packets):
    if p == [[2]] or p == [[6]]:
        decoder_key = decoder_key * (idx+1)

print("Decoder key is", decoder_key)