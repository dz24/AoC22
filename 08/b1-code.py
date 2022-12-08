import numpy as np

def reader(inp):
    with open(inp, 'r') as read:
        array = [] 
        for line in read:
            array.append([int(i) for i in line.rstrip()])

    # pad: add zeros between the forest
    square = np.array(array)
    padded_square = np.pad(square, square.shape, constant_values=-1)
    return padded_square, square.shape
        
def solution(inp):
    square, shape = reader(inp)
    roll_tally = np.zeros(square.shape, dtype=int)
    roll_mult = np.copy(square)
    roll_mult[square >= 0] = 1
    roll_mal = np.copy(roll_mult)

    # right -> left -> down -> up
    for li in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        roll_tally_0 = np.zeros(square.shape, dtype=int)
        roll_tally_1 = np.zeros(square.shape, dtype=int)
        roll_lock = np.copy(roll_mal)
        for i in range(1, shape[0]+1):
            if li[0]*i == li[1]*i == 0:
                continue
            rolled = np.roll(square, (li[0]*i, li[1]*i), axis=(0, 1))

            # part 1
            roll_tally_0 += square > rolled
            # part 2
            roll_lock[rolled == -1] = 0
            roll_tally_1 += (square != -1)*roll_lock
            roll_lock[square <= rolled] = 0

        roll_tally += roll_tally_0 == shape[0]
        roll_mult *= roll_tally_1

    print('part 1:', np.sum(roll_tally>0))
    print('part 2:', np.max(roll_mult))


INP0 = './a0-example.txt'
INP1 = './a1-part1.txt'
solution(INP1)
