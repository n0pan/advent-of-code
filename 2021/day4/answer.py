#!/usr/bin/env python3

test = True
file_name = "test_input" if test else "input"
file = open(file_name).read().strip().split("\n\n")


class BingoBoard:
    board = []

    def __init__(self, board):
        self.board = board

    def display(self):
        print(self.board)

    def has_number(self, number):
        for row_index, row in enumerate(self.board):
            for board_number_index, board_number in enumerate(row):
                if board_number == number:
                    index = int(board_number_index)
                    self.board[row_index][index] = "*"


def get_boards(input):
    def parse_board(i):
        return i.split("\n")

    temp_boards = [parse_board(line) for line in file]
    boards = []
    for i in temp_boards:
        board = []
        for j in i:
            line = j.split(" ")
            line = list(filter(lambda x: x != "", line))
            board.append(line)
        boards.append(board)

    return boards


if __name__ == "__main__":
    input = file.pop(0)
    boards = get_boards(file)

    boards = list(map(lambda board: BingoBoard(board), boards))

    for number in input:
        for board in boards:
            board.has_number(number)
            board.display()

