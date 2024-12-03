import re

matches = []
with open('instructions.txt', 'r') as file:
    for line in file:
        matches.extend(re.findall("mul\(\d?\d?\d?,\d?\d?\d?\)", line));

total = 0;
for instruction in matches:
    values = re.findall("\d?\d?\d?", instruction)
    total += int(values[4]) * int(values[6])

print(total)