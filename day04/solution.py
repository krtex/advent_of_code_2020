def validate_passport(entry):
        if ('byr' in entry
                and 'iyr' in entry
                and 'eyr' in entry
                and 'hgt' in entry
                and 'hcl' in entry
                and 'ecl' in entry
                and 'pid' in entry):
            return True
        return False

def read_line(line):
    return dict(x.split(":") for x in line.split())
    

def read_passports(input):
    valid_passports = 0
    with open(input) as passports:
        passport = {}
        for line in passports:
            if line != '\n':
                passport.update(read_line(line))
            else:
                if validate_passport(passport):
                    valid_passports += 1
                passport.clear()
    return valid_passports

if __name__ == "__main__":
    print("Valid passports:", read_passports("test.txt"))
    print("Valid passports:", read_passports("input.txt"))
