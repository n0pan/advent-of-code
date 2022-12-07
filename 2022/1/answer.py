#!/usr/bin/env python3

is_testing = False
file_name = "test_input" if is_testing else "input"
list_of_elves = open(file_name).read().strip().split("\n")


if __name__ == "__main__":
    calories = []
    current_elf_calories = 0

    for item in list_of_elves:
        if item == "":
            calories.append(current_elf_calories)
            current_elf_calories = 0
        else:
            current_elf_calories += int(item)

    calories.sort(reverse=True)
    print(calories[0] + calories[1] + calories[2])
