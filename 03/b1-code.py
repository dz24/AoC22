prio_str = 'abcdefghijklmnopqrstuvwxyz' + \
           'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
prio = 0
badg = 0
lines = []

with open('./a1-part1.txt', 'r') as read:
    for line in read:
        # part 1
        split = line.rstrip()
        halflen= int(len(split)/2)
        part_a = list(set(split[:halflen]))
        part_b = list(set(split[halflen:]))

        part_set = set(part_a + part_b)
        part_set_str = ''.join(part_a + part_b)
        for letter in part_set:
            if part_set_str.count(letter) == 2:
                prio += prio_str.index(letter) + 1
                break

        # part 2
        lines.append(''.join((set(split))))
        if len(lines) == 3:
            group = ''.join(lines)
            group_set = set(group)
            for letter in group_set:
                if group.count(letter) == 3:
                    badg += prio_str.index(letter) + 1
                    break
            lines = []

print('part 1:', prio)
print('part 2:', badg)
