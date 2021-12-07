import statistics

with open("day7/input.txt","r") as input:
    pos = [int(p) for p in input.read().split(",")]

def fuelUsage(pos:list,dest):
    return sum([abs(crab - dest) for crab in pos])

print(fuelUsage(pos,statistics.median(pos)))