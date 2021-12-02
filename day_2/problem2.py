depth = 0
pos = 0
aim = 0
with open('input.txt', "r") as input:
    for line in input:
        if line.count("up"):
            aim -= int(line.split(" ")[1].rstrip("\n"))

        elif line.count("down"):
            aim += int(line.split(" ")[1].rstrip("\n"))

        else:
            print(aim)
            pos += int(line.split(" ")[1].rstrip("\n"))
            depth = depth + aim * int(line.split(" ")[1].rstrip("\n"))

print(f"depth: {depth}")
print(f"Pos: {pos}")

print(f"Combinded: {pos*depth}")