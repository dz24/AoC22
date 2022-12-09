import numpy as np


def reader(inp):
    result = []
    with open(inp, 'r') as file:
        for line in file:
            split = line.rstrip().split()
            result.append([split[0], int(split[1])])
    return result


def move_bodi(head, tail, move, idx):
    new_head = head + move
    new_tail = np.copy(tail)
    euc_dist = np.sqrt(np.sum((new_head-tail)**2))

    # strings0 = []
    # idx0 = 14
    # if idx == idx0: 
    #     print('booger 0', new_tail, new_head)

    # for i in range(6):
    #     string = ['.']*6
    #     if i == new_head[1]:
    #         string[new_head[0]] = 'H'
    #     if i == tail[1]:
    #         string[tail[0]] = 'T'
    #     strings0.append(''.join(string))

    if euc_dist > 2:
        diff0 = new_head-new_tail
        diff0[abs(diff0) != 1] = 0 
        new_tail = new_tail + diff0 #  (abs(new_head-new_tail == 1)).astype(int)
    # if idx == idx0: 
    #     print('booger 1', new_tail, new_head, (abs(new_head-new_tail)== 1).astype(int))
    #     print(diff0)
    if euc_dist > 1.5: 
        diff1 = np.array((new_head-tail)/2, dtype=int)
        new_tail = new_tail + diff1

    # print(' ')
    # print(idx)
    # for i in reversed(range(6)):
    #     string = ['.']*6
    #     if i == new_head[1]:
    #         string[new_head[0]] = 'H'
    #     if i == new_tail[1]:
    #         string[new_tail[0]] = 'T'
    #     print(strings0[i], '|', ''.join(string))
    # print(' ')

    # if idx == idx0:
    #     exit('ape')

            


    # if euc_dist > 1.5:
    #     # print('ape a', tail, new_head, move)
    #     diff = np.array((new_head-tail)/2, dtype=int)
    #     if euc_dist > 2:
    #         print(new_head, new_tail, diff) 
    #     new_tail = new_tail + diff
    #     if euc_dist > 2:
    #         print('bribe a')
    #         print(new_head, new_tail, (new_head-new_tail) == 1)
    #         new_tail = new_tail + (new_head-new_tail) == 1
    #         print(new_tail)
    #         print('bribe b')
    #         exit('bribe')

        # print('ape b', new_tail, new_head)
    # print('ape')
    # print(f'{idx:02.0f}', ':', tail, head, '|', new_tail, new_head, move)
    return new_head, new_tail


def solution(inp):
    data = reader(inp)
    history = {}
    head, tail = np.array([0, 0]), np.array([0, 0])
    nwse = {'R': [1, 0], 'L': [-1, 0],
            'U': [0, 1], 'D': [0, -1]}
    cnt = 0
    for line in data:
        move = nwse[line[0]]
        print('-- move:', line[0], line[1], '--')
        for _ in range(line[1]):
            head, tail = move_bodi(head, tail, move, cnt)
            tile = f'{tail[0]}, {tail[1]}'
            if tile not in history:
                history[tile] = 0
            history[tile] += 1
            cnt += 1
        print(' ')

    print(sum([i>=1 for i in history.values()]))
    # for key in history.keys():
    #     print(key)
    # print(history)



INP0 = './a0-example.txt'
INP1 = './a1-part1.txt'
solution(INP1)


