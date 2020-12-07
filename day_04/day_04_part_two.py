import re

with open("day_04/day_04.txt", "r") as f:
    data = f.read().replace("\n", " ").strip().split('  ')

# Validation functions for each category of input data
required = {
    'byr':lambda x: len(x) == 4 and 1920 <= int(x) <= 2002,
    'iyr':lambda x: len(x) == 4 and 2010 <= int(x) <= 2020,
    'eyr':lambda x: len(x) == 4 and 2020 <= int(x) <= 2030,
    'hgt':lambda x: re.match(r'^(1([5-8]\d|9[0-3])cm)|((59|6[0-9]|7[0-6])in)$', x),
    'hcl':lambda x: re.match(r'^#[0-9a-f]{6}$', x),
    'ecl':lambda x: re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', x),
    'pid':lambda x: re.match(r'^\d{9}$', x)
}


count = 0
for line in data:
    valid = True 

    # Split all input lines into a list of x:y format values.
    # Then split x and y to create a dictionary of key: x, value: y
    s = line.split(' ')
    passport = dict()
    for item in s:
        x, y = item.split(":")
        if x not in 'cid':
            passport.update({x:y})
    
    # Check that all required values are in the passport dictionary
    # and that all values pass the validation functions.
    for key in passport:
        if not required[key](passport[key]) or not all(key in passport for key in required):
            valid = False
    if valid:
        count+=1

print(count)
# Answer = 140