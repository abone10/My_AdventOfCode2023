import re

file = open("Day6\WaitForItInput.txt", "r")
data = file.readlines()
file.close()
time = ''.join(re.findall(r'\d+', data[0]))
record = ''.join(re.findall(r'\d+', data[1]))

time = int(time)
record = int(record)

result = 0
for pressTime in range(1,time):
    distance = pressTime*(time-pressTime)
    if (distance > record):
        result = result + 1
    elif(result>0):
        break

print(result)