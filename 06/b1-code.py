def read_file(inp):
    with open(inp, 'r') as read:
        for line in read:
            rstrip = line.rstrip()
    return rstrip


def solution(inp, signal_len=14):
    line = read_file(inp)
    signal = []
    for idx, letter in enumerate(line):
        signal.append(letter)
        if len(signal) == signal_len:
            if len(set(signal)) == signal_len:
                print(idx+1, ''.join(signal))
                break
            else:
                signal = signal[1:]

INP0 = './a0-example.txt'
INP1 = './a1-part1.txt'
solution(INP1, signal_len=4)
solution(INP1, signal_len=14)

