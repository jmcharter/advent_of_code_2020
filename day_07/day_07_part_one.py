import re

with open('day_07/input.txt','r') as f:
    data = f.read().strip().split('\n')

outer_bag_re = r'^\w+\s\w+'
inner_bag_re = r'(?<=\d\s)\w+\s\w+'

bag_dict = dict()
for line in data:
    outer_bag = re.findall(outer_bag_re,line)[0]
    inner_bags = re.findall(inner_bag_re, line)
    bag_dict.update({outer_bag:inner_bags})

def check_bag(colour):
    if colour == 'shiny gold':
        return True
    else:
        return any(check_bag(i) for i in bag_dict[colour])

# Count starts negative one to account for the fact that a shiny gold bag does not contain itself
# but will be found with the check_bag function
count = -1
for i in bag_dict.keys():
    if check_bag(i):
        count += 1

print(count)
# Answer = 278