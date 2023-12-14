sum = 0         
game = 1    # Game number

# Part 1

# how many of each originally
red = 12
green = 13
blue = 14

passed = True

red_count = 0
green_count = 0
blue_count = 0

for line in open("day2input-2023.txt", 'r'):
    line = line.strip("\n").split(": ")[1].split("; ")

    for i in line:
        for j in i.split(", "):
            if(j.split(" ")[1][0] == 'r'):
                red_count = int(j.split(" ")[0])
            elif(j.split(" ")[1][0] == 'g'):
                green_count = int(j.split(" ")[0])
            elif(j.split(" ")[1][0] == 'b'):
                blue_count = int(j.split(" ")[0])

            if(red_count > red or green_count > green or blue_count > blue):
                passed = False
            
            # reset
            red_count = 0
            green_count = 0
            blue_count = 0

    if(passed):
        sum += game
    
    # reset/update
    passed = True
    game+=1

print("Part 1 Answer: " + str(sum))


# Part 2
for line in open("day2input-2023.txt", 'r'):
    line = line.strip("\n").split(": ")[1].split("; ")

    # how many of each color in each game?
    red_list = []
    green_list = []
    blue_list = []

    # add to respective list for each game
    for i in line:
        for j in i.split(", "):
            if(j.split(" ")[1][0] == 'r'):
                red_list.append(int(j.split(" ")[0]))
            elif(j.split(" ")[1][0] == 'g'):
                green_list.append(int(j.split(" ")[0]))
            elif(j.split(" ")[1][0] == 'b'):
                blue_list.append(int(j.split(" ")[0]))

    # power of largest number for RGB
    sum += max(red_list) * max(green_list) * max(blue_list)
    
    # reset
    red_list = []
    green_list = []
    blue_list = []

    # update
    game+=1

print("Part 2 Answer: " + str(sum))
