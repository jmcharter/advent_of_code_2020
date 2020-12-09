with open("day_05/day_05.txt") as f:
    data = f.read().splitlines()

def binary_search(line, start, end, lo, hi, char1, char2,):
    target = 0
    for char in line[start:end]:
        if char in char1:
            hi -= (hi - lo) // 2 + 1
            target = lo
        elif char in char2:
            lo += (hi - lo) // 2 + 1
            target = hi
    return target

def find_seat():
    for line in data:
        row = binary_search(line, 0, 7, 0, 127, 'F', 'B')
        column = binary_search(line, 7, None, 0, 7, 'L','R')
        id = row * 8 + column
        yield id

max = 0
for i in find_seat():
    if i > max:
        max = i

print(max)
# Answer = 915

