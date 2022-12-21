f = open('input.txt', 'r').readlines()

elfTotal = 0
myTotal = 0

# f = open("input.txt", "r").readlines()

elfOptions = {
    'A': 1,
    'B': 2,
    'C': 3
}

outcomes = {
    'W': 6,
    'L': 0,
    'D': 3
}

myOptions = {
    'X': 1,
    'Y': 2,
    'Z': 3
}


def playGame(elfOption, myOption):
    elfOpt = elfOptions[elfOption]
    myOpt = myOptions[myOption]

    if elfOpt == myOpt:
        return {'Me': 'D', 'Elf': 'D'}

    if (elfOpt == 3 and myOpt == 1) or (elfOpt == 2 and myOpt == 3) or (elfOpt == 1 and myOpt == 2):
        return {'Me': 'W', 'Elf': 'L'}

    return {'Me': 'L', 'Elf': 'W'}


for game in f:
    game = game.replace(" ", "").replace("\n", "")
    game = list(game)
    myTotal += outcomes[playGame(game[0], game[1])['Me']] + myOptions[game[1]]
    elfTotal += outcomes[playGame(game[0], game[1])
                         ['Elf']] + elfOptions[game[0]]

print(f"Part 1: {myTotal}")


def playGame2(elfOption, myOption):
    elfOpt = elfOptions[elfOption]
    myOpt = myOptions[myOption]

    if myOpt == 2:
        return elfOpt + 3

    if myOpt == 3:
        if elfOpt == 1:
            return 6 + 2
        if elfOpt == 2:
            return 3 + 6
        if elfOpt == 3:
            return 1 + 6

    if myOpt == 1:
        if elfOpt == 1:
            return 3
        elif elfOpt == 2:
            return 1
        elif elfOpt == 3:
            return 2


myTotal = 0

for game in f:
    game = game.replace(" ", "").replace("\n", "")
    game = list(game)
    myTotal += playGame2(game[0], game[1])

print(f"Part 2: {myTotal}")
