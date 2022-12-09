import numpy as np


def reader(inp):
    result = []
    with open(inp, 'r') as file:
        for line in file:
            split = line.rstrip().split()
            result.append([split[0], int(split[1])])
    return result


def move_bodi(head, tail, move, first):
    if first:
        head = head + move
    euc_dist = np.sqrt(np.sum((head-tail)**2))

    if euc_dist > 2:
        diff0 = (head-tail)
        diff0[abs(diff0) != 1] = 0
        tail = tail + diff0
    if euc_dist > 1.5:
        tail = tail + ((head-tail)/2).astype(int)

    return head, tail


def solution(inp, length=2):
    data = reader(inp)
    history = {}
    bodi = [np.array([0, 0]) for _ in range(length)]
    nwse = {'R': [1, 0], 'L': [-1, 0],
            'U': [0, 1], 'D': [0, -1]}
    cnt = 0
    for line in data:
        move = nwse[line[0]]
        for _ in range(line[1]):
            for i in reversed(range(1, length)):
                bodi[i], bodi[i-1] = move_bodi(bodi[i], bodi[i-1],
                                               move, i == length-1)
            tile = f'{bodi[0][0]}, {bodi[0][1]}'
            if tile not in history:
                history[tile] = 0
            history[tile] += 1
            cnt += 1

    print(sum([i>=1 for i in history.values()]))



INP0 = './a0-example.txt'
INP1 = './a1-example.txt'
INP2 = './a2-part1.txt'
solution(INP2, length=2)
solution(INP2, length=10)
