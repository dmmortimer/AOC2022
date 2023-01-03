import json

from enum import Enum
ComparisonStatus = Enum('ComparisonStatus', 'IN_ORDER OUT_OF_ORDER DONT_KNOW_YET')

def compare_packets(left, right):

    if type(left) != list and type(right) != list:
        # we have two numbers, go ahead and compare them and return
        result = None
        left = int(left)
        right = int(right)
        if left<right:
            result = ComparisonStatus.IN_ORDER
        elif left>right:
            result = ComparisonStatus.OUT_OF_ORDER
        else:
            result = ComparisonStatus.DONT_KNOW_YET
        return result

    # convert as needed so both are lists
    if type(left) != list:
        left = [left]
    if type(right) != list:
        right = [right]
    
    for idx,x in enumerate(left):
        if len(right)<=idx:
            # ran out of elements to compare - left has more than right
            result = ComparisonStatus.OUT_OF_ORDER
        else:
            result = compare_packets(x,right[idx])
        if result == ComparisonStatus.DONT_KNOW_YET:
            continue    # move on to next element in the list
        return result

    # Got here without a conclusive result, finally check list len
    if len(left)<len(right):
        result = ComparisonStatus.IN_ORDER
    else:
        result = ComparisonStatus.DONT_KNOW_YET

    return result

answer = 0

pair_idx = 1    # first pair has index 1

with open('C:/Users/Danielle/AOC2022/Day13/input.txt') as f:
    left = None
    right = None
    for line in f:
        line = line.strip()
        if len(line) == 0:
            # blank line separating pairs, ignore
            pass
        elif left == None:
            left = json.loads(line)
        else:
            right = json.loads(line)
            result = compare_packets(left, right)
            #print("Result for pair", pair_idx,"is", result)
            if result == ComparisonStatus.IN_ORDER:
                answer += pair_idx
            left = None
            right = None
            pair_idx += 1

print("the sum of indices of packets in the right order is", answer)

# part two - sort the packets - we have 300 packets in the real input
# look up a good sort algorithm ... and plop our compare function into it
# kind of wishing I'd called my enum LESS_THAN and GREATER_THAN
# but treat IN_ORDER as LESS_THAN and OUT_OF_ORDER as GREATER_THAN
