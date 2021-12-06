# 011010111110

with open("./input") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    sums = [0] * 12
    numbers = len(lines) / 2

    for l in lines:
        for i in range(0, 12):
            sums[i] += int(l[i])

    print(sums)

    gamma = ""
    epsilon = ""

    for i in range(0, 12):
        if sums[i] > numbers:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(gamma, epsilon)

    print(int(gamma, 2) * int(epsilon, 2))
