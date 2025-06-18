from pathlib import Path

input_dir = f"{Path(__file__).parent}/day03.txt"
with open(input_dir) as f:
    data = f.read().split("\n")

def checkChar(c):
    if c.islower():
        return ord(c) - ord('`')
    else:
        return ord(c) - ord('&')

def part1():
    ans = 0

    for x in data:
        a, b = x[:len(x)//2], x[len(x)//2:]
        ans += checkChar(''.join(set(a).intersection(b)))

    print(ans)

def part2():
    ans = 0

    for x in range(0, len(data)-2, 3):
        a, b, c = data[x], data[x+1], data[x+2]
        d = ''.join(set(a).intersection(b).intersection(c))
        ans += checkChar(d)

    print(ans)

part1()
part2()
