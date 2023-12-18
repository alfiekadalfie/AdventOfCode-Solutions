# Part 1 (repeat 40 times)
'''
input = [1, 1, 1, 3, 2, 2, 2, 1, 1, 3]
answer = []

# go through answer 39 times
for k in range(39):
    count = 0
    current = input[0]

    for i in range(len(input)):
        if input[i] == current:
            count += 1
        else:
            answer.append(count)
            answer.append(current)
            
            count = 1
            current = input[i]

    # account for last number
    answer.append(count)
    answer.append(current)

    input = answer
    answer = []

# one last time
count = 0
current = input[0]
for i in range(len(input)):
    if input[i] == current:
        count += 1
    else:
        answer.append(count)
        answer.append(current)
        
        count = 1
        current = input[i]

# account for last number
answer.append(count)
answer.append(current)

print(len(answer))
'''
# Part 2 (repeat 50 times)
input = [1, 1, 1, 3, 2, 2, 2, 1, 1, 3]
answer = []

# go through answer 39 times
for k in range(49):
    count = 0
    current = input[0]

    for i in range(len(input)):
        if input[i] == current:
            count += 1
        else:
            answer.append(count)
            answer.append(current)
            
            count = 1
            current = input[i]

    # account for last number
    answer.append(count)
    answer.append(current)

    input = answer
    answer = []

# one last time
count = 0
current = input[0]
for i in range(len(input)):
    if input[i] == current:
        count += 1
    else:
        answer.append(count)
        answer.append(current)
        
        count = 1
        current = input[i]

# account for last number
answer.append(count)
answer.append(current)

print(len(answer))
