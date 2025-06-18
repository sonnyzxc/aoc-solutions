from utils.parse_input import get_input_1d_str

data = get_input_1d_str("02")

'''
A, X = Rock
B, Y = Paper
C, Z = Scissors
'''

def part1():
    '''
    1 for Rock, 2 for Paper, and 3 for Scissors
    0 if you lost, 3 if the round was a draw, and 6 if you won
    '''
    results = {
        'X' : { 'A' : 4, 'B' : 1, 'C' : 7 },
        'Y' : { 'A' : 8, 'B' : 5, 'C' : 2 },
        'Z' : { 'A' : 3, 'B' : 9, 'C' : 6 }
    }
    ans = 0

    for x in data:
        temp = x.split(' ')
        ans += results[temp[1]][temp[0]]

    print(ans)

def part2():
    '''
    X = Lose
    Y = Draw
    Z = Win
    '''
    results = {
        'X' : { 'A' : 3, 'B' : 1, 'C' : 2 },
        'Y' : { 'A' : 1+3, 'B' : 2+3, 'C' : 3+3},
        'Z' : { 'A' : 2+6, 'B' : 3+6, 'C' : 1+6}
    }
    ans = 0

    for x in data:
        temp = x.split(' ')
        ans += results[temp[1]][temp[0]]

    print(ans)

part1()
part2()
