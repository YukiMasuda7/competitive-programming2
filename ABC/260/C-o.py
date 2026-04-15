# bit全探索？->無理そう
# 操作回数は不明->再帰?

import sys

sys.setrecursionlimit(10**7)


def dfs(l):
    if l <= 1:
        return
    jewels[l][1] += X * jewels[l][0]
    jewels[l - 1][0] += jewels[l][0]
    jewels[l][0] = 0

    jewels[l - 1][1] += Y * jewels[l][1]
    jewels[l - 1][0] += jewels[l][1]
    jewels[l][1] = 0

    dfs(l - 1)


N, X, Y = map(int, input().split())
# jewels[i][j]
# i->0(赤)、1(青)
# j-> レベル
jewels = [[0] * 2 for _ in range(N + 1)]
jewels[N][0] = 1
dfs(N)
print(jewels[1][1])
