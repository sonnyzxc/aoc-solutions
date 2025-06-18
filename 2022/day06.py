from utils.parse_input import get_input_str

data = get_input_str("06")

def part1():
    d = []
    for x in range(len(data) - 4):
        d = [data[x], data[x+1], data[x+2], data[x+3]]
        if len(list(set(d))) == 4:
            print(x+4)
            break

def part2():
    for x in range(13, len(data)):
        d = [data[x - i] for i in range(14)]
        if len(list(set(d))) == 14:
            print(x+1)
            break

part1()
part2()
