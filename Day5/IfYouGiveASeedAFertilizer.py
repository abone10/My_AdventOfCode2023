import re
p1 = re.compile(r'[\D+\-]*:[\n\s]')

file = open("Day5\IfYouGiveASeedAFertilizerInput.txt", "r")
data = file.readlines()
file.close()

data = "".join(data)
data = p1.split(data)

print(' check 1')
for i, line in enumerate(data):
    data[i] = re.split(r'\n', line)
    for j, set in enumerate(data[i]):
        data[i][j] = re.split(r'\s',set)


semi = data[1][0]
data.pop(0)
data.pop(0)
for i in range(len(semi)):
    semi[i] = int(semi[i])


for i in range(len(data)):
    print('check 1.5')
    for j in range(len(data[i])):
        for z in range(len(data[i][j])):
            data[i][j][z] = int(data[i][j][z])

print(' check 2')

for i, group in enumerate(data):
    print(' check 2')
    for set in group:
        print('check 3')
        for i in range(len(semi)):
            if(set[1]<semi[i]<set[1]+set[2]):
                semi[i]=set[0]+semi[i]-set[1]

print(min(semi))