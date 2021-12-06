with open("./input") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    position = {
        "d": 0,
        "h": 0,
    }

    for l in lines:
        command, amount = l.split(" ")
        print(command, amount)

        if command == "forward":
            position["h"] = position["h"] + int(amount)

        if command == "up":
            position["d"] = position["d"] - int(amount)

        if command == "down":
            position["d"] = position["d"] + int(amount)

    print(position)
