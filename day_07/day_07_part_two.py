import re

with open('day_07/input.txt','r') as f:
    data = f.read().strip().split('\n')

outer_bag_re = re.compile(r'^\w+\s\w+')
inner_bag_re = re.compile(r'(\d)(\s\w+\s\w+)')

bag_dict = dict()
for line in data:
    outer_bag = re.match(outer_bag_re,line)
    inner_bags = [re.match(inner_bag_re, line).group(1), re.match(inner_bag_re, line).group(2)]
    bag_dict.update({outer_bag:inner_bags})

def check_bag(colour):
    if colour == 'shiny gold':
        return True
    else:
        return any(check_bag(i) for i in bag_dict[colour])

# count = -1
# for i in bag_dict.keys():
#     if check_bag(i):
#         count += 1

# print(count)
print(bag_dict)