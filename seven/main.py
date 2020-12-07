import re

def get_rules(rules):
    colours = dict()
    for rule in rules:
        rule = rule.replace("bags", "bag").replace("\n", "")
        colour = re.findall("(.*) bag contain", rule)
        contains = re.findall("(\d+) ([^\.,]+) bag?", rule)
        colours[colour[0]] = contains
    return colours


def get_count(rules, colour):
    rules_dict = get_rules(rules)

    colours = []
    total_bags = 0

    for rule in rules_dict:
        # Check for bags that directly contain our colours
        for _, name in rules_dict[rule]:

            # If Gold is in the bag add the overall bag name to the list
            if colour in name:
                total_bags += search_num(rules_dict, colour)

                colours.append(rule)
    # For each of our bags that directly contain our colour, look at what other bags come with it and see if they contain our colour
    for sub_colour in colours:
        for rule in rules_dict:
            for _, name in rules_dict[rule]:
                if sub_colour in name:
                    colours.append(rule)

    total_bags = search_num(rules_dict, "shiny gold") - 1

    return len(set(colours)), total_bags


def search_num(rules, colour):
    if not rules[colour]:
        return 1
    else:
        return sum([int(v)*search_num(rules, k) for v, k in rules[colour]]) + 1


def main():
    input = open("./seven/input.txt", "r")
    answer_a, answer_b = get_count(input, "shiny gold")
    print("7a. Answer is %s" % answer_a)
    print("7b. Answer is %s" % answer_b)