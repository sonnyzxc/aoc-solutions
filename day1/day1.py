caloList = []

with open("file.txt") as f:
    brokList = f.read().split('\n')

temp = 0
for x in brokList:
    if x == '':
        caloList.append(temp)
        temp = 0 
    else:
        temp += int(x)
    
caloList.sort()
caloList.reverse()
print(sum(caloList[0:3]))
