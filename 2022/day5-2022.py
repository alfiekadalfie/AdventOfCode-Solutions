# Part 1
stack = [["Q", "S", "W", "C", "Z", "V", "F" ,"T"], ["Q", "R", "B"], ["B", "Z", "T", "Q", "P", "M", "S"], ["D", "V", "F", "R", "Q", "H"], ["J", "G", "L", "D", "B", "S", "T", "P"], ["W", "R", "T", "Z"], ["H", "Q", "M", "N", "S", "F", "R", "J"], ["R", "N", "F", "H", "W"], ["J", "Z", "T", "Q", "P", "R", "B"]]    # 9 stacks

def move(boxes, start, end):
    count = 0
    while count < boxes:
        popped = stack[start].pop()

        stack[end].append(popped)

        count += 1

for line in open("day5-2022.txt", "r"):
    line = line.strip("\n")

    if line[0:4] == "move":
        line = line.split(" ")

        move(int(line[1]), int(line[3]) - 1, int(line[5]) - 1)

print("Part 1 Answer: ")
for i in range(len(stack)):
    print(stack[i][len(stack[i]) - 1])

# Part 2
stack = [["Q", "S", "W", "C", "Z", "V", "F" ,"T"], ["Q", "R", "B"], ["B", "Z", "T", "Q", "P", "M", "S"], ["D", "V", "F", "R", "Q", "H"], ["J", "G", "L", "D", "B", "S", "T", "P"], ["W", "R", "T", "Z"], ["H", "Q", "M", "N", "S", "F", "R", "J"], ["R", "N", "F", "H", "W"], ["J", "Z", "T", "Q", "P", "R", "B"]]    # 9 stacks

def move_at_once(boxes, start, end):
    count = 0
    pick = []
    while count < boxes:
        pick.append(stack[start].pop())
        
        count += 1
    
    k = len(pick)
    while k > 0:
        stack[end].append(pick.pop())

        k-=1

for line in open("day5-2022.txt", "r"):
    line = line.strip("\n")

    if line[0:4] == "move":
        line = line.split(" ")

        move_at_once(int(line[1]), int(line[3]) - 1, int(line[5]) - 1)

print("\nPart 2 Answer: ")
for i in range(len(stack)):
    print(stack[i][len(stack[i]) - 1])
