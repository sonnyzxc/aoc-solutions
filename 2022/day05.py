import copy
import re
from pathlib import Path

input_dir = f"{Path(__file__).parent}/day05.txt"
l = [list(map(int, re.findall(r'\d+', l.strip()))) for l in open(input_dir)][10:]

s = {
    1: list("BWN"),
    2: list("LZSPTDMB"),
    3: list("QHZWR"),
    4: list("WDVJZR"),
    5: list("SHMB"),
    6: list("LGNJHVPB"),
    7: list("JQZFHDLS"),
    8: list("WSFJGQB"),
    9: list("ZWMSCDJ"),
}

s1 = copy.deepcopy(s)

def part1():
    for x in l:
        for i in range(x[0]):
            s[x[2]].append(s[x[1]].pop())

    print("".join([s[-1] for s in s.values()]))

def part2():
    for x in l:
        a = ''.join(s1[x[1]][-x[0]:])
        for y in a:
            s1[x[1]].pop()
            s1[x[2]].append(y)

    print("".join([s1[-1] for s1 in s1.values()]))

part1()
part2()
