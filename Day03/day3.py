# returns item priority
def item_priority(item):
    # a-z is 1-26
    # A-Z is 27-52
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27
    # ugly but it works

def find_misplaced_item(items):
    # divide the line in half
    # iterate chars in first half looking for match in second half
    for c in items[:len(items)//2]:
        if c in items[len(items)//2:]:
            return c

def find_badge(group):
    item_types='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in item_types:
        if c in group[0] and c in group[1] and c in group[2]:
            return c

with open('C:/Users/Danielle/AOC2022/Day03/input.txt') as f:
    total = 0
    total2 = 0
    group = []
    for  line in f:
        item = find_misplaced_item(line.strip())
        total += item_priority(item)
        # part 2: check the three-elf groups to find the badge (single item in common across the three)
        group.append(line)
        if len(group) == 3:
            badge = find_badge(group)
            total2 += item_priority(badge)
            group = []

print("Sum of priorities of misplaced item types", total)
print("Sum of priorities of group badge item types", total2)