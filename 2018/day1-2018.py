# Part 1

sum = 0

for line in open("day1-2018.txt", "r"):
    number = line.strip("\n")

    if number[0] == '+':
        sum += int(number[1:])
    
    elif number[0] == '-':
        sum -= int(number[1:])

print('Part 1: ' + str(sum))

# Part 2
seen = [0]

sum = 0

flag = True

while flag:
    for line in open("day1-2018.txt", "r"):
        number = line.strip("\n")

        if number[0] == '+':
            sum += int(number[1:])
        
        elif number[0] == '-':
            sum -= int(number[1:])
        
        # Take the first answer shown (right below Part 1's answer)
        if sum in seen:
            print("Part 2: " + str(sum))
            flag = False
    
        seen.append(sum)
