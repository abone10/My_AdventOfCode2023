import re


file = open("Day3\GearRatiosInput.txt", "r")
data = file.readlines()
file.close()

def FindAsterix(matrix, x, ys):
    rangeX=range(0, len(matrix))
    rangeY=range(0, len(matrix[0]))

    startNumber = ys[0]
    EndNumber = ys[1]

    for y in range(startNumber, EndNumber):
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                
                (adjX, adjY) = (x+dx, y+dy)
                if adjX in rangeX and adjY in rangeY and (dx, dy) != (0, 0) and matrix[adjX][adjY] not in '\n.0123456789':
                    return True
    return False

total = 0

for i,line in enumerate(data):
    for match in re.finditer(r'\d+', line):
        if(FindAsterix(data, i, match.span())):
            total += int(match.group())

print(total)