# 行き方は(N-1)!通り
# (8-1)! = 5040なので十分間に合う
# 1以外の数字の順列を全列挙すればよい
from itertools import permutations

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
s = [i for i in range(1, N)]
patterns = permutations(s, N - 1)

ans = 0
for p in patterns:
    # 最初と最後のコストを足す
    cost = T[0][p[0]] + T[p[-1]][0]
    for i in range(N - 2):
        cost += T[p[i]][p[i + 1]]

    if cost == K:
        ans += 1

print(ans)
