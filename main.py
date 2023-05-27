import os
import iptool
import IGtool


def draw_logo():
    f = open('logo.txt', 'r', encoding="utf8")
    print("")
    print(''.join([line for line in f]))
    print("")
    print("")


os.system('color 02')
draw_logo()

print("\n\n\n 1. IP Lookup")
print("2. Instagram Lookup")

x = int(input('\n\nEnter your Choice : '))

if x == 1:
    iptool.ipFinder()

elif x == 2:
    IGtool.get_insta()


input()


