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
                return [pages.index(xPage), pages.index(yPage)]
    return True;

def fixOrdering(pages, ordering):
    while ordering != True:
        pages[ordering[0]], pages[ordering[1]] = pages[ordering[1]], pages[ordering[0]]
        ordering = checkOrdering(pages)

total = 0
for pages in listOfPages:
    ordering = checkOrdering(pages)
    if ordering != True:
        fixOrdering(pages, ordering)
        middle = (len(pages) - 1)/2
        total += int(pages[int(middle)])

print(total)