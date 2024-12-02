# Part 1
# helper functions
def monotonic(report):
    original_report = report

    # all increasing; sort list, lists should match and have no difference
    sorted_report = sorted(report)

    if original_report == sorted_report:
        return True
    
    # all decreasing; invert list, sort list, lists should match and have no difference
    original_reversed_report = list(reversed(report))
    
    sorted_reversed_report = sorted(reversed(report))

    if original_reversed_report == sorted_reversed_report:
        return True

    return False

def check_range(report):
    good_range = [1, 2, 3]

    i = 0

    while i < len(report) - 1:
        if abs(report[i] - report[i+1]) not in good_range:
            return False
        
        i+=1
    
    return True

safe_reports = 0

for line in open("day2-2024.txt", "r"):
    report = [int(number) for number in line.strip("\n").split(" ")]
    
    if monotonic(report) and check_range(report):
        safe_reports+=1

print("Safe reports (Part 1): " + str(safe_reports))

# Part 2
safe_reports = 0

for line in open("day2-2024.txt", "r"):
    report = [int(number) for number in line.strip("\n").split(" ")]

    if monotonic(report) and check_range(report):
        safe_reports+=1
    
    else:
        original_report = report
        
        # here, remove each number in report to see if it's safe
        for i in range(len(original_report)):
            report = original_report

            if i == 0:
                modified_report = report[i+1:]
            elif i == len(original_report) - 1:
                modified_report = report[:i]
            else:
                modified_report = report[:i] + report[i+1:]
            
            if monotonic(modified_report) and check_range(modified_report):
                safe_reports+=1
                break

print("Safe reports (Part 2): " + str(safe_reports))
