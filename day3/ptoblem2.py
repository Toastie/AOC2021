from os import O_EXCL


with open('day3/input.txt','r') as input:
    data = input.read().split("\n")


def mostCommonBit(data:list,pos:int):
    ones = 0

    for j in range(len(data)):
        ones += int(data[j][pos])

    if ones >= (len(data)/2):
        return 1
    else:
        return 0

oxygen = data

for i in range(len(data[0])):
    if len(oxygen) == 1:
        break
    bit = mostCommonBit(oxygen,i)
    oxygen = [value for value in oxygen if int(value[i]) == bit]

co2 = data

for i in range(len(data[0])):
    if len(co2) == 1:
        break
    bit = mostCommonBit(co2,i)
    co2 = [value for value in co2 if int(value[i]) != bit]


print(f"Oxygen: {oxygen}, CO2: {co2}, Multiplied: {int(co2[0],2) * int(oxygen[0],2)}")