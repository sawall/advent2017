#!/usr/bin/env python3

# process is traversing a hex grid
#
#      N
#   NW   NE
#
#   SW   SE
#      S
#
#### part one:
# given a list of steps in the form of 'nw, ne, s, n, ne, ...' find the
# shortest path to the home spot
#
#### part two:
# How many steps away is the furthest he ever got from his starting position?

# this page on hexagon coordinates and distances was extremely useful:
#     https://www.redblobgames.com/grids/hexagons/
# 
# i used the cube system because it seemed most straightforward to code,

cube_directions = {
        'nw': (1, -1, 0), 'n': (1, 0, -1), 'ne': (0, 1, -1),
        'sw': (0, -1, 1), 's': (-1, 0, 1), 'se': (-1, 1, 0),
    }

def cube_distance(a, b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])) // 2

def day11():
    with open('input11.txt', 'r') as f:
        steps = f.read().strip().split(',')

    pos = [0,0,0]
    mx = 0

    for s in steps:
        pos[0] += cube_directions[s][0]
        pos[1] += cube_directions[s][1]
        pos[2] += cube_directions[s][2]
        mx = max(mx, cube_distance([0,0,0], pos))

    print('part one: shortest path from destination to home = ' +
            str(cube_distance([0,0,0], pos)) + ' steps')
    print('part two: max distance from home ever = ' + str(mx) + ' steps')

day11()

