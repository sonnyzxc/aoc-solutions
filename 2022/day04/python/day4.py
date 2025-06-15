with open("file.txt") as f:
    brokList = f.read().split('\n')

t0 = 0
t1 = 0
for x in brokList:
    a, b = x.split(',')[0].split('-'), x.split(',')[1].split('-')
    num1 = [i for i in range(int(a[0]), int(a[1])+1)]
    num2 = [i for i in range(int(b[0]), int(b[1])+1)]

    # part A
    if set(num1).issuperset(set(num2)) or set(num2).issuperset(set(num1)):
        t0 += 1

    # part B
    if set(num1).intersection(set(num2)):
        t1 += 1

print(t0, t1)