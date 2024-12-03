def isAscend(report):
    iter = 0;
    if report[0] < report[1]: iter += 1;
    if report[0] < report[2]: iter += 1;
    if report[0] < report[3]: iter += 1;
    if iter >= 2:
        return True;
    return False;

def dampenReport(report):
    if not isAscend(report):
        for x in range(len(report) - 1):
            difference = report[x] - report[x+1];
            if difference > 3 or difference < 1:
                if isSafe(report[1:]):
                    return True;
                else:
                    report.pop(x+1);
                    return isSafe(report);
    else:
        for x in range(len(report) - 1):
            difference = report[x+1] - report[x];
            if difference > 3 or difference < 1:
                if isSafe(report[1:]):
                    return True;
                else:
                    report.pop(x+1);
                    return isSafe(report);
    return True;

def isSafe(report):
    if not isAscend(report):
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
        if dampenReport(report):
            totalSafeReports += 1;

print(totalSafeReports);