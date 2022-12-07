def read_inp(inp):
    lines = []
    with open(inp, 'r') as file:
        for line in file:
            rstrip = line.rstrip()
            lines.append(rstrip)

    return lines


def solution(inp, tot, fre):
    dirs = {'/': {'tot_data': 0}}
    folder = []
    lines = read_inp(inp)
    for line in lines:
        split = line.split(' ')
        if '$ cd ..' in line:
            folder.pop()
        elif '$ cd' in line[0:4]:
            folder.append(split[-1])
        elif '$' not in line:
            if 'dir' in line:
                absdir = ''.join(folder) + split[-1]
                if absdir not in dirs:
                    dirs[absdir] = {'tot_data': 0}
            else:
                dirdir = ''
                for letter in folder:
                    dirdir += letter
                    dirs[dirdir]['tot_data'] += int(split[0])

    totsum_1 = 0
    totsum_2 = tot
    need_space = fre - (tot - dirs['/']['tot_data'])
    for value in dirs.values():
        tdata = value['tot_data']
        if tdata <= 100000:
            totsum_1 += tdata
        if tdata < totsum_2 and tdata - need_space >= 0:
            totsum_2 = tdata

    print('part1:', totsum_1)
    print('part2:', totsum_2)


TOT = 70000000
FRE = 30000000
INP0 = './a0-example.txt'
INP1 = './a1-part1.txt'
solution(INP1, TOT, FRE)
