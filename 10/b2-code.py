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
    screen = []
    screen_str = ''
    for inst in insts:
        todo = 1 if 'noop' in inst else 2
        for _ in range(todo):
            add_str = '#' if cnt%40 in [tot+i for i in (-1, 0, 1)] else '.'
            screen_str += add_str
            cnt += 1
            if cnt%40 == 0:
                tot_l.append(tot*cnt) 
                screen.append(screen_str)
                screen_str = ''
        tot += 0 if todo == 1 else int(inst[1])
    print(sum(tot_l))
    for screen0 in screen:
        print(screen0)


INP0 = './a0-example.txt'
INP1 = './a1-part1.txt'
solution(INP1)

    

