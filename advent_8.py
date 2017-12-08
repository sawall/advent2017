#!/usr/bin/env python3

#### part one
# instruction examples:
#
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10
#
# arbitrary registers, keep track of all of them w/input file, report
# the highest value
#
#### part two
# report the highest value any register ever achieved

from collections import defaultdict
import operator as op

bops = { '==': op.eq, '!=': op.ne, '>': op.gt, '>=': op.ge, '<': op.lt, '<=': op.le }
ops = {'inc': 1, 'dec': -1}

with open('input8.txt', 'r') as f:
        data = f.read().splitlines()

regs = defaultdict(int)
mxval = -10000

for line in data:
    for reg, rop, rval, _, cvar, cop, cval in [line.split()]:
        regs[reg] += int(rval) * ops[rop] if bops[cop](regs[cvar], int(cval)) else 0
        mxval = max(mxval, regs[reg])

print('part one: max value at end = ' + str(max(regs.values())))
print('part two: max value ever = ' + str(mxval))

