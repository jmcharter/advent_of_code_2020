with open('day_06/input.txt','r') as f:
    data = f.read().replace('\n', " ").strip().split('  ')

# print(data)

group_sums = []
for groups in data:
    answers = []
    for answer in groups:
        if answer not in answers and answer not in " ":
            answers.append(answer)
    group_sums.append(len(answers))
    
sum = 0
for i in group_sums:
    sum += i

print(sum)
# Answer = 6630