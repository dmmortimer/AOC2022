test = False
parttwo = True
fn = 'C:/Users/Danielle/AOC2022/Day11/input.txt'
num_rounds = 10000

if test:
    fn = 'C:/Users/Danielle/AOC2022/Day11/test-input.txt'
    num_rounds = 1000
    #num_rounds = 20

# I can't believe I overwrote my initial solution
# starting over...

'''
  Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3
'''

# data structures
monkey_items = []   # list of monkeys - each monkey has ordered list of items (as worry levels) held by this monkey
# index of the list is the monkey number, monkey numbering starts at 0

monkey_op = []  # list of monkeys - each monkey has operation * + 
monkey_operand = [] # list of monkeys - each monkey has operand (or None if it's multiplied by current value)
monkey_divisor = [] # list of monkeys - each monkey has a (prime!) divisor that it uses for its test
monkey_throw_to_true = []   # list of monkeys - each monkey has a monkey it throws item to when level is divisible by divisor
monkey_throw_to_false = []  # list of monkeys - each monkey has a monkey it throws item to when level is _not_ divisible by divisor

def inspect(item,op,operand,divisor,throw_to_true,throw_to_false,global_divisor):
    new_level = item
    match op:
        case '*':
            if operand == None:
                new_level = item*item
            else:
                new_level = item*operand
        case '+':
            new_level = item+operand
        case '-':
            new_level = item-operand

    # part one
    if not parttwo:
        new_level = new_level//3

    # part two (but see if it works for part one too)
    new_level = new_level % global_divisor

    throw_to = throw_to_true if new_level % divisor == 0 else throw_to_false

    return (new_level,throw_to)

with open(fn) as f:

    for line in f:
        tokens = line.strip().split()
        if len(tokens) == 0:
            continue
        match tokens[0]:
            case "Monkey":
                pass
            case "Starting":
                # Starting items: 1,2,3
                items = []
                for x in line.strip()[16:].split(','):
                    item = int(x.strip())
                    items.append(item)
                monkey_items.append(items)
                pass
            case "Operation:":
                monkey_op.append(tokens[4])
                operand = tokens[5]
                if operand == "old":
                    operand = None
                else:
                    operand = int(operand)
                monkey_operand.append(operand)
                pass
            case "Test:":
                monkey_divisor.append(int(tokens[3]))
                pass
            case "If":
                match tokens[1]:
                    case "true:":
                        monkey_throw_to_true.append(int(tokens[5]))
                        pass
                    case "false:":
                        monkey_throw_to_false.append(int(tokens[5]))
                        pass

n = len(monkey_items)

monkey_activity = [0 for x in range(n)]

# insight from Kevan!
# we can reduce the levels down modulo the multiple of all the primes
gd = 1
for d in monkey_divisor:
    gd = gd * d

r = 0
while r<num_rounds:
    # for each monkey
    for m in range(n):
        # for each item held by monkey
        for item in monkey_items[m]:
            (new_level,throw_to) = inspect(item,monkey_op[m],monkey_operand[m],monkey_divisor[m],monkey_throw_to_true[m],monkey_throw_to_false[m],gd)
            monkey_items[throw_to].append(new_level)
            monkey_activity[m] += 1
        monkey_items[m] = []
    r += 1

print(monkey_activity)
monkey_activity.sort(reverse=True)

monkey_business = monkey_activity[0] * monkey_activity[1]

print("Monkey business after", num_rounds, ":", monkey_business)
