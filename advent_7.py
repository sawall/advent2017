#!/usr/bin/env python3

class Node:
    def __init__(self, name, weight, parent, children):
        self.name = name
        self.weight = weight
        self.parent = parent
        self.children = set(children)
        self.tower_weight = 0

    def __repr__(self):
        out = self.name + ' (' + str(self.weight) + ') [' + str(self.tower_weight) + ']'
        if len(self.children):
            out += ' -> ' + ', '.join(self.children)
        return out

def day7():
    with open('input7.txt', 'r') as f:
        data = f.read().splitlines()
    
    nodes = {}

    # grok the input
    for line in data:
        if len(line.split('->')) > 1:
            children = set(line.split('->')[1].strip().split(', '))
        else:
            children = set()
        name = line.split()[0]
        weight = int(line.split()[1].translate(str.maketrans('','','()')))
        parent = ''
        nodes[name] = Node(name, weight, parent, children)

    #### part one: find name of program at bottom (i.e., the one with no parent)

    # assign parents based on known children
    for t in nodes:
        for c in nodes[t].children:
            nodes[c].parent = nodes[t].name

    for t in nodes:
        if nodes[t].parent == '':
            bottom_prog = nodes[t].name

    print('-= advent of code DAY SEVEN =-')
    print('part one: the bottom program is named: ' + bottom_prog)

    #### part two: count up weights of subtowers and find out which one is causing things
    #### to be unbalanced

    # make sure parents are aware of their children
    for t in nodes:
        if len(nodes[t].parent):
            nodes[nodes[t].parent].children.add(t)

    # recursively determine tower weights
    def sum_weights(node):
        if len(node.children):
            node.tower_weight = sum([sum_weights(nodes[c]) for c in node.children]) + node.weight
        else:
            node.tower_weight = node.weight
        return node.tower_weight
    
    sum_weights(nodes[bottom_prog])

    # recursively find the problem program
    # will not deal well if we get out to the leafs or if there are nodes with < 3 children
    def find_problem(node):
        child_weights = []
        rev_lookup = {}
        for c in node.children:
            child_weights.append(nodes[c].tower_weight)
            rev_lookup[nodes[c].tower_weight] = c
        child_weights = sorted(child_weights)
        if child_weights[0] != child_weights[1]:
            problem_weight = child_weights[0]
            good_weight = child_weights[1]
        elif child_weights[-1] != child_weights[-2]:
            problem_weight = child_weights[-1]
            good_weight = child_weights[-2]
        else:
            return False

        problem = nodes[rev_lookup[problem_weight]]
        if not find_problem(problem):
            print('part two:')
            print('  problem found with: ' + str(problem))
            print('  tower weight is ' + str(problem_weight) + ' and should be ' + str(good_weight))
            fixed_weight = problem.weight + good_weight - problem_weight
            print('  change the weight of ' + str(problem.name) + ' from ' + str(problem.weight) + ' to ' + str(fixed_weight))

        return True

    find_problem(nodes[bottom_prog])

day7()
