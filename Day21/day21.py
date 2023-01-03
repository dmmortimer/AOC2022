input_file = 'C:/Users/Danielle/AOC2022/Day21/input-humn.txt'
test = False
if test:
    #input_file = 'C:/Users/Danielle/AOC2022/Day21/test-input.txt'
    input_file = 'C:/Users/Danielle/AOC2022/Day21/test-input-humn.txt'

# holds the numbers (that we know of)
monkey_numbers = dict()

# simple approch, store the formulas
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
            pass
        pass

# repeatedly loop until root monkey number appears
while "root" not in monkey_numbers:
    for monkey in monkey_inputs:
        if monkey_inputs[monkey] == None:
            continue
        left = monkey_inputs[monkey][0]
        op = monkey_inputs[monkey][1]
        right = monkey_inputs[monkey][2]
        if left in monkey_numbers and right in monkey_numbers:
            result = None
            match op:
                case '+':
                    result = monkey_numbers[left]+monkey_numbers[right]
                case '-':
                    result = monkey_numbers[left]-monkey_numbers[right]
                case '*':
                    result = monkey_numbers[left]*monkey_numbers[right]
                case '/':
                    result = monkey_numbers[left]//monkey_numbers[right]
            monkey_numbers[monkey] = result
            monkey_inputs[monkey] = None
        pass
    pass

print("for humn set to",monkey_numbers['humn'], "root yells", monkey_numbers['root'])
if not test:
    print("tcmj yells", monkey_numbers['tcmj'])
    print("qggp yells", monkey_numbers['qggp'])
else:
    print("pppw yells", monkey_numbers['pppw'])
    print("sjmn yells", monkey_numbers['sjmn'])
pass


# test -  input.txt has humn was 3640
# input-humn.txt sets it to 3886130271976 (for the real data) and see what output is for root's two inputs
# which are root: tcmj + qggp
# they don't match - so it's obviously wrong -
# repeat with test-input-humn.txt set to 1