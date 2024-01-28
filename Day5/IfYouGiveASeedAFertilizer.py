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

print(' check 2')

mappe = []
for i, group in enumerate(data):
    mappe.append({})
    print(' check 2')
    for set in group:
        print('check 3')
        for n in range(int(set[2])):
            mappe[i][str(int(int(set[1]))+n)] = str(int(set[0])+n)

print('check 3')
print(mappe[0])
result = 9999999999999999
for i, seme in enumerate(semi):
    location=semi[i]
    for mappa in mappe:
        lista = mappa.keys()
        if location in lista:
            location = mappa[location]


    if int(location) < result:
        result = int(location)



print(result)