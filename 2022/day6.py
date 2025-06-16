f = open("file.txt").readlines()[0].strip()
# f = open("test.txt").readlines()[0].strip()

# part A
d = []
for x in range(len(f) - 4):
    d = [f[x], f[x+1], f[x+2], f[x+3]]
    if len(list(set(d))) == 4:
        print(x+4)
        break

# part B
for x in range(13,len(f)):
    d = [f[x - i] for i in range(14)]
    # d.reverse()
    # print(x, d, len(list(set(d))))
    if len(list(set(d))) == 14:
        print(x+1)
        break
