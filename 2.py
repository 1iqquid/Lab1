CSI = "\x1b["
RESET = f"{CSI}0m"
BLACK = 40
WHITE = 47
pixel = "  "

repeats = 3
height = 7

for i in range(height):
    offset = abs(i - height//2)
    romb_line = ""
    for position in range(height):
        if position == offset or position == height - offset - 1:
            romb_line += f"{CSI}{BLACK}m{pixel}{RESET}"
        else:
            romb_line += f"{CSI}{WHITE}m{pixel}{RESET}"

    print(romb_line + romb_line[11:] * (repeats - 1))