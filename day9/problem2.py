with open("day9/input.txt","r") as input:
    map = [data.rstrip("\n") for data in input.readlines() ]
    map = [[int(char) for char in data] for data in map]

low_points = []

checked = []

def basinSize(point:tuple,pre:int):
    size = 1
    i = point[0]
    j = point[1]
    v = map[i][j]

    if (i,j) in checked:
        return 0
    else:
        checked.append((i,j))

    if i and pre != 0:
        if map[i-1][j] != 9 and map[i-1][j] > v:
            size += basinSize((i-1,j),2)
    if i < len(map) - 1 and pre != 2:
        if map[i+1][j] != 9 and map[i+1][j] > v:
            size += basinSize((i+1,j),0)
    if j and pre != 4:
        if map[i][j-1] != 9 and map[i][j-1] > v:
            size += basinSize((i,j-1),1)
    if j < len(map[i]) - 1 and pre != 1:
        if map[i][j+1] != 9 and map[i][j+1] > v:
            size += basinSize((i,j+1),4)

    return size


for i,line in enumerate(map):
    low = True
    for j,v in enumerate(line):
        low = True
        if i:
            if v >= map[i-1][j]:
                low = False
                continue
        if j:
            if v >= map[i][j-1]:
                low = False
                continue
        if i < len(map) -1:
            if v >= map[i+1][j]:
                low = False
                continue
        if j < len(line) -1:
            if v >= map[i][j+1]:
                low = False 
                continue
        if low:
            low_points.append((i,j))


size = [basinSize(point,-1) for point in low_points]

size.sort()

size = size[-3:]

print(size[0] * size[1] * size[2])