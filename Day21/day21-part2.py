input_file = 'C:/Users/Danielle/AOC2022/Day21/input.txt'
test = True
if test:
    input_file = 'C:/Users/Danielle/AOC2022/Day21/test-input.txt'

# holds the numbers (that we know of)
monkey_numbers = dict()

# store the formulas
# as tuple (left operand, operator, right operand)
# remove from dictionary after resolution - by setting to None
monkey_inputs = dict()

with open(input_file) as f:

    for line in f:
        tokens = line.strip().split()
        monkey = tokens[0][:-1]
        if tokens[1].isdigit():
            number = int(tokens[1])
            monkey_numbers[monkey] = number
        else:
            monkey_inputs[monkey] = (tokens[1],tokens[2],tokens[3])

# part two
# root monkey looks for equality in its two inputs
# so problem becomes - what should humn yell so that root finds equality

# humn is unknown, ignore input data for it
del(monkey_numbers['humn'])

# what are the two monkies input to root?
root_listen1 = monkey_inputs['root'][0]
root_listen2 = monkey_inputs['root'][2]

# fill in the monkey numbers we can, without knowing what humn yells
# returns the monkey that we need to backtrack from to find what humn yells
def fill_monkey_numbers(monkey_numbers,monkey_inputs):

    # repeatedly loop until no further monkies are filled in
    # once we know one of them, we know the other, because they have to be the same
    change = True
    while change:
        change = False
        for monkey in monkey_inputs:
            if monkey_inputs[monkey] == None:
                # skip over a monkey we already figured out
                continue
            left = monkey_inputs[monkey][0]
            op = monkey_inputs[monkey][1]
            right = monkey_inputs[monkey][2]
            if left in monkey_numbers and right in monkey_numbers:
                left_n = monkey_numbers[left]
                right_n = monkey_numbers[right]
                result = None
                match op:
                    case '+':
                        result = left_n+right_n
                    case '-':
                        result = left_n-right_n
                    case '*':
                        result = left_n*right_n
                    case '/':
                        result = left_n//right_n
                    case _:
                        print("unexpected op",op)
                monkey_numbers[monkey] = result
                monkey_inputs[monkey] = None
                change = True

    if root_listen1 in monkey_numbers:
        monkey_numbers[root_listen2] = monkey_numbers[root_listen1]
        return root_listen2
    else:
        monkey_numbers[root_listen1] = monkey_numbers[root_listen2]
        return root_listen1


m = fill_monkey_numbers(monkey_numbers,monkey_inputs)

print("Starting at",m)
# know m's output and one of m's inputs, so can calculate the other of m's inputs

# now walk back from root_listen to get to humn
while 'humn' not in monkey_numbers:
    left = monkey_inputs[m][0]
    op = monkey_inputs[m][1]
    right = monkey_inputs[m][2]
    result = monkey_numbers[m]

    # result = monkey_numbers[left] op monkey_numbers[right] 
    if left in monkey_numbers:
        left_n = monkey_numbers[left]
        right_n = None
        match op:
            case '+':
                # result = left_n + right_n
                right_n = result - left_n
            case '-':
                # result = left_n - right_n
                right_n = left_n + result
            case '*':
                # result = left_n * right_n
                right_n = result // left_n
            case '/':
                # result = left_n / right_n
                right_n = result * left_n
        monkey_numbers[right] = right_n
        m = right
    else:
        assert(right in monkey_numbers)
        right_n = monkey_numbers[right]
        left_n = None
        match op:
            case '+':
                # monkey_numbers[m] = monkey_numers[left] + right_n
                left_n = result - right_n
            case '-':
                left_n = right_n + result
            case '*':
                left_n = result // right_n
            case '/':
                left_n = result * right_n
        monkey_numbers[left] = left_n
        m = left
    print("at monkey", m, "inputs are", left, right, "job is", op, "output is",result)


print("human yells this to make root's inputs equal:", monkey_numbers['humn'])

# have observed that regardless of input, input2 is always 792784087587
# at least testing 1..91
# so we need to find a number that makes input1 be that same value
# to be continued...

# guessed 3886130271976, it's too high
# TODO test our answer and try numbers near it?

# see modified day21.py it reads from input-humn.txt which can be used to try different values
# for some reason changing humn doesn't change the output!?
# maybe a problem with the integer vs real division?
# with real division, get 3886130271980.3667 which is different!

# try printing the path from humn to tcmj?
# why we start with tcmj set to 792...587, but when we plug in humn value and recalculate, tcmj is something else