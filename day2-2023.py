sum = 0
game = 1
red = 12
green = 13
blue = 14
passed = True

red_count = 0
green_count = 0
blue_count = 0

red_list = []
green_list = []
blue_list = []

'''# Part 1
for line in open("day2input-2023.txt", 'r'):
    #print(line.strip("\n").split(":"))

    line = line.strip("\n").split(": ")

    line = line[1].split("; ") 

    #print(line)

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
            
            red_count = 0
            green_count = 0
            blue_count = 0

    if(passed):
        sum += game
        
    passed = True
    game+=1

print(sum)
'''

# Part 2
for line in open("day2input-2023.txt", 'r'):
    #print(line.strip("\n").split(":"))

    line = line.strip("\n").split(": ")

    line = line[1].split("; ") 

    #print(line)

    for i in line:
        for j in i.split(", "):
            if(j.split(" ")[1][0] == 'r'):
                red_list.append(int(j.split(" ")[0]))
            elif(j.split(" ")[1][0] == 'g'):
                green_list.append(int(j.split(" ")[0]))
            elif(j.split(" ")[1][0] == 'b'):
                blue_list.append(int(j.split(" ")[0]))

    sum += max(red_list) * max(green_list) * max(blue_list)
    
    red_list = []
    green_list = []
    blue_list = []
    game+=1

print(sum)