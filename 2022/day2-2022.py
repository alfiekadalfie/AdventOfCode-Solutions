def winner(x, y):
    if x == "A" and y == "X":
        return 3
    elif x == "A" and y == "Y":
        return 6
    elif x == "A" and y == "Z":
        return 0
    elif x == "B" and y == "Y":
        return 3
    elif x == "B" and y == "X":
        return 0
    elif x == "B" and y == "Z":
        return 6
    elif x == "C" and y == "Z":
        return 3
    elif x == "C" and y == "Y":
        return 0
    elif x == "C" and y == "X":
        return 6
# Part 1
used = {"X":1, "Y":2, "Z":3}

sum = 0

for line in open("day2-2022.txt", "r"):
    line = line.strip("\n").split(" ")

    sum += (winner(line[0], line[1]) + used[line[1]])

print("Part 1 Answer: " + str(sum))

# Part 2
sum = 0

for line in open("day2-2022.txt", "r"):
    line = line.strip("\n").split(" ")

    if(line[1] == "Y"):     # need to draw
        if(line[0] == "A"):
            sum += 4    
        elif(line[0] == "B"):
            sum += 5
        elif(line[0] == "C"):
            sum += 6
    elif(line[1] == "X"):   # need to lose
        if(line[0] == "A"):
            sum += 3    
        elif(line[0] == "B"):
            sum += 1
        elif(line[0] == "C"):
            sum += 2
    elif(line[1] == "Z"):   # need to win
        if(line[0] == "A"):
            sum += 8    
        elif(line[0] == "B"):
            sum += 9
        elif(line[0] == "C"):
            sum += 7

print("Part 2 Answer: " + str(sum))
