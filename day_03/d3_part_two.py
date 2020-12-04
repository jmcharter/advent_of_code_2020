import math

with open("day_03/day_03.txt") as f:
    data = [line.strip() for line in f.readlines()]

gradients = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2),
]

def count_trees(gradient):

    tree_count = 0
    x = 0
    width = len(data[0])
    delta_x, delta_y = gradient

    for y in range(0, len(data), delta_y):
        if '#' in data[y][x % width]:
            tree_count +=1
        x += delta_x
    return tree_count

total_trees = []

for i in gradients:
    total_trees.append(count_trees(i))

print(math.prod(total_trees))

# Answer is: 6419669520