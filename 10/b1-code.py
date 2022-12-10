

def reader(inp):
    instructions = []
    with open(inp, 'r') as file:
        for line in file:
            split = line.rstrip().split()
            instructions.append(split)
    return instructions


def solution(inp):
    insts = reader(inp)
    cnt = 0
    tot = 1
    tot_l = []
    inst_dic = {'noop': 1, 'addx': 2}
    for inst in insts:
        todo = inst_dic[inst[0]]
        for _ in range(todo):
            cnt += 1
            if (cnt+20)%40 == 0:
                tot_l.append(tot*cnt) 
        tot += 0 if todo == 1 else int(inst[1])
    print(sum(tot_l))


INP0 = './a0-example.txt'
INP1 = './a1-part1.txt'
solution(INP1)

    

