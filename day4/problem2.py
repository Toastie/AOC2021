with open("day4/input.txt","r") as input:
    temp = input.read()
    numbers = temp.split("\n")[0].split(",")

    cards = [card for card in temp.split("\n\n")[1:]]

    cards = [[string.rstrip("\n") for string in card.split("\n")] for card in cards]

    cards = [[[string for string in line.split(" ") if string != ""] for line in card] for card in cards]


def checkCard(cards:list,number:str):
    for i,card in enumerate(cards):

        if card == []:
            continue

        for j,lines in enumerate(card):
            for k,numbers in enumerate(lines):
                if number == numbers:
                    cards[i][j][k] = "X"
    return cards


def checkBingo(cards:list[list[list]]):
    winners = []
    for i,card in enumerate(cards):

        if card == []:
            continue

        #check lines
        for lines in card:
            if "".join(lines) == "XXXXX":
                winners.append(i)

        #check columns
        for j in range(5):
            if "".join([line[j] for line in card]) == "XXXXX":
                winners.append(i)
    return winners

def score(card:list[list]):
    sum = 0
    for line in card:
        for number in line:
            sum += int(number) if number != "X" else 0
    return sum

for number in numbers:
    print(f"checking number:{number}")
    cards = checkCard(cards,number)

    winners = checkBingo(cards)

    if len(cards) != 1 and winners != []:
        winners = list(dict.fromkeys(winners))
        for winner in winners:
            lastWinner = (cards[winner],number)
            cards[winner] = []
        continue

    if winners != []:
        print(f"Score: {score(cards[0]) * int(number)}")
        quit()

print(f"Score: {score(lastWinner[0]) * int(lastWinner[1])}")


