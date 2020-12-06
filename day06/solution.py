import re

def count_answers_in_group(group):
    return len(set(group.replace('\n', '')))

def check_common_part(group):
    answers = re.split('\n', group)
    answers = [set(a) for a in answers]
    print(set.intersection(*answers), len(set.intersection(*answers)))
    return len(set.intersection(*answers))

def read_input(input):
    with open(input) as file:
        return re.split('\r\n\r\n|\n\n', file.read())

def count_questions_anyone_answered(groups):
    return [count_answers_in_group(group) for group in groups]

def count_questions_everyone_answered(groups):
    return [check_common_part(group) for group in groups]

if __name__ == "__main__":
    groups = read_input("input.txt")
    print("Sum of all answers", sum(count_questions_anyone_answered(groups)))
    print("Sum of common answers", sum(count_questions_everyone_answered(groups)))
