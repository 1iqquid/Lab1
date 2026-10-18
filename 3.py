import os
import time

CSI = "\x1b["
RESET = f"{CSI}0m"
BLACK = 40
WHITE = 47
pixel = "  "

repeats = 3
heights = [7, 9, 11, 9]

def draw_romb(height):
    for i in range(height):
        offset = abs(i - height // 2)
        line = ""
        for position in range(height):
            if position == offset or position == height - offset - 1:
                line += f"{CSI}{BLACK}m{pixel}{RESET}"
            else:
                line += f"{CSI}{WHITE}m{pixel}{RESET}"
        print(line + line[11:] * (repeats - 1))

for frame in range(16):
    os.system('cls')
    draw_romb(heights[frame % 4])
    time.sleep(0.2)