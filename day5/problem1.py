with open("day5/input.txt","r") as input:
    lines = input.readlines()

lines = [line.rstrip("\n") for line in lines]
lines = [[[int(coord.split(",")[0]), int(coord.split(",")[1])] for coord in line.split(" -> ")] for line in lines]

lines = [line for line in lines if (line[0][0] == line[1][0] or line[0][1] == line[1][1])]

grid = [[0 for i in range(1000)] for i in range(1000)]

def drawLine(line:list[list],grid:list[list]) -> list[list]:
    x1 = min(line[0][0],line[1][0])
    y1 = min(line[0][1],line[1][1])

    x2 = max(line[1][0],line[0][0])
    y2 = max(line[1][1],line[0][1])

    while x1 <= x2:
        temp = y1
        while temp <= y2:
            grid[temp][x1] += 1
            temp += 1
        x1 += 1
    return grid

for line in lines:
    grid = drawLine(line,grid)


sum = 0
for line in grid:
    for number in line:
        sum += 1 if number > 1 else 0

print(sum)