with open("day_03/day_03.txt") as f:
    data = [line.strip() for line in f.readlines()]

tree_count = 0
x = 0
y = 0

for i in data:
    if '#' in i[x % len(data[0])]:
        tree_count +=1
    x += 3

print(tree_count)

# Answer to part 1: 159