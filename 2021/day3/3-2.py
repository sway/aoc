# 011010111110
from functools import reduce


def filterLines(lines, criteria, position):
    if len(lines) == 1:
        return lines[0]

    count = len(lines)

    sum = 0
    for l in lines:
        sum += int(l[position])

    digit = int((sum / count) + 0.5)

    match = list(filter(lambda x: int(x[position]) == digit, lines))
    not_match = list(filter(lambda x: int(x[position]) != digit, lines))

    if criteria == 1:
        return filterLines(match, 1, position + 1)
    else:
        return filterLines(not_match, 0, position + 1)


with open("./input") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    a = filterLines(lines, 1, 0)
    b = filterLines(lines, 0, 0)

    print(int(a, 2) * int(b, 2))
