#!/usr/bin/env python3

#### part one
#
# The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process
# is on the right track, they need you to calculate the spreadsheet's checksum. For each row,
# determine the difference between the largest value and the smallest value; the checksum is the sum
# of all of these differences.
#
# For example, given the following spreadsheet:
# 
# 5 1 9 5
# 7 5 3
# 2 4 6 8
# 
# The first row's largest and smallest values are 9 and 1, and their difference is 8.
# The second row's largest and smallest values are 7 and 3, and their difference is 4.
# The third row's difference is 6.
# In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

def day2_one():
    checksum = 0
    with open('input2.txt', 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        line_l = [int(d) for d in line.split()]
        checksum += max(line_l) - min(line_l)
    print('part one: ' + str(checksum))

#### part two
# It sounds like the goal is to find the only two numbers in each row where one evenly divides the
# other - that is, where the result of the division operation is a whole number. They would like you
# to find those numbers on each line, divide them, and add up each line's result.
#
# For example, given the following spreadsheet:
#
# 5 9 2 8
# 9 4 7 3
# 3 8 6 5
# In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
# In the second row, the two numbers are 9 and 3; the result is 3.
# In the third row, the result is 2.
# In this example, the sum of the results would be 4 + 3 + 2 = 9.

def day2_two():
    checksum = 0
    with open('input2.txt', 'r') as f:
        lines = f.read().splitlines()
    for line in lines:
        row_checksum = 0
        line_l = [int(d) for d in line.split()]
        # this algorithm heavily leverages the 'only one match per row' assumption
        for i in range(len(line_l)):
            numerator = int(line_l[i])
            denoms = line_l[:i] + line_l[i+1:]
            for denom_s in denoms:
                denom = int(denom_s)
                if numerator % denom == 0:
                    row_checksum  = numerator // denom
                    break
            if row_checksum > 0:
                break
        checksum += row_checksum
    print('part two: ' + str(checksum))


# for reference: great concise answers from /u/ellersok on reddit:
#
# with io.StringIO(s) as f:
#     lines = [[int(n) for n in l.split()] for l in f]
#
# ans1 = sum(max(l)-min(l) for l in lines)
# ans2 = sum(b//a for l in lines for a,b in itertools.combinations(sorted(l),2) if b%a==0)

day2_one()
day2_two()

