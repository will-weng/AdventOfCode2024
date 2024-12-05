rules = []
listOfPages = []
readingRules = True
with open('input.txt', 'r') as file:
    for line in file:
        if line[:-1] == '':
            readingRules = False;
        elif(readingRules):
            rules.append(line[:-1].split("|"))
        else:
            listOfPages.append(line[:-1].split(","))

def checkOrdering(pages):
    for iPage, xPage in enumerate(pages[:-1]):
        for yPage in pages[iPage + 1:]:
            if [yPage, xPage] in rules:
                return False
    return True;

total = 0
for pages in listOfPages:
    if checkOrdering(pages):
        middle = (len(pages) - 1)/2
        total += int(pages[int(middle)])

print(total)