import re

def reverseString(string):
    return string[::-1]

def searchXmas(string):
    total = len(re.findall("XMAS", string))
    return total + len(re.findall("XMAS", reverseString(string)))

matrix = []
with open('wordSearch.txt', 'r') as file:
    for line in file:
        row = []
        matrix.append(row)
        for char in line[:-1]:
            row.append(char)

total = 0
rowCount = len(matrix)
colCount = len(matrix[1])

# Checking row
for row in matrix:
    total += searchXmas("".join(row))

# Checking column
for c in range(colCount):
    columnString = ""
    for r in range(rowCount):
        columnString += matrix[r][c]
    total += searchXmas(columnString)

def searchDiagonal(grid):
    count = 0
    # Checking diagonal / top half:
    for r in range(1, rowCount + 1):
        string = ""
        row = r - 1
        for c in range(r):
            string += grid[row][c]
            row -= 1
        count += searchXmas(string)

    # Checking diagonal / bottom half:
    for c in range(1, colCount - 1):
        string = ""
        row = rowCount - 1
        col = c
        for r in reversed(range(c, rowCount)):
            string += grid[row][col]
            row -= 1
            col += 1
        count += searchXmas(string)
    return count

total += searchDiagonal(matrix)
reverseMatrix = []
for row in matrix:
    reversedRow = []
    for c in reversed(row):
        reversedRow.append(c)
    reverseMatrix.append(reversedRow)

total += searchDiagonal(reverseMatrix)

print(total)