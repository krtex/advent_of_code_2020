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
            return complement
    print("Pair not found")
    return None

def find_sum_of_three(report):
    ugly_thing_to_do = list(report)

    for first in range(len(ugly_thing_to_do)):
        for second in range(first + 1, len(ugly_thing_to_do)):
            sum = ugly_thing_to_do[first] + ugly_thing_to_do[second]
            if(sum < 2020):
                third = find_complement(sum, 2020, report)
                if(third):
                    print(ugly_thing_to_do[first], "x", ugly_thing_to_do[second], "x", third, "=", ugly_thing_to_do[first] * ugly_thing_to_do[second] * third)
                    return


if __name__ == "__main__":
    report = read_input_into_set("input.txt")

    find_sum_of_two(report)
    find_sum_of_three(report)
