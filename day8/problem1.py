with open("day8/input.txt","r") as input:
    output = [line.split(" | ")[1].rstrip("\n").split() for line in input.readlines()]

sum = 0

for line in output:
    for item in line:
        sum += 1 if len(item) in [1,3,4,8] else 0

print(sum)
