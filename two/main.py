import re

def part_a(file):
    valid_passwords = 0
    for row in file:
        matches = re.match("(\d\d?)-(\d\d?) (.): (.*)", row)

        lower = int(matches[1])
        upper = int(matches[2])
        character = matches[3]
        password = matches[4]

        count = password.count(character)

        if (count >= lower) and (count <= upper):
            valid_passwords += 1
    return valid_passwords


def part_b(file):
    valid_passwords = 0
    for row in file:
        matches = re.match("(\d\d?)-(\d\d?) (.): (.*)", row)

        lower = int(matches[1])
        upper = int(matches[2])
        character = matches[3]
        password = str(matches[4])

        # We don't use index zero
        lower -= 1
        upper -= 1

        try:
            lower_char = password[lower]
        except IndexError:
            continue

        try:
            upper_char = password[upper]
        except IndexError:
            continue

        if (lower_char == character) and (upper_char != character):
            valid_passwords += 1
        elif (lower_char != character) and (upper_char == character):
            valid_passwords += 1
    return valid_passwords

def main():

    file = open("./two/passwords.txt", "r")

    valid_passwords = part_a(file)
    print("2a. Answer is %s" % valid_passwords)

    valid_passwords = part_b(file)
    print("2b. Answer is %s" % valid_passwords)