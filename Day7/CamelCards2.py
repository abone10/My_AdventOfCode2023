import re

file = open("Day7\CamelCardsinput.txt", "r")
data = ''.join(file.readlines())
file.close()




def assignRank(hand):
    jokers = 0
    count = {}
    
    for ch in hand:
        if ch == 'J':
            jokers += 1
            continue
        if ch not in count.keys():
            count[ch] = hand.count(ch)
    
    cNumbers = sorted(count.values(), reverse=True)
    print(hand, cNumbers)
    if jokers == 5 or cNumbers[0] + jokers == 5:
        return 6
    if cNumbers[0] + jokers == 4:
        return 5
    if cNumbers[0] + jokers == 3 and cNumbers[1] == 2:
        return 4
    if cNumbers[0] + jokers == 3:
        return 3
    if cNumbers[0] == 2 and cNumbers[1] == 2:
        return 2
    if cNumbers[0] + jokers == 2:
        return 1
    return 0

bets = []
for match in re.findall(r'(\w+) (\d+)',data):
    cards, bet = match
    bets.append((cards, bet, assignRank(cards)))
    print(assignRank(cards))
        
cardValue = {'J':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'Q':11, 'K':12, 'A':13 }

def priority(hand1, hand2):
    if hand1[2] > hand2[2]:
        return 1
    if hand1[2] < hand2[2]:
        return -1
    for  (c1, c2) in zip(hand1[0], hand2[0]):
        if cardValue[c1] > cardValue[c2]:
            return 1
        if cardValue[c1] < cardValue[c2]:
            return -1


def orderHands(array):
    for l in range(len(array)-1):
        Flag = True
        for n in range(len(array)-1):
            if priority(array[n], array[n+1]) == 1:
                (array[n], array[n+1]) = (array[n+1], array[n])
                Flag = False
        if Flag == True:
            return
                
orderHands(bets)

result = 0
for i, (cards, bet, rank) in enumerate(bets):
    result += int(bet) * (i+1)
print(result)
#249912316
#250577259