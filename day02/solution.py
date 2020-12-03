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

    def is_new_password_correct(self):
        result = False
        if self.password[self.lower-1] == self.letter:
            result = not result
        if self.password[self.upper-1] == self.letter:
            result = not result
        return result

def parse_line(line):
    found = re.search('(\d+)-(\d+) ([a-z]): ([a-z]+)', line)
    result = Entry(int(found.group(1)), int(found.group(2)), found.group(3), found.group(4))
    return result.is_password_correct(), result.is_new_password_correct()

if __name__ == "__main__":
    old_pwds = 0
    new_pwds = 0
    with open("input.txt") as input:
        lines = input.readlines()
        for line in lines:
            old_pwd_policy, new_pwd_policy = parse_line(line)
            if old_pwd_policy:
                old_pwds += 1
            if new_pwd_policy:
                new_pwds += 1

    print("Correct passwords:", old_pwds, new_pwds)

