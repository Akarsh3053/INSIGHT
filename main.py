import os
import iptool


def draw_logo():
    f = open('logo.txt', 'r', encoding="utf8")
    print("")
    print(''.join([line for line in f]))
    print("")
    print("")


os.system('color 02')
draw_logo()

print("\n\n\n\n\n 1. IP Lookup")
x = int(input('Enter your Choice : '))

if x == 1:
    iptool.ipFinder()


input()


