import re

def count_answers_in_group(group):
    return len(set(group.replace('\n', '')))

def read_input(input):
    with open(input) as file:
        groups = re.split('\r\n\r\n|\n\n', file.read())
        return [count_answers_in_group(group) for group in groups]


if __name__ == "__main__":
    print("Sum of all answers", sum(read_input("input.txt")))
