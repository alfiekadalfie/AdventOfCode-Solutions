# Part 1
sum = 0

# HASH algorithm
def hash(input):
    current = 0

    for i in input:
        ascii = ord(i)
        current += ascii
        current = current * 17
        current = current % 256
    
    return current

for line in open("day15-2023.txt", "r"):
    text = line.strip("\n").split(",")

for j in text:
    sum += hash(j)

print("Part 1 Answer: " + str(sum))

# Part 2
# helper to add up all focusing power for each box
def focusing_power(box, number):
    sum = 0
    i = 0
    while i < len(box):
        element = box[i].split(" ")[1]

        sum += (number + 1) * (i+1) * int(element)

        i+=1
    
    return sum

box = 0      # hash
focal = ""
dict = {}   # storing elements in each box

for number in range(256):
    dict[number] = []


for line in open("day15-2023.txt", "r"):
    text = line.strip("\n").split(",")

for i in text:
    # -; remove from box's list if in the list
    if "-" in i:
        box = hash(i.split("-")[0])
        
        count = 0
        while count < len(dict[box]):
            if i.split("-")[0] in dict[box][count]:
                dict[box].pop(count)
            
            count += 1
    # =; update or append to box's list
    elif "=" in i:
        box = hash(i.split("=")[0])
        focal = i.split("=")[0] + " " + i.split("=")[1]
        
        count = 0
        passed = False

        while count < len(dict[box]):
            if i.split("=")[0] in dict[box][count]:
                passed = True
                dict[box][count] = focal
            
            count += 1
        
        if not passed:
            dict[box].append(focal)

total_focusing_power = 0
for i in dict:
    total_focusing_power += focusing_power(dict[i], i)

print("Part 2 Answer: " + str(total_focusing_power))
