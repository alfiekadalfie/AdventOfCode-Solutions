sums = []
inputs = []

for line in open("day7-2021.txt", "r"):
    line = line.strip("\n").split(",")

    for i in line:
        inputs.append(int(i))

inputs.sort()

i = 0
while i < len(inputs):
    target = inputs[i]

    sum = 0

    for j in inputs:
        sum += abs(j - target)
    
    sums.append(sum)

    i+=1

print("Part 1 Answer: " + str(min(sums)))

# Part 2
sums = []

i = 0
while i < len(inputs):
    target = inputs[i]

    sum = 0

    for j in inputs:
        diff =  abs(j - target)

        for k in range(1, diff+1):
            sum += k
    
    sums.append(sum)

    i+=1

print("Part 2 Answer: " + str(min(sums)))
