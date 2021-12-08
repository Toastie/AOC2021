with open("day6/input.txt","r") as input:
    fish = list(map(int,input.read().split(",")))

days = [0,0,0,0,0,0,0,0,0]

for f in fish:
    days[f] += 1

total = len(fish)

for i in range(256):
    total += days[0]

    temp = days[0]
    days = days[1:] + [0]

    days[6] += temp
    days[8] = temp

print(total)
