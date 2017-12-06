#!/usr/bin/env python3

#### part one:
#
# Positive jumps ("forward") move downward; negative jumps move upward. For legibility in this
# example, these offset values will be written all on one line, with the current instruction marked
# in parentheses. The following steps would be taken before an exit is found:
#
# (0) 3  0  1  -3  - before we have taken any steps.
# (1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). Fortunately, the instruction
#                    is then incremented to 1.
#  2 (3) 0  1  -3  - step forward because of the instruction we just modified. The first instruction
#                    is incremented again, now to 2.
#  2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
#  2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
#  2  5  0  1  -2  - jump 4 steps forward, escaping the maze.

#### part two:
# Now, the jumps are even stranger: after each jump, if the offset was three or more, instead
# decrease it by 1. Otherwise, increase it by 1 as before.
#
# Using this rule with the above example, the process now takes 10 steps, and the offset values
# after finding the exit are left as 2 3 2 3 -1.
#
# How many steps does it now take to reach the exit?

def day5(part2=False):
    with open("input5.txt") as f:
        maze = list(map(int, f.readlines()))
    stepcount = 0
    cursor = 0
    while cursor >= 0 and cursor < len(maze):
        if part2 and maze[cursor] >= 3:
            maze[cursor] -= 1
            cursor += maze[cursor] + 1
        else:
            maze[cursor] += 1
            cursor += maze[cursor] - 1
        stepcount += 1
    print('part ' + ('two' if part2 else 'one') + ': escaped maze after ' + str(stepcount) + ' steps!')

day5()
day5(part2=True)
