import re

def multiply(instruction):
    values = re.findall("\d?\d?\d?", instruction)
    return int(values[4]) * int(values[6])

instructions = []
with open('instructions.txt', 'r') as file:
    for line in file:
        instructions.extend(re.findall("mul\(\d?\d?\d?,\d?\d?\d?\)|do\(\)|don\'t\(\)", line));

total = 0;
flag = True;
for instruction in instructions:
    if instruction == "don't()":
        flag = False;
    elif instruction == "do()":
        flag = True;
    else:
        if flag:
            total += multiply(instruction);
        else:
            next;

print(total)