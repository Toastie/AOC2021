from os import curdir
import statistics

with open("day7/input.txt","r") as input:
    pos = [int(p) for p in input.read().split(",")]

median = statistics.median(pos)

def fuelUsage(pos:list,dest):
    return sum([sum(range(int(abs(crab - dest)) + 1)) for crab in pos])

more = fuelUsage(pos,median+1)
exact = fuelUsage(pos,median)
less = fuelUsage(pos,median-1)

if more > exact and less > exact:
    print(median)
elif more > exact and less < exact:
    dir = -1
    current = less
    p = median  - 1
else:
    dir = 1
    current = more
    p = median + 1

last = current + 1

while(last > current):
    last = current

    p += dir

    current = fuelUsage(pos,p)


print(last)
