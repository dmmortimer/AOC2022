# returns score for player 2 given this move for player 1 and the desired result
def score2(player1, result):

    player2 = None

    # ABC = Rock Paper Scissors
    # XYZ = lose draw win

    match player1:
        case 'A':
            match result:
                case 'X':
                    player2 = 'Z' # to lose against rock, play scissors
                case 'Y':
                    player2 = 'X'  # to draw against rock, play rock
                case 'Z':
                    player2 = 'Y'   # to win against rock, play paper
        case 'B':
            match result:
                case 'X':
                    player2 = 'X' # to lose against paper, play rock
                case 'Y':
                    player2 = 'Y'  # to draw against paper, play paper
                case 'Z':
                    player2 = 'Z'   # to win against paper, play scissors
        case 'C':
            match result:
                case 'X':
                    player2 = 'Y' # to lose against scissors, play paper
                case 'Y':
                    player2 = 'Z'  # to draw against scissors, play scissors
                case 'Z':
                    player2 = 'X'   # to win against scissors, play rock

    return score(player1,player2)

# returns score for player 2 given these moves for player 1 and player 2
def score(player1, player2):
    x = 0
    # ABC = Rock Paper Scissors = XYZ
    match player2:
        case 'X':
            x += 1  # rock
        case 'Y':
            x += 2  # paper
        case 'Z':
            x += 3  # scissors
    # points for winning 0, 3 or 6
    # rock beats scissors
    if player2 == 'X':  # rock
        if player1 == 'C':  # scissors
            x += 6
        elif player1 == 'A':    # rock
            x += 3
    # scissors beats paper
    elif player2 == 'Z':    # scissors
        if player1 == 'B':  # paper
            x += 6
        elif player1 == 'C':    # scissors
            x += 3
    # paper beats rock
    elif player2 == 'Y':    # paper
        if player1 == 'A':  # rock
            x += 6
        elif player1 == 'B':    # paper
            x += 3

    return x

with open('C:/Users/Danielle/AOC2022/Day02/input.txt') as f:
    total = 0
    for  line in f:
        [player1,result] = line.strip().split()
        total += score2(player1,result)

print("Total score with part two strategy", total)