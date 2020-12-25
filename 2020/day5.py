from math import floor, ceil

FRONT = "F"
BACK = "B"
LEFT = "L"
RIGHT = "R"

ROW_RANGE = {"start": 0, "end": 127}
COLUMN_RANGE = {"start": 0, "end": 7}

SEAT = {"pass": "", "row": ROW_RANGE, "column": COLUMN_RANGE, "seatID": ""}


def get_seat(boarding_pass, current_char_index, current_seat):
    if current_char_index <= len(boarding_pass) - 1:
        if boarding_pass[current_char_index] == FRONT:
            if boarding_pass[current_char_index + 1] == LEFT:
                return get_seat(
                    boarding_pass,
                    current_char_index + 1,
                    {
                        "pass": boarding_pass,
                        "row": {
                            "start": current_seat["row"]["start"],
                            "end": current_seat["row"]["start"],
                        },
                        "column": current_seat["column"],
                        "seatID": "",
                    },
                )
            elif boarding_pass[current_char_index + 1] == RIGHT:
                return get_seat(
                    boarding_pass,
                    current_char_index + 1,
                    {
                        "pass": boarding_pass,
                        "row": {
                            "start": current_seat["row"]["end"],
                            "end": current_seat["row"]["end"],
                        },
                        "column": current_seat["column"],
                        "seatID": "",
                    },
                )
            else:
                return get_seat(
                    boarding_pass,
                    current_char_index + 1,
                    {
                        "pass": boarding_pass,
                        "row": {
                            "start": current_seat["row"]["start"],
                            "end": floor(current_seat["row"]["end"] / 2),
                        },
                        "column": current_seat["column"],
                        "seatID": "",
                    },
                )
        elif boarding_pass[current_char_index] == BACK:
            return get_seat(
                boarding_pass,
                current_char_index + 1,
                {
                    "pass": boarding_pass,
                    "row": {
                        "start": ceil(current_seat["row"]["end"] / 2),
                        "end": current_seat["row"]["end"],
                    },
                    "column": current_seat["column"],
                    "seatID": "",
                },
            )
        elif boarding_pass[current_char_index] == LEFT:
            if current_char_index == len(boarding_pass) - 1:
                return get_seat(
                    boarding_pass,
                    current_char_index + 1,
                    {
                        "pass": boarding_pass,
                        "row": current_seat["row"],
                        "column": {
                            "start": current_seat["column"]["start"],
                            "end": current_seat["column"]["start"],
                        },
                        "seatID": "",
                    },
                )
            else:
                return get_seat(
                    boarding_pass,
                    current_char_index + 1,
                    {
                        "pass": boarding_pass,
                        "row": current_seat["row"],
                        "column": {
                            "start": current_seat["column"]["start"],
                            "end": floor(current_seat["column"]["end"] / 2),
                        },
                        "seatID": "",
                    },
                )
        elif boarding_pass[current_char_index] == RIGHT:
            if current_char_index == len(boarding_pass) - 1:
                return get_seat(
                    boarding_pass,
                    current_char_index + 1,
                    {
                        "pass": boarding_pass,
                        "row": current_seat["row"],
                        "column": {
                            "start": current_seat["column"]["end"],
                            "end": current_seat["column"]["end"],
                        },
                        "seatID": "",
                    },
                )
            else:
                return get_seat(
                    boarding_pass,
                    current_char_index + 1,
                    {
                        "pass": boarding_pass,
                        "row": current_seat["row"],
                        "column": {
                            "start": ceil(current_seat["column"]["end"] / 2),
                            "end": current_seat["column"]["end"],
                        },
                        "seatID": "",
                    },
                )
    else:
        return {
            "pass": current_seat["pass"],
            "row": current_seat["row"],
            "column": current_seat["column"],
            "seatID": current_seat["row"]["start"] * 8 + current_seat["column"]["start"],
        }


if __name__ == "__main__":
    f = open("./inputs/day5.txt")
    boarding_passes = filter(lambda x: x != "", f.read().split("\n"))
    seats = []

    for boarding_pass in boarding_passes:
        seat = get_seat(boarding_pass, 0, SEAT)
        seats.append(seat)

    def seatID(elem):
        return elem["seatID"]

    seats.sort(reverse=True, key=seatID)

    print(seats[0])

    f.close()
