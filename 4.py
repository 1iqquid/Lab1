BLUE = '\u001b[44m'
RED = '\u001b[41m'
RESET = '\u001b[0m'
BEGIN = '\x1B[1G'

def sequence():
    file = open('sequence.txt')
    greater = []
    less = []
    for line in file:
        x = float(line)
        if x > -5 and x < 0:
            greater.append(x)
        elif x < -5 and x < 0:
            less.append(x)
    file.close()

    total = len(greater) + len(less)
    percent_greater = len(greater) / total * 100
    percent_less = 100 - percent_greater
    
    bar_greater = ' ' * int(len(greater) / 2)
    bar_less = ' ' * int(len(less) / 2)

    print(f'{BLUE}{bar_greater}{RESET} {round(percent_greater, 2)}%  (> -5)')
    print(f'{RED}{bar_less}{RESET} {round(percent_less, 2)}%  (< -5)')

sequence()