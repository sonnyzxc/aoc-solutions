from functools import reduce
from operator import mul
from utils.parse_input import get_input_2d_int

data = get_input_2d_int("08")
N, M = len(data), len(data[0])

ans1 = 0
ans2 = 0
for j in range(N):
    for k in range(M):
        if j in [0, N - 1] or k in [0, M - 1]:
            ans1 += 1
            continue

        cur = data[j][k]
        left = [data[j][x] for x in range(k)]
        right = [data[j][x] for x in range(k + 1, M)]
        top = [data[y][k] for y in range(j)]
        down = [data[y][k] for y in range(j + 1, N)]

        # part 1
        if any([
            all(cur > h for h in left),
            all(cur > h for h in right),
            all(cur > h for h in top),
            all(cur > h for h in down),
        ]):
            ans1 += 1

        # part 2
        ans2 = max(ans2, reduce(mul, [
            next((i + 1 for i, h in enumerate(reversed(left)) if cur <= h), len(left)),
            next((i + 1 for i, h in enumerate(right) if cur <= h), len(right)),
            next((i + 1 for i, h in enumerate(reversed(top)) if cur <= h), len(top)),
            next((i + 1 for i, h in enumerate(down) if cur <= h), len(down))
        ]))

print(ans1)
print(ans2)
