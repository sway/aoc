with open("./input") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

    position = {
        "d": 0,  # depth
        "h": 0,  # horizontal
        "a": 0,  # aim
    }

    for l in lines:
        command, amount = l.split(" ")
        print(command, amount)

        if command == "up":
            position["a"] = position["a"] - int(amount)

        if command == "down":
            position["a"] = position["a"] + int(amount)

        if command == "forward":
            position["h"] = position["h"] + int(amount)
            position["d"] = position["d"] + (int(amount) * position["a"])

    print(position)
