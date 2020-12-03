def climb_slope(file, x, y):
    # Index 0 so adding 1 to start in the right place
    current_x = 1
    current_y = 0
    trees_encountered = 0
    max_rows = len(file)

    for i in range(max_rows):
        # Increment both by x (across) y (down)
        current_y += y
        current_x += x
        try:
            row = file[current_y]
            # We use index zero so subtract 1 from X
            slope_obj = row[current_x - 1]

            if slope_obj == "#":
                trees_encountered += 1

        except IndexError:
            # We've most likely hit the end of the file
            return trees_encountered
    return trees_encountered


def repeat_input(file, n):
    repeated_input = []
    for row in file:
        # Strip line breaks
        row = row.rstrip()
        # Repeat n times into new array with a line break at the end
        repeated_input.append("%s\n" % (row * n))
    return repeated_input


def calculate_b(file):

    step_A = climb_slope(file, 1, 1)
    step_B = climb_slope(file, 3, 1)
    step_C = climb_slope(file, 5, 1)
    step_D = climb_slope(file, 7, 1)
    step_E = climb_slope(file, 1, 2)

    return step_A * step_B * step_C * step_D * step_E


def main():
    input = open("./three/input.txt", "r")
    input = repeat_input(input, 73)

    part_a = climb_slope(input, 3, 1)
    print("3a. Answer is %s" % part_a)

    part_b = calculate_b(input)
    print("3b. Answer is %s" % part_b)
