def run_ins(input, stage="a"):
    # Array we'll use to track what we've already done
    completed = []
    pos = 0
    i = 0
    while i < len(input):
        # If we've already done this iteration before, return the value
        if i in set(completed):
            if stage == "a":
                return pos
            else:
                # In part b this would be considered a failure as we'd iterate again and go into an infinate loop
                return False

        completed.append(i)
        instruction = input[i][0]
        action = input[i][1]

        if instruction == "acc":
            pos += int(action)
            i += 1
        elif instruction == "nop":
            i += 1
        elif instruction == "jmp":
            i += int(action)

    return pos


def repair(input, input_raw):
    # Part B - find the bad command and replace it.
    for i in range(len(input)):
        # A tmp array that we'll change on the fly and send into the function to see if it fixes the iteration

        tmp_arry = []
        for line in input_raw:
            # split by space
            tmp_arry.append(line.split())

        if tmp_arry[i][0] == "jmp":
            tmp_arry[i][0] = "nop"
        elif tmp_arry[i][0] == "nop":
            tmp_arry[i][0] = "jmp"

        result = run_ins(tmp_arry, "b")
        if not result:
            continue
        else:
            return result


def main():
    input = open('./eight/input.txt').read().splitlines()
    instructions = []
    for f in input:
        #f = f.replace("\n", "")
        f = f.split()
        instructions.append([f[0],f[1]])

    answer_a = run_ins(instructions)

    print("8a. Answer is %s" % answer_a)

    answer_b = repair(instructions, input)

    print("8b. Answer is %s" % answer_b)