# Part 1
victims = []
inputs = []
passed = []

for line in open("day9-2020.txt", "r"):
    inputs.append(int(line.strip("\n")))

# first 25
for i in range(25):
    victims.append(inputs[i])

for i in range(25, len(inputs)):
    victims.append(inputs[i])

    number = inputs[i]

    for j in range(len(victims)-1):
        for k in range(j+1, len(victims)):
            if victims[j] + victims[k] == number:
                passed.append(number)
    
    victims.pop(0)

# For Part 2
target = 0

for i in inputs[25:]:
    if i not in passed:
        target = i
        print("Part 1 Answer: " + str(i))

# Part 2
window = []

i = 0
while i < len(inputs):
    if sum(window) == target:
        break

    while sum(window) < target:
        window.append(inputs[i])
        i+=1

    while sum(window) > target:
        window.pop(0)

    
print("Part 2 Answer: " + str(min(window) + max(window)))
