from collections import Counter


def stage_one(numbers):
    socket = 0
    inbuilt = max(numbers) + 3

    counter = Counter(numbers)

    numbers.append(0)
    numbers.sort()
    # built in device rate
    numbers.append(numbers[-1] + 3)

    differences = {}
    for a, b in zip(numbers[1:], numbers[:-1]):
        if a - b not in differences:
            differences[a - b] = 1
        else:
            differences[a - b] += 1

    print("Differences :", differences)
    print(f"Result is {differences[1] * differences[3]}")


def stage_two(numbers):
    c = Counter({0: 1})
    for x in numbers:
        c[x + 1] += c[x]
        c[x + 2] += c[x]
        c[x + 3] += c[x]
    print("Part 2:", c[max(numbers) + 3])

def main():

    with open('./ten/input.txt', 'r') as file_:
        numbers = list(map(int, file_.read().split()))

    stage_one(numbers)

    stage_two(numbers)