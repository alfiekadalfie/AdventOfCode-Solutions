sum = 0
count = 0
winning_numbers = []

''' # Part 1
for line in open("day4-2023.txt", "r"):
    #print(line.strip("\n").split(": "))

    line = line.strip("\n").split(": ")[1].split(" | ")

    for i in line[0].split(" "):
        if(i is not ""):
            winning_numbers.append(i)
    #print(winning_numbers)
    
    for j in winning_numbers:
        if(j in line[1].split(" ")):
            count+=1
    print(count)
    
    if(count > 0):
        sum += 2 ** (count - 1)
    
    count = 0
    winning_numbers = []

print(sum)
'''

# Part 2
card = 0    # card number

original_cards = []

for k in range(216):
    original_cards.append(1)

for line in open("day4-2023.txt", "r"):
    line = line.strip("\n").split(": ")[1].split(" | ")

    for i in line[0].split(" "):
        if(i != ""):
            winning_numbers.append(i)
    #print(winning_numbers)
    
    for j in winning_numbers:
        if(j in line[1].split(" ")):
            count+=1
    #print(count, card)
    
    for l in range(card+1, card+count+1):
        original_cards[l]+=original_cards[card]
    
    card+=1
    count = 0
    winning_numbers = []

for m in original_cards:
    sum += m

print(original_cards)
print(sum)