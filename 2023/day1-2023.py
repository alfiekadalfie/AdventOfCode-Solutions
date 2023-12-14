start = 0   # index of first number
end = 0     # index of last number
sum = 0     # sum of all 'first + last'

# Part 1
for line in open("day1input-2023.txt", 'r'):
    for i in line:
        if(i.isnumeric()):
           start = i
           break
    
    for j in line:
        if(j.isnumeric()):
            end = j
    
    sum += int(str(start) + str(end))

print("Part 1 Answer: " + str(sum))

# Part 2
# helper to find first 'number'
def findFirstNumber(line):
    i = 0
    while i < len(line):
        if(line[i].isnumeric()):
            recentIndex = i+1
            return line[i]
        else:
            if(line[i] == 'o'):
                if(line[i+1] == 'n' and line[i+2] == 'e'):
                    recentIndex = i+3
                    return 1
                
            if(line[i] == 't'):
                if(line[i+1] == 'w' and line[i+2] == 'o'):
                    recentIndex = i+3
                    return 2
                
                elif(line[i+1] == 'h' and line[i+2] == 'r' and line[i+3] == 'e' and line[i+4] == 'e'):
                    recentIndex = i+5
                    return 3
            
            if(line[i] == 'f'):
                if(line[i+1] == 'o' and line[i+2] == 'u' and line[i+3] == 'r'):
                    recentIndex = i+4
                    return 4
                
                elif(line[i+1] == 'i' and line[i+2] == 'v' and line[i+3] == 'e'):
                    recentIndex = i+4
                    return 5
            
            if(line[i] == 's'):
                if(line[i+1] == 'i' and line[i+2] == 'x'):
                    recentIndex = i+3
                    return 6
                
                elif(line[i+1] == 'e' and line[i+2] == 'v' and line[i+3] == 'e' and line[i+4] == 'n'):
                    recentIndex = i+5
                    return 7
                
            if(line[i] == 'e'):
                if(line[i+1] == 'i' and line[i+2] == 'g' and line[i+3] == 'h' and line[i+4] == 't'):
                    recentIndex = i+5
                    return 8
            
            if(line[i] == 'n'):
                if(line[i+1] == 'i' and line[i+2] == 'n' and line[i+3] == 'e'):
                    recentIndex = i+4
                    return 9
        
        i+=1

# helper to find last 'number'
# index takes in recentIndex
def findLastNumber(line, index):
    i = index
    while i < len(line):
        if(line[i].isnumeric()):
            end = line[i]
        else:
            if(line[i] == 'o'):
                if(line[i+1] == 'n' and line[i+2] == 'e'):
                    end = 1
                
            if(line[i] == 't'):
                if(line[i+1] == 'w' and line[i+2] == 'o'):
                    end = 2
                
                elif(line[i+1] == 'h' and line[i+2] == 'r' and line[i+3] == 'e' and line[i+4] == 'e'):
                    end = 3
            
            if(line[i] == 'f'):
                if(line[i+1] == 'o' and line[i+2] == 'u' and line[i+3] == 'r'):
                    end = 4
                
                elif(line[i+1] == 'i' and line[i+2] == 'v' and line[i+3] == 'e'):
                    end = 5
            
            if(line[i] == 's'):
                if(line[i+1] == 'i' and line[i+2] == 'x'):
                    end = 6
                
                elif(line[i+1] == 'e' and line[i+2] == 'v' and line[i+3] == 'e' and line[i+4] == 'n'):
                    end = 7
                
            if(line[i] == 'e'):
                if(line[i+1] == 'i' and line[i+2] == 'g' and line[i+3] == 'h' and line[i+4] == 't'):
                    end = 8
            
            if(line[i] == 'n'):
                if(line[i+1] == 'i' and line[i+2] == 'n' and line[i+3] == 'e'):
                    end = 9

        i+=1
    
    return end

# index following the first 'number'
recentIndex = 0

for line in open("day1input-2023.txt", 'r'):
    start = str(findFirstNumber(line))
    end = str(findLastNumber(line, recentIndex))

    sum += int(start + end)

print("Part 2 Answer: " + str(sum))
