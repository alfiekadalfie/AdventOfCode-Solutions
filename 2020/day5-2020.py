# Part 1
seatID = [] # max of this list is answer
inputs = []

for line in open("day5-2020.txt", "r"):
    inputs.append(line.strip("\n"))

for i in inputs:
    row = [0, 127]
    col = [0, 7]

    row_answer = 0
    col_answer = 0

    # binary search for row
    for j in range(6):
        if i[j] == "F":
            row[1] = row[0] + ((row[1] - row[0]) // 2)
        elif i[j] == "B":
            row[0] = row[1] - ((row[1] - row[0]) // 2)
    
    if i[6] == "F":
        row_answer = row[0]
    elif i[6] == "B":
        row_answer = row[1]
    
    # binary search for col
    for j in range(7, 9):
        if i[j] == "L":
            col[1] = col[0] + ((col[1] - col[0]) // 2)
        elif i[j] == "R":
            col[0] = col[1] - ((col[1] - col[0]) // 2)
    
    if i[9] == "L":
        col_answer = col[0]
    elif i[9] == "R":
        col_answer = col[1]

    seatID.append(row_answer * 8 + col_answer)

print("Part 1 Answer: " + str(max(seatID)))

# Part 2
absent_seatID = []
for i in range(max(seatID)+1):
    if i not in seatID:
        absent_seatID.append(i)

# when printed, this answer has no seatID +1 or -1 from it
print("Part 2 Answer: " + str(absent_seatID[len(absent_seatID) - 1]))
