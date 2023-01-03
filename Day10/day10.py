def check_signal(cycle, x):
    signal_strength = 0
    if (cycle+20)% 40 == 0 and cycle<=220:
        signal_strength = cycle * x
        print("During cycle", cycle, "register X has value", x, "and signal strength is", signal_strength)
    return signal_strength

with open('C:/Users/Danielle/AOC2022/Day10/input.txt') as f:

    cycle = 0
    x = 1
    sum_signal_strengths = 0
    
    for line in f:
        tokens = line.strip().split()
        print(line.strip())
        instruction = tokens[0]
        match instruction:
            case "noop":
                cycle += 1
                sum_signal_strengths += check_signal(cycle,x)
                pass
            case "addx":
                cycle += 1
                sum_signal_strengths += check_signal(cycle,x)
                cycle += 1
                sum_signal_strengths += check_signal(cycle,x)
                value = int(tokens[1])
                x += value
                pass

print("Sum of signal strengths of cycles:", sum_signal_strengths)