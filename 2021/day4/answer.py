#!/usr/bin/env python3

test = True
file_name = "test_input" if test else "input"
file = open(file_name).read().strip().split("\n")


class BingoBoard:
    board = []

    def __init__(self, board):
        self.board = board


if __name__ == "__main":
    print('test')
