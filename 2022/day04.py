from utils.parse_input import get_input_1d_str

data = get_input_1d_str("04")

t0 = 0
t1 = 0
for x in data:
    a, b = x.split(',')[0].split('-'), x.split(',')[1].split('-')
    num1 = [i for i in range(int(a[0]), int(a[1])+1)]
    num2 = [i for i in range(int(b[0]), int(b[1])+1)]

    # part A
    if set(num1).issuperset(set(num2)) or set(num2).issuperset(set(num1)):
        t0 += 1

    # part B
    if set(num1).intersection(set(num2)):
        t1 += 1

print(t0, t1, sep="\n")
