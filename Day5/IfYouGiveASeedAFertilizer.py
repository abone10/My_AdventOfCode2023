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


semi = data[1][0]
data.pop(0)
data.pop(0)
for i in range(len(semi)):
    semi[i] = int(semi[i])


data[-1].pop(-1)
for i in range(len(data)):
    for j in range(len(data[i])):
        for z in range(len(data[i][j])):
            data[i][j][z] = int(data[i][j][z])


for group in data:
    for set in group:
        for i in range(len(semi)):
            if(set[1]<semi[i]<set[1]+set[2]):
                semi[i]=set[0]+semi[i]-set[1]

print(min(semi))
