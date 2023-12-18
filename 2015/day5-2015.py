# Part 1
nice = 0

def three_vowels(input):
    vowels = ['a', 'e', 'i', 'o', 'u']

    count = 0

    for i in input:
        if i in vowels:
            count+=1
    
    if count >= 3:
        return True

    return False

def twice_letter(input):
    i = 0
    while i < len(input) - 1:
        if input[i] == input[i+1]:
            return True
        i+=1
    
    return False

def bad_strings(input):
    bad = ['ab', 'cd', 'pq', 'xy']

    i = 0
    while i < len(input) - 1:
        if input[i:i+2] in bad:
            return False
        i+=1
    
    return True

for line in open("day5-2015.txt", "r"):
    line = line.strip("\n")

    if three_vowels(line) and twice_letter(line) and bad_strings(line):
        nice += 1

print("Part 1 Answer: " + str(nice))

# Part 2
nice = 0

def repeat_and_between(input):
    i = 0
    while i < len(input) - 2:
        if input[i] == input[i+2]:
            return True
        i+=1
    
    return False

def not_overlap(input):
    i = 0
    while i < len(input) - 1:
        if input[i:i+2] in input[i+2:]:
            return True
        i+=1
    
    return False

for line in open("day5-2015.txt", "r"):
    line = line.strip("\n")

    if not_overlap(line) and repeat_and_between(line):
        nice += 1

print("Part 2 Answer: " + str(nice))
