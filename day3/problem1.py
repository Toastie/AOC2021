with open('day3/input.txt','r') as input:
    data = input.read().split("\n")

gamma = ""
epsilon = ""

for i in range(len(data[0])):
    ones = 0
    for j in range(len(data)):
        ones += int(data[j][i])

    if ones > (len(data) / 2):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print(f"Gamma: {gamma}, Epsilon: {epsilon}, Multiplied: {int(gamma,2) * int(epsilon,2)}")