#!/usr/bin/env python3

#### part one: grok an incoming stream of groups
#
# group begins with { and ends with }
# groups are nestable, i.e., } closes most recent {
#
# garbage begins with < and ends with >
# {}< within garbage have no special meaning
#
# ! and the character immediately after it should be ignored
#
# {}, 1 group.
# {{{}}}, 3 groups.
# {{},{}}, also 3 groups.
# {{{},{},{{}}}}, 6 groups.
#
# score groups; each group given a score that is one more than the score of # the group
# that contains it. outermost group is score 1
#
# {}, score of 1.
# {{{}}}, score of 1 + 2 + 3 = 6.
# {{},{}}, score of 1 + 2 + 2 = 5.
# {{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
#
#### part two
#
# count all of the characters that were removed from the garbage, not including
# leading and trailing < and >, nor ! or any characters that they canceled

from collections import defaultdict
import operator as op

def day9(debug=False):
    with open('input9.txt', 'r') as f:
        data = f.read()
    
    in_garbage = False
    i = 0
    level = 0
    score = 0 # part one
    garbagecount = 0 # part two
    if debug:
        debug_data = ''

    while i < len(data):
        if data[i] == '!':
            i += 1 # ignore next
        elif in_garbage:
            if data[i] == '>':
                in_garbage = False
            else:
                garbagecount += 1
        elif data[i] == '<':
            in_garbage = True
        elif data[i] == '{':
            level += 1
            if debug:
                debug_data += '{' + str(level)
        elif data[i] == '}':
            score += level
            level -= 1
            if debug:
                debug_data += '}'
        i += 1

    if debug:
        print(debug_data)
    print('part one: score = ' + str(score))
    print('part two: garbage collected = ' + str(garbagecount))

day9()
