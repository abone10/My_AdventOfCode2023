import re

file = open("Day6\WaitForItInput.txt", "r")
data = file.readlines()
file.close()
times = re.findall(r'\d+', data[0])
records = re.findall(r'\d+', data[1])


result = 1

for i in range(len(times)):
    times[i] = int(times[i])
    records[i] = int(records[i])

    nOfWays = 0
    for pressTime in range(1,times[i]):
        distance = pressTime*(times[i]-pressTime)
        if (distance > records[i]):
            nOfWays = nOfWays + 1
    result *= nOfWays

print(result)