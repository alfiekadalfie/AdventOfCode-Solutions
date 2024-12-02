# Part 1
total_distance = 0
left_list = []
right_list = []

for line in open("day1-2024.txt", "r"):
    numbers = line.strip("\n").split("   ")

    left_list.append(numbers[0])
    right_list.append(numbers[1])

while len(left_list) != 0:
    min_left_list, index_left_list = min(left_list), left_list.index(min(left_list))
    min_right_list, index_right_list = min(right_list), right_list.index(min(right_list))

    total_distance += (abs(int(min_left_list) - int(min_right_list)))

    left_list.pop(index_left_list)
    right_list.pop(index_right_list)

print("Total distance: " + str(total_distance))

# Part 2
# left_list and right_list are empty

score = 0

for line in open("day1-2024.txt", "r"):
    numbers = line.strip("\n").split("   ")

    left_list.append(int(numbers[0]))
    right_list.append(int(numbers[1]))

for number in left_list:
    score += (number * right_list.count(number))

print("Similarity Score: " + str(score))
