path = "LLRLLRLRLRRRLLRRRLRRLRLRLRLRLRLRRLRRRLRLLRRLRRLRRRLLRLLRRLLRRRLLLRLRRRLLLLRRRLLRRRLRRLRLLRLRLRRRLRRRLRRLRRLRRLRLLRRRLRRLRRRLLRRRLRLRRLLRRLLRLRLRRLRRLLRLLRRLRLLRRRLLRRRLRRLLRRLRRRLRLRRRLRRLLLRLLRLLRRRLRLRLRLRRLRRRLLLRRRLRRRLRRRLRRLRLRLRLRRRLRRLLRLRRRLRLRLRRLLLRRRR"
inputs = []
steps = 1 # how many steps does it take to get to ZZZ?

dict = {}   # keeps track of key either L or R

# Part 1 (keep this commented out to run Part 2)
'''
# splits 'key' from 'value'
for line in open("day8-2023.txt", "r"):
    inputs.append(line.strip("\n").split(" = "))

# splits 'L' or 'R' for each key
for i in inputs:
    i[1] = i[1].split(", ")

    dict[i[0]] = [i[1][0][1:], i[1][1][0:3]]

target = "ZZZ"
start = "AAA"

j = 0
while j < len(path):
    if(path[j] == "L"):
        start = dict[start][0]
    else:
        start = dict[start][1]
    
    if(start == target):
        break
    
    steps+=1

    j+=1

    # repeat set of instructions if not found yet
    if(j == len(path)):
        j = 0
    
print("Part 1 Answer: " + str(steps))
'''

# Part 2
# this takes a while (like a REALLY long time)
# splits 'key' from 'value'
for line in open("day8-2023.txt", "r"):
    inputs.append(line.strip("\n").split(" = "))

# splits 'L' or 'R' for each key
for i in inputs:
    i[1] = i[1].split(", ")

    dict[i[0]] = [i[1][0][1:], i[1][1][0:3]]

# key ends with A
start = []

for i in dict:
    if i[2] == "A":
        start.append(i)

j = 0
passed = []
for i in range(len(start)): # all in start ends with Z
    passed.append(False)

while j < len(path):
    if(path[j] == "L"):
        for i in start:
            i = dict[i][0]
    else:
        for i in start:
            i = dict[i][1]
    
    k = 0
    while k < len(start):
        if(start[k][2] == "Z"):
            passed[k] = True
        else:
            passed[k] = False
        
        k+=1
    
    steps+=1

    count = 0
    for z in passed:
        if z == True:
            count+=1
    
    if count == len(start):
        break

    j+=1

    print("Part 2 Answer: " + str(steps))

    # repeat set of instructions if not found yet
    if(j == len(path)):
        j = 0

print("Part 2 Answer: " + str(steps))
