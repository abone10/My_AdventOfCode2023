import re

l = ["a",
     ".",
     "5",
     '+']
n = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     []]

p = re.compile(r'(?!\d|\. )')
print(p.match(l[3]))


l2 = []
for s in l:
    l2.append([*s])


def neighbours(matrix, x, y):
    rangeX=range(0, len(matrix))
    rangeY=range(0, len(matrix[0]))
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            (adjX, adjY) = (x+dx, y+dy)
            if adjX in rangeX and adjY in rangeY and (dx, dy) != (0, 0) and matrix[adjX][adjY]=="*":
                return True
    return False


#print(neighbours(l2,0,1))

