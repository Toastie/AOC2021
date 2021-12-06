with open("day6/input.txt","r") as input:
    fish = list(map(int,input.read().split(",")))

fish2 = fish.copy()

for i in range(80):

    fish = fish2.copy()

    for j,f in enumerate(fish):
        if f == 0:
            fish2[j] = 6
            fish2.append(8)
        else:
            fish2[j] -= 1

print(len(fish2))