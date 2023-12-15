count = 0   # did it beat record?

# Part 1
time = [62, 73, 75, 65]
distance = [644, 1023, 1240, 1023]
total = 1   # multiply number of ways of beating record for all four

i = 0
while(i < len(time)):
    for j in range(time[i]):
        hold = j
        remaining = time[i] - hold
        
        travel = hold * remaining

        if(travel > distance[i]):
            count+=1
    # update
    total *= count
    # reset
    count = 0

    i+=1 

print("Part 1 Answer: " + str(total))

# Part 2 (same logic as Part 1, but without outer loop and total)
time = 62737565
distance = 644102312401023

for k in range(time):
    hold = k
    remaining = time - hold

    travel = hold * remaining

    if(travel > distance):
        count+=1

print("Part 2 Answer: " + str(count))
