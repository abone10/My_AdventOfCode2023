#Part 1
'''
f = open(r'Day1\TrebuchetInput.txt', 'r')
l = f.readlines()
f.close()

sum=0
for s in l:
    L=0
    R=len(s)-1
    while(s[L].isnumeric() == False):
        L+=1
    while(s[R].isnumeric() == False):
        R-=1
    LR=s[L]+s[R]
    sum+=int(LR)


print(sum)

'''
#part 2
f = open('Day1\TrebuchetInput.txt', 'r')
l = f.readlines()
f.close()

numbers = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", 'seven' : '7', 'eight' : '8', 'nine' : '9'}

def getNumber(s):
    L=0
    R=len(s)-1

    while(s[L].isnumeric() == False and L<len(s)-1):  
        L+=1
    Ln=s[L]
    while(s[R].isnumeric() == False and R>0):
        R-=1
    Rn=s[R]

    for key in numbers.keys():
        p=s.find(key)
        if (p>=0 and p<=L):
            L=p
            Ln=numbers[key]
        p=s.rfind(key)
        if(p>=R):
            R=p
            Rn=numbers[key]

    value=Ln+Rn
    return value
        

sum=0
for s in l:
    value=getNumber(s)
    sum+=int(value)

print(sum)
