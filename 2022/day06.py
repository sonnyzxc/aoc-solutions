from pathlib import Path

input_dir = f"{Path(__file__).parent}/day06.txt"
f = open(input_dir).readlines()[0].strip()

def part1():
    d = []
    for x in range(len(f) - 4):
        d = [f[x], f[x+1], f[x+2], f[x+3]]
        if len(list(set(d))) == 4:
            print(x+4)
            break

def part2():
    for x in range(13,len(f)):
        d = [f[x - i] for i in range(14)]
        # d.reverse()
        # print(x, d, len(list(set(d))))
        if len(list(set(d))) == 14:
            print(x+1)
            break

part1()
part2()
