

# rock: 1 paper: 2 scissor: 3
         #  stone   paper   sciss  <- win
move_dic = {'X': 1, 'Y': 2, 'Z': 3,
            'A': 1, 'B': 2, 'C': 3}

# stone vs: paper (-1 l), sciss (-2 w)
# paper vs: sciss (-1 l), sciss ( 1 w)
# sciss vs: stone ( 2 l), paper ( 1 w)
# win: 6 draw: 3, lose: 0
win_dic = {0: 3, 1: 6, -2: 6, -1: 0, 2: 0}

tot_p = 0
with open('./a1-part1.txt') as file:
    for line in file:
        strip = line.rstrip().split()
        diff = move_dic[strip[1]] - move_dic[strip[0]]
        tot_p += win_dic[diff] + move_dic[strip[1]]
        print(win_dic[diff], move_dic[strip[1]], tot_p)
