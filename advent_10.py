#!/usr/bin/env python3

#### part one: knot hash
#
# given a circular list of numbers from 0-255
# given an input of lengths to pinch/twist the list
#
# for each new length:
# 1. length to twist starts at current position
# 2. twist the length (reverse the order of the sublist)
# 3. move current position forward to length + skip size
# 4. increase skip size by 1

#### part two:
#
# - treat input as a string of bytes (ascii character codes)
# - add '17, 31, 73, 47, 23' to the end of the sequence
# - run 64 rounds of the hash instead of a single round, but maintain
#   the current position and skip size
# - calculate dense hash; bitwise XOR to combine each consecutive block
#   of 16 numbers (entries, not digits). this means XORing sublist
#   entries to themselves.
# - concatenate the dense hash and convert each digit to hex

def twist_knot(lst, pos, length):
    if pos + length < len(lst):
        lst[pos:pos + length] = lst[pos:pos + length][::-1]
    else:
        firstlen = (pos + length) - len(lst)
        sublst = (lst[pos:] + lst[:firstlen])[::-1]
        for i,v in enumerate(sublst):
            lst[(pos + i) % len(lst)] = v
    return lst

def day10(inp, part2=False):
    cursor = 0
    skip_size = 0
    rounds = 1
    knot = list(range(256))

    if not part2:
        # treat input as a comma-delimited list of lengths
        digits = [int(c) for c in inp.split(',')]
    else:
        # treat input as a string of bytes, including the commas
        digits = []
        for d in inp:
            digits.append(ord(d))
        for d in [int(c) for c in '17,31,73,47,23'.split(',')]:
            digits.append(d)
        rounds = 64

    for _ in range(rounds):
        for length in digits:
            knot = twist_knot(knot, cursor, length)
            cursor = (cursor + length + skip_size) % len(knot)
            skip_size += 1

    if not part2:
        ans = knot[0] * knot[1]
        print('part one: product of first two digits = ' + str(ans))
    else:
        ans = ''
        for i in range(16):
            sl = knot[i * 16:(i+1) * 16]
            xored = 0
            for elem in sl:
                xored ^= elem
            ans += '{0:0{1}x}'.format(xored,2) # pad 0's!
        print('part two: hash = ' + str(ans))

given = '106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36'
day10(given)
day10(given, part2=True)
