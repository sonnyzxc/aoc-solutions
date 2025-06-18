from utils.parse_input import get_input_1d_str

data = get_input_1d_str("01")

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
