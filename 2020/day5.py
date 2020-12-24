from math import floor, ceil

FRONT = "F"
BACK = "B"
LEFT = "L"
RIGHT = "R"

ROW_RANGE = {"start": 0, "end": 127}
COLUMN_RANGE = {"start": 0, "end": 7}

def get_seat(boarding_pass, current_char_index, current_range):
    current_boarding_pass_char = boarding_pass[current_char_index]
    
    if current_char_index <= len(boarding_pass) - 1:
        if current_boarding_pass_char == FRONT:
            get_seat(
                boarding_pass,
                current_char_index + 1,
                {
                    "start": current_range["start"],
                    "end": floor(current_range["end"] / 2),
                },
            )
        elif current_boarding_pass_char == BACK:
            get_seat(
                boarding_pass,
                current_char_index + 1,
                {
                    "start": ceil(current_range["start"] / 2),
                    "end": current_range["end"],
                },
            )
        elif current_boarding_pass_char == LEFT:
            get_seat(
                    boarding_pass,
                    current_char_index + 1,
                    {
                        "start": 
                        }
                    )


    else:
        print("done")


if __name__ == "__main__":
    f = open("./inputs/day5.txt")
    boarding_passes = filter(lambda x: x != "", f.read().split("\n"))

    for boarding_pass in boarding_passes:
        get_seat(boarding_pass, 0, ROW_RANGE)

    f.close()
