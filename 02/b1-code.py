

# rock: 1 paper: 2 scissor: 3
         #  lose    draw    win
MOVE_DIC = {'X': 1, 'Y': 2, 'Z': 3, # win cond
            'A': 1, 'B': 2, 'C': 3} # what they play
         #  stone   paper   sciss  -> win

# stone vs: paper (-1 l), sciss (-2 w)
# paper vs: sciss (-1 l), sciss ( 1 w)
# sciss vs: stone ( 2 l), paper ( 1 w)
# win: 6 draw: 3, lose: 0
WIN_DIC = {0: 3, 1: 6, -2: 6, -1: 0, 2: 0}
MOVES = 'ABC'

def part_12(inp, part2=False):
    with open(inp, 'r') as file:

        tot_p = 0
        for line in file:
            strip = line.rstrip().split()

            enem = strip[0]
            if part2:
                # given enem, find ally move
                ally_idx = MOVES.index(enem) + MOVE_DIC[strip[1]] - 2
                ally = MOVES[ally_idx%3]
            else:
                ally = strip[1]

            # add win_dic and move_dic
            diff = MOVE_DIC[ally] - MOVE_DIC[enem]
            tot_p += WIN_DIC[diff] + MOVE_DIC[ally]
    print(tot_p)

INP = './a1-part1.txt'
part_12(INP)
part_12(INP, part2=True)
