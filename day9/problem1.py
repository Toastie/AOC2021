from typing import Counter


with open("day9/input.txt","r") as input:
    map = [data.rstrip("\n") for data in input.readlines() ]
    map = [[int(char) for char in data] for data in map]

risk = 0


for i,line in enumerate(map):
    low = True
    for j,v in enumerate(line):
        low = True
        n = []
        if i:
            n.append(map[i-1][j])
            if v >= map[i-1][j]:
                low = False
                continue
        if j:
            n.append(map[i][j-1])
            if v >= map[i][j-1]:
                low = False
                continue
        if i < len(map) -1:
            n.append(map[i+1][j])
            if v >= map[i+1][j]:
                low = False
                continue
        if j < len(line) -1:
            n.append(map[i][j+1])
            if v >= map[i][j+1]:
                low = False 
                continue
        if low:
            print((i,j,v,n))
            risk += (1 + v)

print(risk)