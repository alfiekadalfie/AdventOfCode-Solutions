# Part 1

count = 0

for line in open("day4-2017.txt", "r"):
    passphrase = line.strip("\n").split(" ")

    flag = True

    for i in range(len(passphrase)-1):
        for j in range(i+1, len(passphrase)):

            if passphrase[i] == passphrase[j]:
                flag = False
    
    if flag:
        count+=1

print('Part 1: ' + str(count))

# Part 2
count = 0

for line in open("day4-2017.txt", "r"):
    passphrase = line.strip("\n").split(" ")

    flag = True

    for i in range(len(passphrase)-1):
        for j in range(i+1, len(passphrase)):
            
            if ''.join(sorted(passphrase[i])) == ''.join(sorted(passphrase[j])):
                flag = False
    
    if flag:
        count+=1

print('Part 2: ' + str(count))