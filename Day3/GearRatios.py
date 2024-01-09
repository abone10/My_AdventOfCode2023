import re


p = re.compile(r'(?!\d|\. )')

#Day 3

#Setup
file = open("Day3\GearRatiosInput.txt", "r")
input = file.readlines()
file.close()

data=[]
for s in input:
    data.append([*re.sub(r'\n', '', s)])

specials=[ '', '', '', '', '', '', '', '',
]
flag=0
number=0
sum=0


#Function wich return true if there's a neighbouring asterisk

def FindAsterix(matrix, x, y):
    rangeX=range(0, len(matrix))
    rangeY=range(0, len(matrix[0]))
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            (adjX, adjY) = (x+dx, y+dy)
            if adjX in rangeX and adjY in rangeY and (dx, dy) != (0, 0) and matrix[adjX][adjY]=="*":
                return True
    return False

#Main part

for i in range(len(data)):
    for j in range(len(data[i])):
        if re.match( r'\d', data[i][j]) and flag == 0:
            flag = 1

        if re.match( r'\d', data[i][j]):
            #If it's the first number of a sequesce we set the flag to 1 to distinguish it
            number = number*10 + int(data[i][j])
            if FindAsterix(data, i, j): flag=2 #If there's an asterisk near we set the flag to 2
        else:
            if flag == 1: (flag, number) = (0, 0)
            if flag == 2:
                sum += number
                (flag, number) = (0, 0)


print(sum)
                
