with open("file.txt") as f:
    brokList = f.read().split('\n')

t = 0

def checkChar(c):
    if c.islower():
        return ord(c) - ord('`')
    else:
        return ord(c) - ord('&')
# part 1
# for x in brokList:
#     a, b = x[:len(x)//2], x[len(x)//2:]
#     c = ''.join(set(a).intersection(b))
#     t += checkChar(c)
# print(t)

# part 2
for x in range(0, len(brokList)-2, 3):
    a, b, c = brokList[x], brokList[x+1], brokList[x+2]
    d = ''.join(set(a).intersection(b).intersection(c))
    t += checkChar(d)
print(t)