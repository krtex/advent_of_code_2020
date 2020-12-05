import re

def validate_byr(entry):
    return 1920 <= int(entry['byr']) <= 2002

def validate_iyr(entry):
    return 2010 <= int(entry['iyr']) <= 2020

def validate_eyr(entry):
    return 2020 <= int(entry['eyr']) <= 2030

def validate_hgt(entry):
    height = entry['hgt']
    if height[-2:] == 'cm':
        return 150 <= int(height[:-2]) <= 193
    if height[-2:] == 'in':
        return 59 <= int(height[:-2]) <= 76
    return False

def validate_hcl(entry):
    return re.match(r'^#[a-f0-9]{6}$', entry['hcl'])

def validate_ecl(entry):
    return entry['ecl'] in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

def validate_pid(entry):
    return re.match(r'\d{9}', entry['pid'])

def validate_passport(entry):
        if ('byr' in entry
                and 'iyr' in entry
                and 'eyr' in entry
                and 'hgt' in entry
                and 'hcl' in entry
                and 'ecl' in entry
                and 'pid' in entry):
            return validate_byr(entry) and validate_iyr(entry) \
                    and validate_eyr(entry) and validate_hgt(entry) \
                    and validate_hcl(entry) and validate_ecl(entry) \
                    and validate_pid(entry)
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
    print("Valid passports:", read_passports("input.txt"))
