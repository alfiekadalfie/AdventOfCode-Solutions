sum = 0
count = 0   # number of winning numbers
winning_numbers = []

# Part 1
for line in open("day4-2023.txt", "r"):
    # take only winning numbers and given numbers
    line = line.strip("\n").split(": ")[1].split(" | ")

    # append each winning number
    for i in line[0].split(" "):
        if(i != ""):
            winning_numbers.append(i)
    # increment count for each winning number found in set
    for j in winning_numbers:
        if(j in line[1].split(" ")):
            count+=1
    # if there is at least one winning number, update sum by doubling for every match
    if(count > 0):
        sum += 2 ** (count - 1)
    
    # reset
    count = 0
    winning_numbers = []

print("Part 1 Answer: " + str(sum))

# Part 2
card = 0    # card number

original_cards = []

# Each has 1 original card
for k in range(216):
    original_cards.append(1)

for line in open("day4-2023.txt", "r"):
    # take only winning numbers and given numbers
    line = line.strip("\n").split(": ")[1].split(" | ")

    # append each winning number
    for i in line[0].split(" "):
        if(i != ""):
            winning_numbers.append(i)
    
    # increment count for each winning number found in set
    for j in winning_numbers:
        if(j in line[1].split(" ")):
            count+=1
    
    # update next 'count' cards
    for l in range(card+1, card+count+1):
        original_cards[l]+=original_cards[card]
    
    # reset/update
    card+=1
    count = 0
    winning_numbers = []

# add em all up
for m in original_cards:
    sum += m

print("Part 2 Answer: " + str(sum))
