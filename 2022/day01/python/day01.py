from pathlib import Path

input_dir = f"{Path(__file__).parent.parent}/day01.txt"
with open(input_dir) as f:
    data = f.read().split("\n")

def part1():
    temp = ans = 0
    for x in data:
        if x == "":
            ans = max(ans, temp)
            temp = 0
        else:
            temp += int(x)

    print(ans)

def part2():
    caloList = []
    temp = 0
    for x in data:
        if x == "":
            caloList.append(temp)
            temp = 0 
        else:
            temp += int(x)

    print(sum(sorted(caloList)[-3:]))

part1()
part2()
