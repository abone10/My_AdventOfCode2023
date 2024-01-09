import re
#Part 1
p1= re.compile(r'(.*[:] )|[\n]')
p2= re.compile(r';\s')
p3= re.compile(r',\s')
p4= re.compile(r'\s')

f= open('Day2\CubeConundrumInput.txt','r')
data=f.readlines()
f.close()

balls={
    'red':12,
    'green':13,
    'blue':14
}

sum=0


def checkSet(set):
    for j in range(len(set)):
        #Single Extraction
        set[j]=p4.split(set[j])
        if (balls[set[j][1]]<int(set[j][0])): 
            return False
    return True

for n in range(len(data)):
    #single game
    flag=True
    data[n]=p2.split(p1.sub('', data[n]))
    for i in range(len(data[n])):
        #set
        data[n][i]=p3.split(data[n][i])
        if(checkSet(data[n][i])==False):
            flag=False
    if(flag):
        sum+=n+1

print(sum)