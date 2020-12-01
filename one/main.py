def part_a(numbers):
    for first_num in numbers:
        for second_num in numbers:
            total = first_num + second_num
            if total == 2020:
                print("We've a match, the numbers are %s + %s" % (first_num, second_num))
                print("So the answer is %s" % (first_num*second_num))
                return


def part_b(numbers):
    for first_num in numbers:
        for second_num in numbers:
            for third_num in numbers:
                total = first_num + second_num + third_num
                if total == 2020:
                    print("We've a match, the numbers are %s + %s + %s" % (first_num, second_num, third_num))
                    print("So the answer is %s" % (first_num*second_num*third_num))
                    return


def main():

    file = open("./one/report.csv", "r")
    expense_report = [int(i) for i in file]

    part_a(expense_report)
    part_b(expense_report)
