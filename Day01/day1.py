elves = []  # list of totals

with open('C:/Users/Danielle/AOC2022/Day01/input.txt') as f:
    c = 0
    for  line in f:
        if line.strip() == "":
            elves.append(c)
            c = 0
        else:
            c += int(line.strip())

print("Elf with most calories has", max(elves))

# part two: calories carried by top three elves

elves.sort()
print("Calories of top three elves", sum(elves[-3:]))