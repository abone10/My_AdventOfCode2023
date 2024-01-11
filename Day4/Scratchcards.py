import re

file = open("Day4\ScratchcardsInput.txt", "r")
data = file.readlines()
file.close()

def ContentsShared(list1, list2):
    count = 0
    for n in list2:
        if n in list1:
            count +=1
    return  count

result = 0

flag = 0
for i, line in enumerate(data):
    for NumberSeries in re.finditer(r'(\d+\s+)+', line):
        if flag == 0: 
            WinningNumbers = re.findall(r'\d+', NumberSeries.group())
            flag = 1
        else:
            PresentNumbers = re.findall(r'\d+', NumberSeries.group())
            matches = ContentsShared(WinningNumbers, PresentNumbers)
            if matches >0:
                result += pow(2, matches-1)
            flag = 0

print(result)
            
#Risultato: 20107