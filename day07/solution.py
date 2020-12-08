from enum import IntEnum
import re


def parse_file(input):
    with open(input) as file:
        return file.readlines()

def build_table(lines):
    attribute = set()
    colour = set()
    for line in lines:
        found = re.search(r'^([a-z]+) ([a-z]+) [a-z 0-9,]*.$' , line)
        attribute.add(found.group(1))
        colour.add(found.group(2))

    attribute = IntEnum('attribute', sorted(attribute), start=0)
    colour = IntEnum('colour', sorted(colour), start=0)

    bags = []
    for i in range(len(attribute)):
        bags.append([])
        for j in range(len(colour)):
            bags[i].append([])

    return bags, attribute, colour

def parse_line(line):
    found = re.search(r'^([a-z]+) ([a-z]+) [a-z]+ [a-z]+ \d+ ([a-z]+) ([a-z]+) [a-z]+(, \d+ ([a-z]+) ([a-z]+) [a-z]+)*.', line)

    if found == None:
        found = re.search(r'^([a-z]+) ([a-z]+) [a-z]+ [a-z]+ [a-z]+', line)
        return (found.group(1), found.group(2)), []

    outer = (found.group(1), found.group(2))
    inners = [(found.group(3), found.group(4))]
    if found.group(5) != None:
        for i in range(6, len(found.groups()), 3):
            inners.append((found.group(i), found.group(i+1)))

    return outer, inners

def add_outer_bags(lines, bags, attribute, colour):
    for line in lines:
        outer, inners = parse_line(line)
        for inner in inners:
            bags[attribute[inner[0]]][colour[inner[1]]].append(outer)

def find_gold_containers(bagsi, attribute, colour):
    gold_containers = set()
    to_check = set(bags[attribute['shiny']][colour['gold']])

    while len(to_check) > 0:
        found = set()
        to_check = to_check.difference(gold_containers)
        for e in to_check:
            found.update(bags[attribute[e[0]]][colour[e[1]]])
        gold_containers.update(to_check)
        to_check = found

    return gold_containers

if __name__ == "__main__":
    lines = parse_file("input.txt")
    #lines = parse_file("test.txt")
    bags, attribute, colour = build_table(lines)
    add_outer_bags(lines, bags, attribute, colour)
    gold_containers = find_gold_containers(bags, attribute, colour)
    print(len(gold_containers))
