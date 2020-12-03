def read_input_into_set(name):
    return set(map( int, set(line.strip() for line in open(name))))

def find_sum(name):
    report = read_input_into_set(name)

    for entry in report:
        rest = 2020 - entry
        if rest in report:
            print(entry, "x", rest, "=", entry*rest)
            return
    print("Pair not found")
    return

if __name__ == "__main__":
    find_sum("input.txt")
