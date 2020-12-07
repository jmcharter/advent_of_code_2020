required = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid'
]

with open("day_04/day_04.txt", "r") as f:
    data = f.read().strip().split('\n\n')

count = 0
for entry in data:
    valid = True
    for item in required:
        if not item in entry:
            valid = False
    if valid == True:
        count+=1

print(count)
# Answer = 222