def count_unique(groups):
    sum = 0
    for group in groups:
        sum += len(set(group))
    return sum


def count_intersections(groups):
    total_groups = 0
    for group in groups:
        count_people = group.count('\n')

        if count_people == 0:
            total_groups += len(set(group))
        else:
            total_groups += len(set.intersection(*[set(person) for person in group.split()]))

    return total_groups


def main():
    input = open("./daysix/input.txt", "r")
    groups = input.read().split("\n\n")
    groups_no_returns = (s.replace("\n", "") for s in groups)

    answer_a = count_unique(groups_no_returns)

    print("3a. Answer is %s" % answer_a)

    answer_b = count_intersections(groups)
    print("3b. Answer is %s" % answer_b)
