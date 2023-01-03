def check_signal(cycle, x):
    signal_strength = 0
    if (cycle+20)% 40 == 0 and cycle<=220:
        signal_strength = cycle * x
        print("During cycle", cycle, "register X has value", x, "and signal strength is", signal_strength)
    return signal_strength

# we're going to draw a # or a . each cycle
# every 40 pixels we add a newline (or move to next row if we're going to keep a data structure and output it later)
# draw a # if the current position is +/- 1 of the pixel being drawn, else draw .
# current position is the x register value
crt_lines = []

# x is sprite position (center of)
def is_sprite_visible(cycle,x):
    pixel = (cycle-1)%40
    assert pixel >= 0 and pixel <= 39
    return pixel == x or pixel == x+1 or pixel == x-1

def render_pixel(cycle,x,crt_line,crt_lines):
    if is_sprite_visible(cycle,x):
        crt_line.append('#')
    else:
        crt_line.append('.')
    if len(crt_line) == 40:
        crt_lines.append(crt_line.copy())
        crt_line.clear()
    return

with open('C:/Users/Danielle/AOC2022/Day10/input.txt') as f:

    cycle = 0
    x = 1
    sum_signal_strengths = 0
    crt_line = []
    
    for line in f:
        tokens = line.strip().split()
        print(line.strip())
        instruction = tokens[0]
        match instruction:
            case "noop":
                cycle += 1
                sum_signal_strengths += check_signal(cycle,x)
                render_pixel(cycle,x,crt_line,crt_lines)
            case "addx":
                cycle += 1
                sum_signal_strengths += check_signal(cycle,x)
                render_pixel(cycle,x,crt_line,crt_lines)
                cycle += 1
                sum_signal_strengths += check_signal(cycle,x)
                render_pixel(cycle,x,crt_line,crt_lines)
                value = int(tokens[1])
                x += value
                pass

print("Sum of signal strengths of cycles:", sum_signal_strengths)

for crt_line in crt_lines:
    print(''.join(crt_line))