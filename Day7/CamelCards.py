import re

file = open("Day7\CamelCardsinput.txt", "r")
data = ''.join(file.readlines())
file.close()
#print(data)

def assignRank(string):
    count = {}
    for ch in string:
        if ch not in count.keys():
            n = string.count(ch)
            if n==5:
                return 7
            if n==4: 
                return 6
            count[ch] = n
    results = list(count.values())
    if max(results) == 1:
        return 1
    if results.count(2) == 2:
        return 3
    if 2 in results and 3 in results:
        return 5
    if 2 in results:
        return 2
    if 3 in results:
        return 4

        


        
lista = []

for match in re.findall(r'(\w+) (\d+)',data):
    cards, bet = match
    print(cards, assignRank(cards))
    lista.append((cards, bet, assignRank(cards)))

