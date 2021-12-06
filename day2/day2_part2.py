with open('input') as data:
    instructions = data.read().splitlines()
    data.close()


def main():
    hpos = 0
    depth = 0
    aim = 0
    for item in instructions:
        direction, distance = item.split()
        if direction == "forward":
            hpos += int(distance)
            depth += (aim * int(distance))
        elif direction == "up":
            aim -= int(distance)
        else:
            #depth += int(distance)
            aim += int(distance)
    print(hpos, depth)
    print(hpos * depth)


if __name__ == "__main__":
    main()
