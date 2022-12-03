print('ape')


prio_str = 'abcdefghijklmnopqrstuvwxyz' + \
           'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
prio = 0

with open('./a1-part1.txt', 'r') as read:
    for line in read:
        split = line.rstrip()
        halflen= int(len(split)/2)
        part_a = set(sorted(split[:halflen]))
        part_b = set(sorted(split[halflen:]))
        
        for letter in part_a:
            if letter in part_b:
                prio += prio_str.index(letter) + 1
                break
        
print(prio)
