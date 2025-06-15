# A, X = Rock
# B, Y = Paper
# C, Z = Scissors 

# 1 for Rock, 2 for Paper, and 3 for Scissors
# 0 if you lost, 3 if the round was a draw, and 6 if you won

# part 2: 
# X = Lose
# Y = Draw
# Z = Win

# part 1 results
# results = {
#     'X' : { 'A' : 4, 'B' : 1, 'C' : 7 },
#     'Y' : { 'A' : 8, 'B' : 5, 'C' : 2 },
#     'Z' : { 'A' : 3, 'B' : 9, 'C' : 6 }
# }
results = {
    'X' : { 'A' : 3, 'B' : 1, 'C' : 2 },
    'Y' : { 'A' : 1+3, 'B' : 2+3, 'C' : 3+3},
    'Z' : { 'A' : 2+6, 'B' : 3+6, 'C' : 1+6}
}

with open("file.txt") as f:
    brokList = f.read().split('\n')

total = 0

for x in brokList:
    temp = x.split(' ')
    total += results[temp[1]][temp[0]]

print(total)