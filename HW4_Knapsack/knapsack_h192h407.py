# import necessary libs
import sys
import numpy as np
import re

answer = []


# read file input and reformate
def read_file(fileName):
    with open(fileName) as f:
        # read the rest lines as proposal preference
        N = int(f.readline())
        for line in f:
            # delete all () and split by ','
            pair = re.sub(r'[()]', '', line).strip('\n').split(',')
            # regroup in to pairs
            pair = [(int(pair[a]), int(pair[a+1])) for a in range(0, len(pair), 2)]
    return N, pair


def initialization(Capacity, items):
    # initialize array with all -1 as placeholders
    grid = np.empty((Capacity+1, len(items)), dtype=[('value', 'i4'), ('from', 'U10')])
    # initialize the first row as 0s
    for i in range(0, grid[0].size):
        grid[0, i] = (0, 'I')
    # place first item in the first column
    for i in range(0, Capacity+1):
        # if the first item weight is less than capacity and less than the current weight row
        if items[0][0] < Capacity and items[0][0] <= i:
            grid[i, 0] = (items[0][1], 'I')
        else:
            grid[i, 0] = (0, 'I')
    return grid


# trace back
def trace(grid, Capacity, index, items):
    global answer
    # if the number is from Left
    if grid[Capacity, index]['from'] == 'L':
        trace(grid, Capacity, index-1, items)
    # if the number is from its top-left
    elif grid[Capacity, index]['from'] == 'T':
        answer.append(index+1)
        trace(grid, Capacity - items[index][0], index-1, items)
    # if the number is from initialized
    elif grid[Capacity, index]['from'] == 'I' and grid[Capacity, index]['value'] > 0:
        answer.append(index+1)


def knapsack_solving(Capacity, items):
    grid = initialization(Capacity, items)
    # since grid already been initialized, start with item 1
    for c in range(1, Capacity+1):
        for i in range(1, len(items)):
            # the number from left
            value1 = grid[c, i - 1]['value']
            if c - items[i][0] >= 0:
                # the number from right
                value2 = grid[c - items[i][0], i - 1]['value'] + items[i][1]
            else:
                value2 = 0
            if value1 >= value2:
                grid[c, i] = (value1, 'L')
            else:
                grid[c, i] = (value2, 'T')
    trace(grid, Capacity, len(items)-1, items)


def main():
    C = 0
    global answer
    items = []  # items = (weight, value)
    C, items = read_file(sys.argv[1])
    knapsack_solving(C, items)
    answer = [str(a) for a in sorted(answer)]
    print(','.join(answer))


if __name__ == '__main__':
    main()
