
def calculate_seat(input):

    seats = []

    # Part A - convert to binary
    for seat in input:
        seats.append(int(seat.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2))

    # Part B check for missing seat in range
    for seat_id in range(min(seats), max(seats)):
        if seat_id not in seats and seat_id - 1 in seats and seat_id + 1 in seats:
            missing_seat = seat_id

    return max(seats), missing_seat


def iterate(low, high, input, inc_char):
    for char in input:
        mid = (low+high) // 2
        if char == inc_char:
            low = mid
        else:
            high = mid
    return low



def main():
    input = open("./five/input.txt", "r")

    part_a, part_b = calculate_seat(input)
    print("5a. Answer is %s" % part_a)

    print("5b. Answer is %s" % part_b)
