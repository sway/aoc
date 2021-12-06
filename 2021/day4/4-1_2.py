#!/usr/local/bin/python3

import re
import numpy

with open("./input") as file:
    input = file.readline()
    lines = file.read()

    lines = re.sub(r'(?<=[0-9])\n', ' ', lines)
    lines = re.sub(r" {1,2}", " ", lines)

    puzzles = []

    for line in lines.split("\n")[1:]:
        line = line.strip().split(" ")
        puzzle = numpy.mat(
            list(map(lambda x: int(x), line))).reshape(5, 5)
        puzzles.append(puzzle)

    for i in input.split(","):
        i = int(i)
        nextPuzzles = []
        for p in puzzles:
            numpy.putmask(p, p == i, [-1])
            cSums = numpy.sum(p, axis=0)
            rSums = numpy.sum(p, axis=1)
            if -5 in cSums or -5 in rSums:
                numpy.putmask(p, p == -1, [0])
                print(numpy.sum(p) * i)
            else:
                nextPuzzles.append(p)
        puzzles = nextPuzzles
