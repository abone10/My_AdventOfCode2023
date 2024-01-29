import re

p1 = re.compile(r'[\D+\-]*:[\n\s]')

file = open("Day5\IfYouGiveASeedAFertilizerInput.txt", "r")
data = file.readlines()
file.close()

data = "".join(data)
data = p1.split(data)
for i, line in enumerate(data):
    data[i] = re.split(r'\n', line)
    for j, set in enumerate(data[i]):
        data[i][j] = re.split(r'\s',set)


#separate seed line from maps
linea1= data[1][0]
data.pop(0)
data.pop(0)


#convert all strings to integers
semi = []
rangeSemi = []

for i in range(len(linea1)):
    linea1[i] = int(linea1[i])
    if (i%2):
        rangeSemi.append(linea1[i])
    else:
        semi.append(linea1[i])

for i in range(len(data)):
    for j in range(len(data[i])):
        for z in range(len(data[i][j])):
            data[i][j][z] = int(data[i][j][z])


#computetional part

intervalli = []
for i in range(len(semi)):
    intervalli.append((semi[i], semi[i] + rangeSemi[i], 0))


locations = []
while intervalli:
    print(intervalli)
    x1, x2, nPassaggi = intervalli.pop()

    if (nPassaggi == 7):
        locations.append(x1)
        continue

    for set in data[nPassaggi]:
        dest, start, delta = (set[0], set[1], set[2])
        end = start + delta -1
        diff = dest - start

        if (x1 > end or x2 < start):  #Non coincide tenta il prossimo set
            continue
        if(x1 < start):
            intervalli.append((x1, start-1, nPassaggi))
            x1=start
        if (x2 > end):
            intervalli.append((end+1, x2, nPassaggi))
            x2 = end
        intervalli.append((x1+diff, x2+diff, nPassaggi+1))
        break
    else:
        intervalli.append((x1, x2, nPassaggi+1))

print(min(locations))
