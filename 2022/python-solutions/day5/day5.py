import re
import copy

l = [list(map(int, re.findall(r'\d+', l.strip()))) for l in open("file.txt")][10:]

s = {
    1: list("RGHQSBTN"),
    2: list("HSFDPZJ"),
    3: list("ZHV"),
    4: list("MZJFGH"),
    5: list("TZCDLMSR"),
    6: list("MTWVHZJ"),
    7: list("TFPLZ"),
    8: list("QVWS"),
    9: list("WHLMTDNC"),
}

s1 = copy.deepcopy(s)

# part A
for x in l:
    for i in range(x[0]):
        s[x[2]].append(s[x[1]].pop())

print("".join([s[-1] for s in s.values()]))

# part B
for x in l:
    a = ''.join(s1[x[1]][-x[0]:])
    for y in a:
        s1[x[1]].pop()
        s1[x[2]].append(y)

print("".join([s1[-1] for s1 in s1.values()]))


