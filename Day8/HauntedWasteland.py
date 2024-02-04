import re

file = open("Day8\HauntedWastelandInput.txt", "r")
data = file.readlines()
file.close()

directionString = data.pop(0)
data = ''.join(data)

directions = []
for ch in directionString:
    if ch == 'L':
        directions.append(0)
    if ch == 'R':
        directions.append(1)

nodesDictionary = {}
nodes = re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', data)
for node in nodes:
    node, left, right = node
    nodesDictionary[node] = (left, right)


step = 0
directionsLength = len(directions)
node = 'AAA'
while node != 'ZZZ':
    LorR = directions[step%directionsLength]
    node = nodesDictionary[node][LorR]
    step +=1

print(step)

#20093