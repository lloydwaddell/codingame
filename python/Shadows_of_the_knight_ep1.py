import sys
import math
min_w, min_h, max_w, max_h, n, x, y = [0,0] + [int(i) for i in raw_input().split()] + [int(raw_input())] + [int(i) for i in raw_input().split()]
while True:
    bomb_dir = raw_input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    if("U" in bomb_dir):
        max_h = y - 1
    if("R" in bomb_dir):
        min_w = x + 1
    if("L" in bomb_dir):
        max_w = x - 1
    if("D" in bomb_dir):
        min_h = y + 1
    
    y = (max_h + min_h) / 2
    x = (max_w + min_w) / 2
    
    # the location of the next window Batman should jump to.
    print "{} {}".format(int(x),int(y))
