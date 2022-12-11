#!/usr/bin/env python3

is_testing = False


def get_sections(file_name):
    parsed_file = open(file_name).read().strip().split("\n")
    sections = []

    for item in parsed_file:
        sections.append(item.split(","))

    return sections


def get_range(section):
    split_section = section.split("-")
    return (int(split_section[0]), int(split_section[1]))


def part_one():
    file_name = "test_input" if is_testing else "input"
    sections = get_sections(file_name)

    result_count = 0

    for section in sections:
        first_min_value, first_max_value = get_range(section[0])
        second_min_value, second_max_value = get_range(section[1])

        if (
            (second_min_value >= first_min_value
             and second_min_value <= first_max_value)
            and (second_max_value >= first_min_value
                 and second_max_value <= first_max_value)
        ) or (
            (first_min_value >= second_min_value
             and first_min_value <= second_max_value)
            and (first_max_value >= second_min_value
                 and first_max_value <= second_max_value)
        ):
            result_count += 1

    print("part 1:", result_count)


def part_two():
    file_name = "test_input" if is_testing else "input"
    sections = get_sections(file_name)

    count = 0

    for section in sections:
        first_min_value, first_max_value = get_range(section[0])
        second_min_value, second_max_value = get_range(section[1])

        first_list = range(first_min_value, first_max_value + 1)
        second_list = range(second_min_value, second_max_value + 1)
        total_list_length = len(first_list) + len(second_list)

        merged_list = list(first_list) + \
            list(set(second_list) - set(first_list))
        merged_list_length = len(merged_list)

        if (merged_list_length < total_list_length):
            count += 1

    print("part 2:", count)


if __name__ == "__main__":
    part_one()
    part_two()
