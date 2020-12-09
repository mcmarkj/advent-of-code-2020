def find_property(file_input, max_steps):
    for i in range(len(file_input)):
        try:
            preamble_range = []
            curr = i + int(max_steps)
            curr = file_input[curr]
            for x in range(int(max_steps)):
                pos = x+i
                preamble_range.append(file_input[pos])

            if not iterate_range(curr, preamble_range):
                return(curr)
        except IndexError:
            return


def iterate_range(curr, preamble_range):
    for x in preamble_range:
        for y in reversed(preamble_range):
            if (int(x) + int(y) == int(curr)) and x != y:
                return True
    return False


def find_weakness(numbers, invalid):
    pos1 = 0
    pos2 = 2
    while sum(numbers[pos1:pos2]) != int(invalid):
        if sum(numbers[pos1:pos2]) < int(invalid):
            pos2 += 1
        else:
            pos1 += 1
            pos2 = pos1 + 2
    return min(numbers[pos1:pos2 + 1]) + max(numbers[pos1:pos2 + 1])


def main():
    file_input = []

    file = open("./nine/input.txt", "r")
    for line in file.readlines():
        numbers = line.split()
        file_input.append(numbers)

    with open('./nine/input.txt', 'r') as file_:
        file_input = list(map(int, file_.read().split()))

    answer_a = find_property(file_input, "25")
    print("9A. Answer is %s" % answer_a)

    answer_b = find_weakness(file_input, answer_a)
    print("9b. Answer is %s" % answer_b)