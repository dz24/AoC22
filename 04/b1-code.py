unions = 0
non_overlap = 0

with open('./a1-part1.txt', 'r') as read:
    for line in read:
        split = line.rstrip().split(',')
        split_a = split[0].split('-')
        split_b = split[1].split('-')
        range_a = list(range(int(split_a[0]), int(split_a[1]) + 1))
        range_b = list(range(int(split_b[0]), int(split_b[1]) + 1))

        # part 1
        union = set(range_a) & set(range_b)
        if True in (union == set(i) for i in [range_a, range_b]):
            unions += 1

        # part 2
        if len(set(range_a) & set(range_b)) > 0:
            non_overlap += 1

print(unions)
print(non_overlap)
