from math import prod

def load_lines(input):
    with open(input) as file:
        lines = file.readlines()
    lines = [l.strip() for l in lines]
    return lines

def count_trees(slope, right=3, down=1):
    tree_count = 0
    for idx, line in enumerate(slope):
        if not (idx % down):
            if line[(right * idx) % len(line)] == '#':
                tree_count += 1
    return tree_count

if __name__ == "__main__":
    slope = load_lines("input.txt")

    paths = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    grand_result = [count_trees(slope, *i) for i in paths]
    print("Trees on given slopes:", grand_result, "and their product:", prod(grand_result))

