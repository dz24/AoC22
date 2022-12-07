def read_inp(inp):
    lines = []
    with open(inp, 'r') as file:
        for line in file:
            rstrip = line.rstrip()
            lines.append(rstrip)

    return lines


def solution(inp, tot, fre):
    dirs = {'/': {'data': [], 'name': [], 'folders': [], 'tot_data': 0}}
    lines = read_inp(inp)
    dollar = None
    folder = []
    for line in lines:
        if '$ cd ..' in line:
            dollar = 'cd'
            folder.pop()
        elif '$ cd' in line[0:4]:
            dollar = 'cd'
            folder.append(line.split()[-1])
        elif '$ ls' in line[0:4]:
            dollar = 'ls'
        elif dollar == 'ls':
            split = line.split(' ')
            curdir = ''.join(folder)
            if 'dir' in line:
                top_folder = split[-1]
                absdir = curdir + top_folder
                dirs[curdir]['folders'].append(top_folder)
                if absdir not in dirs:
                    dirs[absdir] = {'data': [], 'name': [], 'folders': [],
                                    'tot_data': 0}
            else:
                dirs[curdir]['data'].append(int(split[0]))
                dirs[curdir]['name'].append(split[1])
                dirdir = ''
                for letter in folder:
                    dirdir += letter
                    dirs[dirdir]['tot_data'] += int(split[0])

    totsum = 0
    for _, item in dirs.items():
        if item['tot_data'] <= 100000:
            totsum += item['tot_data']
    dire_l = []
    data_l = []
    for key, item in dirs.items():
        dire_l.append(key)
        data_l.append(item['tot_data'])

    used_space = dirs['/']['tot_data']
    free_space = tot-used_space
    need_space = fre - free_space
    min_data = [i for i in sorted(data_l) if i - need_space >= 0]
    print(min_data[0])


TOT = 70000000
FRE = 30000000

INP0 = './a0-example.txt'
INP1 = './a1-part1.txt'
solution(INP1, TOT, FRE)
