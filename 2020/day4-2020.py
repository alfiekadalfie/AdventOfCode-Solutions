# Part 1
valid = 0
inputs = []
# For Part 2
valid_passports = []
attribute = []

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

for line in open("day4-2020.txt", "r"):
    inputs.append(line.strip("\n"))

count = 0
current = ""

for i in inputs:
    if i != "":
        current = i.split(" ")
        
        for j in current:
            attribute.append(j)

            if j[0:3] in fields:
                count+=1
    else:
        if count == len(fields):
            valid += 1
        
        valid_passports.append(attribute)

        attribute = []

        count = 0

# check for last passport since there's no ""
valid_passports.append(attribute)

if count == len(fields):
    valid += 1
    
print("Part 1 Answer: " + str(valid))

# Part 2
valid = 0
count = 0 # needs to equal 7 for all requirements
# Check Part 1 valid_passports to check each field
for passport in valid_passports:
    for i in passport:
        i = i.split(":")

        if i[0] == "byr":
            if int(i[1]) >= 1920 and int(i[1]) <= 2002:
                count+=1
        
        if i[0] == "iyr":
            if int(i[1]) >= 2010 and int(i[1]) <= 2020:
                count+=1
        
        if i[0] == "eyr":
            if int(i[1]) >= 2020 and int(i[1]) <= 2030:
                count+=1
        
        if i[0] == "pid":
            if len(i[1]) == 9:
                count+=1
        
        if i[0] == "ecl":
            if i[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                count+=1
        
        if i[0] == "hcl":
            if i[1][0] == "#" and i[1][1:].isalnum():
                count+=1
        
        if i[0] == "hgt":
            number = ""

            for j in i[1]:
                if j.isnumeric():
                    number += j
                elif j == "i":
                    if int(number) >= 59 and int(number) <= 76:
                        count+=1
                elif j == "c":
                    if int(number) >= 150 and int(number) <= 193:
                        count+=1
    
    if count == len(fields):
        valid += 1
    
    count = 0

print("Part 2 Answer: " + str(valid))
