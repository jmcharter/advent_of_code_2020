with open('day_06/input.txt','r') as f:
    data = f.read().replace('\n', " ").strip().split('  ')

group_answer_count = []
for groups in data:
    # Init list to hold valid answers (those that appear within each response for a given group)
    answers = []
    # Create a list of the individual responses within a group
    responses = groups.split(" ")
    for char in groups:
        # Iterate through each group and check if the relevant character is with all of them
        if all(char in item for item in responses) and char not in answers and char != " ":
            answers.append(char)
    group_answer_count.append(len(answers))
            
    
sum = 0
for i in group_answer_count:
    sum += i

print(sum)
# Answer = 3437