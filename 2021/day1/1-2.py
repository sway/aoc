with open("./input") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]

    entries = len(lines)

    sum = 0
    previousSum = 999999999
    count = 0

    for i in range(0, entries - 2):
        s = lines[i] + lines[i + 1] + lines[i + 2]
        print("{}: {} + {} + {} = {} ({})".format(i,
                                                  lines[i], lines[i + 1], lines[i + 2], s, s > previousSum))
        if s > previousSum:
            count = count + 1
        previousSum = s
        sum = 0

    print(count)
