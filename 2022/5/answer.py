"""day 5"""
#!/usr/bin/env python3

IS_TESTING = True


def parse_file(file_name):
    """read and parse input file"""
    return open(file_name, encoding="utf-8").read().strip()


if __name__ == "__main__":
    FILE_NAME = "test_input" if IS_TESTING else "input"
