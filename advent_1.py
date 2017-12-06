#!/usr/bin/env python3

# https://adventofcode.com
#
# day 1. captcha solver
#
#### part one:
#
# The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of
# all digits that match the next digit in the list. The list is circular, so the digit after the
# last digit is the first digit in the list.
# 
# For example:
# 1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the
#      third digit (2) matches the fourth digit.
# 1111 produces 4 because each digit (all 1) matches the next.
# 1234 produces 0 because no digit matches the next.
# 91212129 produces 9 because the only digit that matches the next one is the last digit, 9.

#### part two:
#
# Now, instead of considering the next digit, it wants you to consider the digit halfway around the
# circular list. That is, if your list contains 10 items, only include a digit in your sum if the
# digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.
#
# For example:
# 1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
# 1221 produces 0, because every comparison is between a 1 and a 2.
# 123425 produces 4, because both 2s match each other, but no other digit has a match.
# 123123 produces 12.
# 12131415 produces 4.

def dayone(part2=False):
    with open('input1.txt') as f:
        data = f.read().strip()
    total = 0
    if not part2:
        if data[0] == data[-1]:
            total += int(data[0])
    for i in range(len(data) - 2):
        if not part2:
            if data[i] == data[i+1]:
                total += int(data[i])
        else:
            if data[i] == data[(i + len(data) // 2) % len(data)]:
                total += int(data[i])
    print('part ' + ('two' if part2 else 'one') + ': ' + str(total))

dayone()
dayone(part2=True)

# javascript variant to help a friend
#
#var s = '1123441';
#var total = 0;
#for (var i = 0; i < s.length; i++) {
#  if (i < (s.length - 1)) {
#  	if (s[i] == s[i+1]) {
#      total += parseInt(s[i]);
#    }
#  } else {
#    if (s[i] == s[0]) {
#    	total += parseInt(s[i]);
#    }
#  }
#}
