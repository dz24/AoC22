def read_inp(inp):
    lines = []
    with open(inp, 'r') as file:
        for line in file:
            rstrip = line.rstrip()
            lines.append(rstrip)
            
    return lines


def part1(inp):
    dirs = {'/': {'data': [], 'name': [], 'folders': []}}
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
            curdir = ''.join(folder)
            split = line.split(' ')
            if 'dir' in line:
                top_folder = split[-1]
                absdir = curdir + top_folder
                dirs[curdir]['folders'].append(top_folder)
                if absdir not in dirs:
                    dirs[absdir] = {'data': [], 'name': [], 'folders': []}
            else:
                dirs[curdir]['data'].append(int(split[0]))
                dirs[curdir]['name'].append(split[1])

    # print(dirs)
    totsum = 0
    for key, item in dirs.items():
        if sum(item['data']) <= 100000:
            print(item, sum(item['data']))
            totsum += sum(item['data'])
    print(totsum)

INP0 = './a0-example.txt'
part1(INP0)
