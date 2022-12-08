#!/usr/bin/env python3

is_testing = False
file_name = "test_input" if is_testing else "input"
turns = open(file_name).read().strip().split("\n")

scores = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

WIN_SCORE = 6
DRAW_SCORE = 3
LOSS_SCORE = 0

total_score = 0

def add_draw_score(move):
    global total_score
    total_score += DRAW_SCORE + scores[move]

def add_win_score(move):
    global total_score
    total_score += WIN_SCORE + scores[move]

def add_loss_score(move):
    global total_score
    total_score += LOSS_SCORE + scores[move]

if __name__ == "__main__":
    for turn in turns:
        moves = turn.split(" ")

        match moves[0]:
            case "A":
                if moves[1] == "X":
                    add_loss_score("Z")
                elif moves[1] == "Y":
                    add_draw_score("X")
                else:
                    add_win_score("Y")
            case "B":
                if moves[1] == "X":
                    add_loss_score("X")
                elif moves[1] == "Y":
                    add_draw_score("Y")
                else:
                    add_win_score("Z")
            case "C":
                if moves[1] == "X":
                    add_loss_score("Y")
                elif moves[1] == "Y":
                    add_draw_score("Z")
                else:
                    add_win_score("X")

    print(total_score)
