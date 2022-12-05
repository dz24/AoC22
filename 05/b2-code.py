def read_input(inp):
    stacks_r = []
    orders = []
    switch = False
    # get lines in either stack_r(ows) or orders
    with open(inp, 'r') as file:
        for line in file:
            rstrip = line.rstrip()
            if rstrip == '':
                switch = True
                continue
            if not switch:
                stacks_r.append(rstrip)
            else:
                orders.append(rstrip)

    # add the letters correctly to stacks_l(ist)
    stacks_lst = [[] for _ in stacks_r[-1] if _ not in ' ']
    for line in stacks_r[:-1]:
        letter_idxs = [i for i in range(len(line)) if (i+3)%4 == 0]
        for idx, letter_idx in enumerate(letter_idxs):
            if line[letter_idx] not in ('[] '):
                stacks_lst[idx] += line[letter_idx]

    # reverse list:
    for lst in stacks_lst:
        lst.reverse()

    return stacks_lst, orders

def reorder(stacks_l, orders):
    stacks_l2 = [lst.copy() for lst in stacks_l]

    # part1:
    for order in orders:
        # number, from to
        split = order.split()
        todo = [int(split[i]) for i in [1,3,5]]
        for _ in range(todo[0]):
            stacks_l[todo[2]-1].append(stacks_l[todo[1]-1].pop())

    # part2:
    for order in orders:
        # number, from to
        temp = []
        split = order.split()
        todo = [int(split[i]) for i in [1,3,5]]
        for _ in range(todo[0]):
            temp.append(stacks_l2[todo[1]-1].pop())

        temp.reverse()
        stacks_l2[todo[2]-1] += temp

    print(''.join([i[-1] for i in stacks_l]))
    print(''.join([i[-1] for i in stacks_l2]))



INP0 = './a0-example.txt'
INP1 = './a1-part1.txt'
stacks_l0, orders0 = read_input(INP0)
reorder(stacks_l0, orders0)
