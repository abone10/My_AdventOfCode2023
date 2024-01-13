import re

file = open("Day4\ScratchcardsInput.txt", "r")
data = file.readlines()
file.close()

result = 0
flag = 0
ncopie=[]
for line in range(len(data)):
    ncopie.append(1)

def ContentsShared(list1, list2):
    count = 0
    for n in list2:
        if n in list1:
            count +=1
    return  count


for i, line in enumerate(data):
    for NumberSeries in re.finditer(r'(\d+\s+)+', line):
        if flag == 0: 
            WinningNumbers = re.findall(r'\d+', NumberSeries.group())
            flag = 1
        else:
            PresentNumbers = re.findall(r'\d+', NumberSeries.group())
            matches = ContentsShared(WinningNumbers, PresentNumbers)

            for n in range(1, matches+1):
                ncopie[i+n] +=ncopie[i]
            result +=ncopie[i]

            flag = 0

print(result)
            
#Risultato: 20107