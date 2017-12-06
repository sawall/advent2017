#!/usr/bin/env python3

# memory allocation
#
#### part one
#
# The debugger would like to know how many redistributions can be done before a blocks-in-banks
# configuration is produced that has been seen before.
#
# For example, imagine a scenario with only four memory banks:
#
# The banks start with 0, 2, 7, and 0 blocks. The third bank has the most blocks, so it is chosen
# for redistribution.
# Starting with the next bank (the fourth bank) and then continuing to the first bank, the second
# bank, and so on, the 7 blocks are spread out over the memory banks. The fourth, first, and second
# banks get two blocks each, and the third bank gets one back. The final result looks like this: 2 4
# 1 2.
# Next, the second bank is chosen because it contains the most blocks (four). Because there are four
# memory banks, each gets one block. The result is: 3 1 2 3.
# Now, there is a tie between the first and fourth memory banks, both of which have three blocks.
# The first bank wins the tie, and its three blocks are distributed evenly over the other three
# banks, leaving it with none: 0 2 3 4.
# The fourth bank is chosen, and its four blocks are distributed such that each of the four banks
# receives one: 1 3 4 1.
# The third bank is chosen, and the same thing happens: 2 4 1 2.
# At this point, we've reached a state we've seen before: 2 4 1 2 was already seen. The infinite loop is detected after the fifth block redistribution cycle, and so the answer in this example is 5.
# 
# Given the initial block counts in your puzzle input, how many redistribution cycles must be
# completed before a configuration is produced that has been seen before?

import math

def day6():
    inp = '4 10 4 1 8 4 9 14 5 1 14 15 0 15 3 5'
    memory = [int(i) for i in inp.strip().split()]
    past_states = []
    num_banks = len(memory)
    cycles = 0

    while (hash(tuple(memory)) not in past_states):
        past_states.append(hash(tuple(memory)))
        realloc_blocks = max(memory)
        realloc_cursor = memory.index(max(memory))
        memory[realloc_cursor] = 0
        while realloc_blocks > 0:
            realloc_cursor += 1
            memory[(realloc_cursor) % num_banks] += 1
            realloc_blocks -= 1
        cycles += 1
    print('-= advent of code DAY SIX =-')
    print('   part one: total cycles until loop detected = ' + str(cycles))

#### part two
#
# Out of curiosity, the debugger would also like to know the size of the loop: starting from a state
# that has already been seen, how many block redistribution cycles must be performed before that
# same state is seen again?

    loop_start = past_states.index(hash(tuple(memory)))
    print('   part two: loop size = ' + str(cycles - loop_start))

day6()

