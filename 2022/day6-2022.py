# Part 1
characters = 4
string = ""
current_four = []

# take input string
for line in open("day6-2022.txt", "r"):
    string += line.strip("\n")

# take first four chars in input
for i in string[0:4]:
    current_four.append(i)

all_different = False

# until previous 4 are all different, pop LRU char, append next char
while not all_different:
    if current_four[0] not in current_four[1:] and current_four[1] not in current_four[2:] and current_four[2] not in current_four[3:]:
        all_different = True
    else:
        current_four.pop(0)
        current_four.append(string[characters])

        characters+=1

print("Part 1 Answer: " + str(characters))

# Part 2
characters = 14
string = ""
current_fourteen = []

# helper to check if all fourteen chars are different
def check_diff(list):
    diff = True
    for i in range(13):
        if list[i] in list[i+1:]:
            diff = False
            break
    
    return diff

# take input string
for line in open("day6-2022.txt", "r"):
    string += line.strip("\n")

# take first fourteen chars in input
for i in string[0:14]:
    current_fourteen.append(i)

all_different = False

# until previous 14 are all different, pop LRU char, append next char
while not all_different:
    if check_diff(current_fourteen):
        all_different = True
    else:
        current_fourteen.pop(0)
        current_fourteen.append(string[characters])

        characters+=1

print("Part 2 Answer: " + str(characters))
