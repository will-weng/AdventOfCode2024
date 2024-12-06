from enum import Enum

class Directions(str, Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    LEFT = 'LEFT'
    RIGHT = 'RIGHT'

class Guard:
    def __init__(self, x, y, direction):
        self.direction = direction
        self.x = x
        self.y = y

    def print(self):
        print(self.direction)
        print(self.x, self.y)

    def rotate(self):
        match self.direction:
            case Directions.UP:
                self.direction = Directions.RIGHT
            case Directions.RIGHT:
                self.direction = Directions.DOWN
            case Directions.DOWN:
                self.direction = Directions.LEFT
            case Directions.LEFT:
                self.direction = Directions.UP

    def move(self, matrix):
        match self.direction:
            case Directions.UP:
                if self.y == 0:
                    matrix[self.y][self.x] = 'X'
                    return False
                elif matrix[self.y - 1][self.x] == '#':
                    self.rotate()
                    return self.move(matrix)
                else:
                    matrix[self.y][self.x] = 'X'
                    self.y -= 1
            case Directions.RIGHT:
                if self.x == len(matrix[0]) - 1:
                    matrix[self.y][self.x] = 'X'
                    return False
                elif matrix[self.y][self.x + 1] == '#':
                    self.rotate()
                    return self.move(matrix)
                else:
                    matrix[self.y][self.x] = 'X'
                    self.x += 1
            case Directions.DOWN:
                if self.y == len(matrix) - 1:
                    matrix[self.y][self.x] = 'X'
                    return False
                elif matrix[self.y + 1][self.x] == '#':
                    self.rotate()
                    return self.move(matrix)
                else:
                    matrix[self.y][self.x] = 'X'
                    self.y += 1
            case Directions.LEFT:
                if self.x == 0:
                    matrix[self.y][self.x] = 'X'
                    return False
                elif matrix[self.y][self.x - 1] == '#':
                    self.rotate()
                    return self.move(matrix)
                else:
                    matrix[self.y][self.x] = 'X'
                    self.x -= 1
        return True

def printMatrix(matrix):
    for row in matrix:
        print(row)

def findStart(matrix):
    for row in matrix:
        if '^' in row or '>' in row or 'v' in row or '<' in row:
            for item in row:
                match item:
                    case '^':
                        return Guard(row.index('^'), matrix.index(row), Directions.UP)
                    case '>':
                        return Guard(row.index('>'), matrix.index(row), Directions.RIGHT)
                    case 'v':
                        return Guard(row.index('v'), matrix.index(row), Directions.DOWN)
                    case '<':
                        return Guard(row.index('<'), matrix.index(row), Directions.LEFT)

def findDistinctPositions(matrix):
    return sum(row.count('X') for row in matrix)

matrix = []
with open('input.txt', 'r') as file:
    for line in file:
        row = []
        matrix.append(row)
        for char in line[:-1]:
            row.append(char)

guard = findStart(matrix)
while guard.move(matrix):
    pass

guard.print()
# printMatrix(matrix)
print(findDistinctPositions(matrix))