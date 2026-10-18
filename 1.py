CSI = "\x1b["
RESET = f"{CSI}0m"

width = 30
height = 20

def color(row,column):
    if (row - width/2)**2 + (column-height/2)**2 < (0.3*height)**2:
        return 41
    else:
        return 47

def draw_flag():
    pixel = '  '
    for i in range(height):
        for j in range(width):
            print(f'{CSI}{color(j,i)}m{pixel}{RESET}', end="")
        print()

draw_flag()