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
        [player1,player2] = line.strip().split()
        total += score(player1,player2)

print("Total score", total)