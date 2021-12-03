def parse_input():
    f = open("input.py", "r")
    lines = f.readlines()
    return lines


def get_directions_from_line(line):
    line = line.replace("\n", "")
    directions = line.split(" ")
    return directions


def part_one(input):
    horizontal = 0
    depth = 0

    for line in input:
        directions = get_directions_from_line(line)
        direction = directions[0]
        value = int(directions[1])
        if direction == "forward":
            horizontal += value
        elif direction == "up":
            depth -= value
        elif direction == "down":
            depth += value

    print("horizontal", horizontal)
    print("depth", depth)
    print(horizontal * depth)


def part_two(input):
    horizontal = 0
    depth = 0
    aim = 0

    for line in input:
        directions = get_directions_from_line(line)
        direction = directions[0]
        value = int(directions[1])
        if direction == "forward":
            horizontal += value
            depth += aim * value
        elif directions[0] == "up":
            aim -= value
        elif directions[0] == "down":
            aim += value

    print("horizontal", horizontal)
    print("depth", depth)
    print(horizontal * depth)


if __name__ == "__main__":
    input = parse_input()

    part_one(input)
    part_two(input)
