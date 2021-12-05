with open("day5/input.txt","r") as input:
    lines = input.readlines()

lines = [line.rstrip("\n") for line in lines]
lines = [[[int(coord.split(",")[0]), int(coord.split(",")[1])] for coord in line.split(" -> ")] for line in lines]



grid = [[0 for i in range(1000)] for i in range(1000)]

def interpolate(p1:list,p2:list):

    x = p1[0]
    y = p1[1]

    points =[[x,y]]

    while True:
        if x == p2[0] and y == p2[1]:
            return points
        if x < p2[0]:
            x += 1
        if x > p2[0]:
            x -= 1

        if y < p2[1]:
            y += 1
        if y > p2[1]:
            y -= 1

        points.append([x,y])


def drawLine(line:list[list],grid:list[list]) -> list[list]:

    draw = interpolate(line[0],line[1])

    for point in draw:
        grid[point[1]][point[0]] += 1

    return grid


for line in lines:
    grid = drawLine(line,grid)


sum = 0
for line in grid:
    for number in line:
        sum += 1 if number > 1 else 0


print(sum)
