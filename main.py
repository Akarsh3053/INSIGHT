import os
import IP


def draw_logo():
    f = open('logo.txt', 'r', encoding="utf8")
    print("")
    print(''.join([line for line in f]))
    print("")
    print("")


os.system('color 02')
draw_logo()


