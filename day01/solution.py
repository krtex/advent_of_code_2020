def read_input_into_set(name):
    return set(map( int, set(line.strip() for line in open(name))))

def find_complement(addend, sum, report):
    complement = sum - addend
    if complement in report:
        return complement
    return None

def find_sum_of_two(report):
    for entry in report:
        complement = find_complement(entry, 2020, report)
        if(complement):
            print(entry, "x", complement, "=", entry*complement)
            return
    print("Pair not found")
    return

if __name__ == "__main__":
    report = read_input_into_set("input.txt")
    find_sum_of_two(report)
