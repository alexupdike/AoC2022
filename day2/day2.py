def part1():
    opponent, player, score = 0, 0, 0

    rock = ['A','X']
    paper = ['B','Y']
    scissors = ['C','Z']

    def assignValue(choice):
        if choice in rock:
            return 1
        if choice in paper:
            return 2
        if choice in scissors:
            return 3
        raise ValueError("You cannot chose 'Bomb' as a option.")

    def assignScore():
        if opponent == player:
            return player + 3
        if opponent == 1 and player == 2:
            return player + 6
        if opponent == 2 and player == 3:
            return player + 6
        if opponent == 3 and player == 1:
            return player + 6
        return player


    with open("input.txt") as file:
        for line in file:
            current = line.rstrip()

            opponent = assignValue(current[0])
            player = assignValue(current[2])

            score = score + assignScore()
            
    return score

print("Part 1 score: ", part1())


def part2():
    opponent, player, score = 0, 0, 0

    options = {
        'A': 1, #Rock
        'B': 2, #Paper
        'C': 3  #Scissors
    }

    call = {
        'X': 0, #Lose
        'Y': 3, #Draw
        'Z': 6  #Win
    }

    def runStrat():
        if player == 0:
            if opponent == 1: return player + 3
            if opponent == 2: return player + 1
            if opponent == 3: return player + 2
        if player == 3:
            if opponent == 1: return player + 1
            if opponent == 2: return player + 2
            if opponent == 3: return player + 3
        if player == 6:
            if opponent == 1: return player + 2
            if opponent == 2: return player + 3
            if opponent == 3: return player + 1
        raise ValueError("Abort! strat failure.")


    with open("input.txt") as file:
        for line in file:
            current = line.rstrip()

            opponent = options[current[0]]
            player = call[current[2]]

            score = score + runStrat()
            
    return score

print("Part 2 score: ", part2())