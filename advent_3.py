#!/usr/bin/env python3

# Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then
# counting up while spiraling outward. For example, the first few squares are allocated like this:
#
# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23---> ...
#
# While this is very space-efficient (no squares are skipped), requested data must be carried back
# to square 1 (the location of the only access port for this memory system) by programs that can
# only move up, down, left, or right. They always take the shortest path: the Manhattan Distance
# between the location of the data and square 1.
#
# For example:
# 
# Data from square 1 is carried 0 steps, since it's at the access port.
# Data from square 12 is carried 3 steps, such as: down, left, left.
# Data from square 23 is carried only 2 steps: up twice.
# Data from square 1024 must be carried 31 steps.
# How many steps are required to carry the data from the square identified in your puzzle input all
# the way to the access port?
#
# Your puzzle input is 265149.
#
# ...
#
# Let's think of this grid as a series of expanding squares
#   first square is 1x1, second is 3x3, third is 5x5
#   first has 1, second has 2-9 (8 digits), third has 10-25 (16)
#
# the first space on each square is one step above the bottom
# right corner
# (2 is above 9, 10 is above 25, etc)
#
# upper value in any square is (square_num * 2 - 1) ** 2 ... 1, 9, 25, 49, etc

inp = 265149

def find_loc(inp):
    spirals_out = 0   # 0 is the center 'spiral'
    spiral_upper = 1  # upper value of this spiral
    while(spiral_upper <= inp):
        spirals_out += 1
        spiral_upper = ((spirals_out + 1) * 2 - 1) **2

    print('input: ' + str(inp) + ', spiral_upper: ' + str(spiral_upper) + ', spirals_out: ' + str(spirals_out)) 

    # find the side length and values of the corners
    spiral_side_len = (spirals_out + 1) * 2 - 1
    val_btm_rt =  spiral_upper
    val_btm_lt = val_btm_rt - spiral_side_len + 1
    val_top_lt = val_btm_lt - spiral_side_len + 1
    val_top_rt = val_top_lt - spiral_side_len + 1
   
    if (inp <= val_top_rt):    # right side
        loc = [spirals_out, spirals_out - (val_top_rt - inp)]
    elif (inp <= val_top_lt):  # top
        loc = [-spirals_out + (val_top_lt - inp), spirals_out]
    elif (inp <= val_btm_lt):  # left side
        loc = [-spirals_out, -spirals_out + (val_btm_lt - inp)]
    elif (inp <= val_btm_rt):  # bottom
        loc = [spirals_out - (val_btm_rt - inp), -spirals_out]
    else:
        print('wtf')
    
    return loc

print('part one')
location = find_loc(inp)
steps = abs(location[0]) + abs(location[1])
print('location: ' + str(location) + ', steps: ' + str(steps))

print('part two')
# https://oeis.org/A141481
# https://oeis.org/A141481/b141481.txt
