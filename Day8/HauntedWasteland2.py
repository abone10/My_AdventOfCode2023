import re
import math
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
print(directions)

nodesDictionary = {}
nodes = re.findall(r'(\w{3}) = \((\w{3}), (\w{3})\)', data)
for node in nodes:
    node, left, right = node
    nodesDictionary[node] = (left, right)
startingNodes = [node for node in nodesDictionary if node[2] == 'A']

iterations = []
directionsLength = len(directions)
for node in startingNodes:
    step = 0
    while True:
        LorR = directions[step%directionsLength]
        node = nodesDictionary[node][LorR]
        step += 1
        if node[2] == 'Z':
            iterations.append(step)
            break

result = math.lcm(*iterations)

print(result)
