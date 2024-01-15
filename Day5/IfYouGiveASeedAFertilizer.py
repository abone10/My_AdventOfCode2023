import re
p1 = re.compile(r'[\D+\-]*:[\n\s]')

file = open("Day5\IfYouGiveASeedAFertilizerInput.txt", "r")
data = file.readlines()
file.close()

data = "".join(data)
data = p1.split(data)

for i, line in enumerate(data):
    data[i] = re.split(r'\n', line)

print(data)
data.pop(0)
print(data)
