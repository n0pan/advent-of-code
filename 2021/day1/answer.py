from input import input


def partOne():
    counter = 0
    for index, value in enumerate(input):
        if index != 0:
            if value > input[index - 1]:
                counter += 1
    print(counter)


def partTwo():
    counter = 0
    for index, value in enumerate(input):
        if 0 < index <= len(input) - 3:
            first_window = input[index - 1] + input[index] + input[index + 1]
            second_window = input[index] + input[index + 1] + input[index + 2]
            if second_window > first_window:
                counter += 1
    print(counter)


if __name__ == "__main__":
    partTwo()
