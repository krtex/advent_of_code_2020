def load_lines(input):
    with open(input) as file:
        lines = file.readlines()
    lines = [l.strip() for l in lines]
    return lines

def count_trees(slope):
    tree_count = 0
    for idx, line in enumerate(slope):
        print(line)
        if line[(3 * idx) % len(line)] == '#':
            print("TREE!")
            tree_count += 1
    return tree_count

if __name__ == "__main__":
    slope = load_lines("input.txt")
    result = count_trees(slope)

    print("There were", result, "trees on my way!")
