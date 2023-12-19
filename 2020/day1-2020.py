# Part 1
inputs = []
for line in open("day1-2020.txt", "r"):
    inputs.append(int(line.strip("\n")))

answer = 0

for i in range(len(inputs) - 1):
    for j in range(1, len(inputs)):
        if inputs[i] + inputs[j] == 2020:
            answer = inputs[i] * inputs[j]

print("Part 1 Answer: " + str(answer))

# Part 2
inputs = []
for line in open("day1-2020.txt", "r"):
    inputs.append(int(line.strip("\n")))

answer = 0

for i in range(len(inputs) - 2):
    for j in range(1, len(inputs) - 1):
        for k in range(2, len(inputs)):
            if inputs[i] + inputs[j] + inputs[k] == 2020:
                answer = inputs[i] * inputs[j] * inputs[k]

print("Part 2 Answer: " + str(answer))
