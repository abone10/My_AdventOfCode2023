import re

file = open("Day3\GearRatiosInput.txt", "r")
data = file.readlines()
file.close()

def CalculateNumber(matrix, x, gearY):
    result =1
    numberqta = 0
    checked=[]

    for dx in range(-1, 2):
        for Match in re.finditer(r'\d+', matrix[x+dx]):
            Number = int(Match.group())
            NumberRange = range(Match.span()[0], Match.span()[1])
            for dy in range(-1,2):
                if gearY+dy in NumberRange and Number not in checked and (dx, dy) != (0, 0):
                    checked.append(Number)
                    result *= int(Number)
                    numberqta+=1
        checked.clear()

    if numberqta==2:
        return result
    return 0 

total = 0

for i,line in enumerate(data):
    for match in re.finditer(r'\*', line):
        total += CalculateNumber(data, i, match.span()[0])

print(total)