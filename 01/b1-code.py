def part1(inp):
    calories = [0]
    with open(inp, 'r') as read:
        for line in read:
            strip = line.rstrip()
            if len(strip) == 0:
                calories.append(0)
            else:
                calories[-1] += int(strip)
    
    print('part 1:', max(calories))
    return calories
    
def part2(inp):
    calories = part1(inp)
    top_three = 0
    for _ in range(3):
        maxidx = calories.index(max(calories))
        top_three += calories.pop(maxidx)
    print('part 2:', top_three)

example = './a0-example.txt'
inp = './a1-part1.txt'
part2(inp)
