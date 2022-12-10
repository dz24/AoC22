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
    screen_line = ''
    for inst in insts:
        todo = 1 if 'noop' in inst else 2
        for _ in range(todo):
            screen_line += '#' if abs(cnt%40-tot) < 2 else '.'
            cnt += 1
            if (cnt+20)%40 == 0:
                tot_l.append(tot*cnt)
            if cnt%40 == 0:
                screen.append(screen_line)
                screen_line = ''
        tot += 0 if todo == 1 else int(inst[1])
    print('part1:', sum(tot_l))
    print('part2:')
    for screen_line in screen:
        print(screen_line)


INP0 = './a0-example.txt'
INP1 = './a1-part1.txt'
solution(INP1)
