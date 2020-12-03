import re

class Entry:
    def __init__(self, lower, upper, letter, password):
        self.lower = lower
        self.upper = upper
        self.letter = letter
        self.password = password

    def is_password_correct(self):
        occurrences = len([pos.start() for pos in re.finditer(self.letter, self.password)])
        if occurrences <= self.upper and occurrences >= self.lower:
            return True
        return False

def parse_line(line):
    found = re.search('(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
    result = Entry(int(found.group(1)), int(found.group(2)), found.group(3), found.group(4))
    return result.is_password_correct()

if __name__ == "__main__":
    correct_pwds = 0
    with open("input.txt") as input:
        lines = input.readlines()
        for line in lines:
            if parse_line(line):
                correct_pwds += 1

    print("Correct passwords:", correct_pwds)

