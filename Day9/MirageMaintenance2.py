import re

file = open("Day9\MirageMaintenanceInput.txt", "r")
data = file.readlines()
file.close()


reports = []
for line in data:
    reports.append([])
    reports[-1].append([int(n.group()) for n in re.finditer(r'-?\d+', line)])

print (reports)
def allZeros(array):
    for element in array:
        if element != 0:
            return False
    return True

differences = []
for i, report in enumerate(reports):
    while(allZeros(reports[i][-1]) == False):
        for j in range(len(report[-1])-1):
            differences.append(report[-1][j+1]-report[-1][j])
        copia=[]
        copia.extend(differences)
        reports[i].append(copia)
        differences.clear()


result = 0
for obj in reports:
    history = 0
    for obje in reversed(obj[:-1]):
        history = obje[0] - history
    result += history

print(result)