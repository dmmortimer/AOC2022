#2-4,6-8
import re
p = re.compile("(\d+)-(\d+),(\d+)-(\d+)")

with open('C:/Users/Danielle/AOC2022/Day04/input.txt') as f:
    n = 0
    n2 = 0
    for  line in f:
        m = p.match(line.strip())
        assert(m)
        elf1 = set(range(int(m.group(1)),int(m.group(2))+1))
        elf2 = set(range(int(m.group(3)),int(m.group(4))+1))
        if elf1.issubset(elf2) or elf2.issubset(elf1):
            n+=1
        if len(elf1.intersection(elf2)) > 0:
            n2+=1

print("Number of pairs in which one range fully contains the other", n)
print("Number of pairs in which there is at least one overlapping section",n2)