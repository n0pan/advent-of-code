f = open("./inputs/day5.txt")
boarding_passes = filter(lambda x: x != "", f.read().split("\n"))

INITIAL_ROW_RANGE = range(128)
INITIAL_COLUMN_RANGE = range(8)

FRONT = "F"
BACK = "B"
LEFT = "L"
RIGHT = "R"

seats = []


def get_lower_half(value_range):
    return value_range[slice(len(value_range) / 2)]


def get_upper_half(value_range):
    return value_range[slice(len(value_range) / 2, len(value_range))]


def get_seat_id(row, column):
    return row * 8 + column


for boarding_pass in boarding_passes:
    row = boarding_pass[slice(7)]
    column = boarding_pass[slice(7, len(boarding_pass))]

    current_row_range = INITIAL_ROW_RANGE
    current_column_range = INITIAL_COLUMN_RANGE

    for index, value in enumerate(row):
        if index == len(row):
            if value == FRONT:
                current_row_range = current_row_range[0]
            elif value == BACK:
                current_row_range = current_row_range[1]
        else:
            if value == FRONT:
                current_row_range = get_lower_half(current_row_range)
            elif value == BACK:
                current_row_range = get_upper_half(current_row_range)

    row = current_row_range[0]

    for index, value in enumerate(column):
        if index == len(column):
            if value == LEFT:
                current_column_range = current_column_range[0]
            elif value == RIGHT:
                current_column_range = current_column_range[1]
        else:
            if value == LEFT:
                current_column_range = get_lower_half(current_column_range)
            elif value == RIGHT:
                current_column_range = get_upper_half(current_column_range)

    column = current_column_range[0]

    seats.append(
        {
            "row": row,
            "column": column,
            "pass": boarding_pass,
            "seat_id": get_seat_id(row, column),
        }
    )


def seat_id(e):
    return e["seat_id"]


seats.sort(key=seat_id)

seat_ids = list(map((lambda x: x["seat_id"]), seats))
full_seat_ids = range(seat_ids[0], len(seat_ids))


def contains_seat_id(e):
    if e not in seat_ids:
        return True


print(filter(contains_seat_id, full_seat_ids))

f.close()
