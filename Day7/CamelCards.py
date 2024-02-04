import re

file = open("Day7\CamelCardsinput.txt", "r")
data = ''.join(file.readlines())
file.close()

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
    return 4


 
lista = []

for match in re.findall(r'(\w+) (\d+)',data):
    cards, bet = match
    lista.append((cards, bet, assignRank(cards)))


def partition(array, low, high):
 
    pivot = array[high]
 
    i = low - 1
 
    for j in range(low, high):
        if array[j][2] <= pivot[2]:

            i = i + 1

            (array[i], array[j]) = (array[j], array[i])
 
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    return i + 1

def quickSort(array, low, high):
    if low < high:
 
        pi = partition(array, low, high)
 
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

rankings = {
    '2':1,
    '3':2,
    '4':3,
    '5':4,
    '6':5,
    '7':6,
    '8':7,
    '9':8,
    'T':9,
    'J':10,
    'Q':11,
    'K':12,
    'A':13,
}

def highcard(hand1, hand2):
    for n in range(5):
        if  rankings[hand1[n]] > rankings[hand2[n]]:
            return True
        if rankings[hand1[n]] < rankings[hand2[n]]:
            return False

def orderByCard(array):
    for i in range(len(array)-1):
        for n in range(len(array)-1-i):
            if array[n][2] == array[n+1][2] and highcard(array[n][0], array[n+1][0]):
                (array[n], array[n+1]) = (array[n+1], array[n])

quickSort(lista, 0, len(lista)-1)
orderByCard(lista)

winnings = 0
for rank, play in enumerate(lista):
    winnings += int(play[1])*(rank+1)

print(winnings)

#251312383 no