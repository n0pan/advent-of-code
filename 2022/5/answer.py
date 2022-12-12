#!/usr/bin/env python3

is_testing = True


def parse_file(file_name):
    return open(file_name).read().strip()


if __name__ == "__main__":
    file_name = "test_input" if is_testing else "input"
