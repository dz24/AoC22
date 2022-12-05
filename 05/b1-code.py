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
    numbering = [i for i in stacks_r[-1] if i != ' ']
    stacks_l = [[] for _ in numbering]
    len_r = len(stacks_r[0])
    letter_idx = [i for i in range(len_r) if (i+3)%4 == 0]
    for line in stacks_r[:-1]:
        letter_idxs = [i for i in range(len(line)) if (i+3)%4 == 0]
        for idx, letter_idx in enumerate(letter_idxs):
            if line[letter_idx] not in ('[] '):
                stacks_l[idx] += line[letter_idx]

    # reverse list:
    for lst in stacks_l:
        lst.reverse()

    return stacks_l, orders

def reorder(stacks_l, orders):
    for order in orders:
        # number, from to
        split = order.split()
        todo = [int(split[i]) for i in [1,3,5]]
        # todo = [int(i) for i in order if i in numbers]
        for i in range(todo[0]):
            stacks_l[todo[2]-1].append(stacks_l[todo[1]-1].pop())

    print(''.join([i[-1] for i in stacks_l]))



INP0 = './a0-example.txt'
INP1 = './a1-part1.txt'
stacks_l, orders = read_input(INP1)
reorder(stacks_l, orders)

