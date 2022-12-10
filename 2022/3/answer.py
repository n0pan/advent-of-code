#!/usr/bin/env python3

item_types = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

is_testing = False
file_name = "test_input" if is_testing else "input"


def parse_file(file_name):
    return open(file_name).read().strip().split("\n")


def get_rucksack_compartments(ruckshack):
    first_half = ruckshack[0 : (int(len(ruckshack) / 2))]
    second_half = ruckshack[int(len(ruckshack) / 2) : len(ruckshack)]
    return [first_half, second_half]


def part_one():
    priority_sum = 0

    ruckshacks = parse_file(file_name)

    for ruckshack in ruckshacks:
        compartments = get_rucksack_compartments(ruckshack)
        repeating_item_type = ""
        for item_type_1 in compartments[0]:
            for item_type_2 in compartments[1]:
                if item_type_1 == item_type_2 and item_type_1 != repeating_item_type:
                    repeating_item_type = item_type_1
                    priority_sum += item_types.index(item_type_1) + 1

    print("part_one", priority_sum)


def part_two():
    def parse_groups():
        ruckshacks = parse_file(file_name)

        groups_of_elves = []
        count = 0

        while count <= len(ruckshacks) - 1:
            groups_of_elves.append(
                [ruckshacks[count], ruckshacks[count + 1], ruckshacks[count + 2]]
            )
            count += 3

        return groups_of_elves

    groups_of_elves = parse_groups()
    priority_sum = 0

    for group in groups_of_elves:
        first_items = group[0]
        second_items = group[1]
        third_items = group[2]

        repeating_type = []

        for first_item_type in first_items:
            for second_item_type in second_items:
                if first_item_type == second_item_type:
                    for third_item_type in third_items:
                        if (
                            first_item_type == third_item_type
                            and first_item_type not in repeating_type
                        ):
                            repeating_type.append(first_item_type)
                            priority_sum += item_types.index(first_item_type) + 1

    print("part_two:", priority_sum)


if __name__ == "__main__":
    part_one()
    part_two()
