from validation import validate_int
import re


def validate_passport(passports, part="a"):
    valid = 0
    valid_verified = 0
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    optional = ["cid"]

    for passport in passports:

        if validate_fields(required, optional, passport):
            if part == "a":
                valid += 1
            else:
                if validation(passport):
                    valid_verified += 1
    if part == "a":
        return valid
    else:
        return valid_verified


def validate_fields(required, optional, passport):
    for field in required:
        if field in passport:
            pass
        elif field in optional:
            pass
        else:
            return False
    return True


def validation(passport):
    try:
        # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        validate_int(int(passport["byr"]), min_value=1920, max_value=2002)

        # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        validate_int(int(passport["iyr"]), min_value=2010, max_value=2020)

        # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        validate_int(int(passport["eyr"]), min_value=2020, max_value=2030)

        # hgt (Height) - a number followed by either cm or in:
        height = passport["hgt"]
        if "cm" in height:
            # If cm, the number must be at least 150 and at most 193.
            height = height.replace("cm", "")
            validate_int(int(height), min_value=150, max_value=193)
        elif "in" in height:
            # If in, the number must be at least 59 and at most 76.
            height = height.replace("in", "")
            validate_int(int(height), min_value=59, max_value=76)
        else:
            return False

        # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        hcl = re.match("^#[0-9|a-f]{6}$", passport["hcl"])
        # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        ecl = re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport["ecl"])
        # pid (Passport ID) - a nine-digit number, including leading zeroes.
        pid = re.match("^[0-9]{9}$", passport["pid"])

        # cid (Country ID) - ignored, missing or not.

        if None in {hcl, ecl, pid}:
            return False
        return True
    except ValueError:
        return False


def create_key_values(passports):
    final_passports = []
    for passport in passports:
        # Get rid of new lines and keep it consistent with spaces
        passport = passport.replace('\n', ' ')

        # Use a space as a way to split each element of the object
        passport_object = passport.split(" ")

        # Split KVs by : into a dictionary
        pass_dict = dict(element.split(":") for element in passport_object)

        # Append each line in the loop to the final object
        final_passports.append(pass_dict)

    return final_passports


def main():
    input = open("./four/input.txt", "r")
    passports = input.read().split("\n\n")

    passport_kv = create_key_values(passports)

    total = validate_passport(passport_kv)

    print("4a. Answer is %s" % total)

    total = validate_passport(passport_kv, "b")
    print("4b. Answer is %s" % total)
