import re
#Part 1
p1= re.compile(r'(.*[:] )|[\n]')
p2= re.compile(r';\s')
p3= re.compile(r',\s')
p4= re.compile(r'\s')

f= open('Day2\CubeConundrumInput.txt','r')
data=f.readlines()
f.close()

sum=0



def checkSet(set):
    for j in range(len(set)):
        #Single Extraction
        set[j]=p4.split(set[j])
        if (ballz[set[j][1]]<int(set[j][0])): 
            ballz[set[j][1]]=int(set[j][0])
    return 0
    

for n in range(len(data)):
    #single game
    ballz={
        'red':0,
        'green':0,
        'blue':0
    }
    qta=ballz.values()
    data[n]=p2.split(p1.sub('', data[n]))
    for i in range(len(data[n])):
        #set
        data[n][i]=p3.split(data[n][i])
        sum+=checkSet(data[n][i])
    
    p=1
    for n in qta:
        p=p*n
    sum+=p

print(sum)