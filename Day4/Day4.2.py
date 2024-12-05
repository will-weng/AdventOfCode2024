import re

# M.S
# .A.
# M.S
def isXmasH(matrix, row, col):
    if matrix[row - 1][col - 1] != "M":
        return False;
    if matrix[row - 1][col + 1] != "S":
        return False;
    if matrix[row + 1][col - 1] != "M":
        return False;
    if matrix[row + 1][col + 1] != "S":
        return False;
    return True;
# M.M
# .A.
# S.S
def isXmasV(matrix, row, col):
    if matrix[row - 1][col - 1] != "M":
        return False;
    if matrix[row - 1][col + 1] != "M":
        return False;
    if matrix[row + 1][col - 1] != "S":
        return False;
    if matrix[row + 1][col + 1] != "S":
        return False;
    return True;

def searchXmas(matrix):
    count = 0
    for irow, row in enumerate(matrix[1:-1]):
        for icol, col in enumerate(row[1:-1]):
            if col == 'A':
                if isXmasH(matrix, irow + 1, icol + 1):
                    matrix[irow + 1][icol + 1] = 'O'
                    count += 1
                elif isXmasV(matrix, irow + 1, icol + 1):
                    matrix[irow + 1][icol + 1] = 'O'
                    count += 1
    return count

def reverseMatrix(matrix):
    reversedMatrix = []
    for row in matrix:
        reversedRow = []
        for c in reversed(row):
            reversedRow.append(c)
        reversedMatrix.append(reversedRow)
    return reversedMatrix

def flipMatrix(matrix):
    flippedMatrix = []
    for row in reversed(matrix):
        flippedMatrix.append(row)
    return flippedMatrix

matrix = []
with open('wordSearch.txt', 'r') as file:
    for line in file:
        row = []
        matrix.append(row)
        for char in line[:-1]:
            row.append(char)

total = 0
total += searchXmas(matrix)
total += searchXmas(reverseMatrix(matrix))
total += searchXmas(flipMatrix(matrix))

print(total)