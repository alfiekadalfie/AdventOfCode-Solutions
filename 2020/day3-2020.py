# Part 1
trees = 0

inputs = []

for line in open("day3-2020.txt", "r"):
    inputs.append(line.strip("\n"))

row = 0
col = 0

right = 3
down = 1

while row < len(inputs) - 1:
    if inputs[row+down][(col+right) % len(inputs[0])] == "#":
        trees += 1
    
    row += down
    col = (col+right) % len(inputs[0])

print("Part 1 Answer: " + str(trees))

# Part 2
total = 1
answers = [0, trees, 0, 0, 0]

# right 1, down 1
trees = 0

row = 0
col = 0

right = 1
down = 1

while row < len(inputs) - 1:
    if inputs[row+down][(col+right) % len(inputs[0])] == "#":
        trees += 1
    
    row += down
    col = (col+right) % len(inputs[0])

answers[0] = trees

# right 5, down 1
trees = 0

row = 0
col = 0

right = 5
down = 1

while row < len(inputs) - 1:
    if inputs[row+down][(col+right) % len(inputs[0])] == "#":
        trees += 1
    
    row += down
    col = (col+right) % len(inputs[0])

answers[2] = trees

# right 7, down 1
trees = 0

row = 0
col = 0

right = 7
down = 1

while row < len(inputs) - 1:
    if inputs[row+down][(col+right) % len(inputs[0])] == "#":
        trees += 1
    
    row += down
    col = (col+right) % len(inputs[0])

answers[3] = trees

# right 1, down 2
trees = 0

row = 0
col = 0

right = 1
down = 2

while row < len(inputs) - 1:
    if inputs[row+down][(col+right) % len(inputs[0])] == "#":
        trees += 1
    
    row += down
    col = (col+right) % len(inputs[0])

answers[4] = trees

# calculating total
for i in answers:
    total *= i

#print(answers)
print("Part 2 Answer: " + str(total))
