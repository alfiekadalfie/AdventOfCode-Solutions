# Part 1

twos = 0
threes = 0

for line in open("day2-2018.txt", "r"):
    word = line.strip("\n")

    count = {}

    for letter in word:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1
    
    if 2 in count.values():
        twos+=1
    
    if 3 in count.values():
        threes+=1

print("Part 1: " + str(twos * threes))

# Part 2
def check_match(first, second):
    mismatch = 0
    matching = []

    for i in range(len(first)):
        if first[i] != second[i]:
            mismatch+=1
        else:
            matching.append(first[i])
        
        if mismatch > 1:
            return False
    
    if mismatch == 1:
        return (True, matching)

words = []

for line in open("day2-2018.txt", "r"):
    words.append(line.strip("\n"))

for i in range(len(words) - 1):
    for j in range(i+1, len(words)):

        if check_match(words[i], words[j]):
            print('Part 2: ' + ''.join(check_match(words[i], words[j])[1]))