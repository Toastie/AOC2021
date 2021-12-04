with open("day4/input.txt","r") as input:
    temp = input.read()
    numbers = temp.split("\n")[0].split(",")

    cards = [card for card in temp.split("\n\n")[1:]]

    cards = [[string.rstrip("\n") for string in card.split("\n")] for card in cards]

    cards = [[[string for string in line.split(" ") if string != ""] for line in card] for card in cards]


def checkCard(cards:list,number:str):
    for i,card in enumerate(cards):
        for j,lines in enumerate(card):
            for k,numbers in enumerate(lines):
                if number == numbers:
                    cards[i][j][k] = "X"
    return cards


def checkBingo(cards:list[list[list]]):
    for i,card in enumerate(cards):
        #check lines
        for lines in card:
            if "".join(lines) == "XXXXX":
                return i

        #check columns
        for j in range(5):
            if "".join([line[j] for line in card]) == "XXXXX":
                return i
    return -1

def score(card:list[list]):
    sum = 0
    for line in card:
        for number in line:
            sum += int(number) if number != "X" else 0
    return sum

for number in numbers:
    print(f"checking number:{number}")
    cards = checkCard(cards,number)

    winner = checkBingo(cards)
    if winner >= 0:

        print(f"Winner: {winner + 1} with Score: {score(cards[winner]) * int(number)}")

        break

print(winner)

print(cards[winner])
