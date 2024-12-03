def isSafe(report):
    if report[0] > report[1]:
        for x in range(len(report) - 1):
            difference = report[x] - report[x+1];
            if difference > 3 or difference < 1:
                return False;
    else:
        for x in range(len(report) - 1):
            difference = report[x+1] - report[x];
            if difference > 3 or difference < 1:
                return False;
    return True;

totalSafeReports = 0;
with open('reports.txt', 'r') as file:
    for line in file:
        report = [int(i) for i in line.split()];
        if isSafe(report):
           totalSafeReports += 1;

print(totalSafeReports);