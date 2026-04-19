# 2次元の累積和
# 4点に+1, -1を入れてimos法
N = int(input())
G = [[0] * 1002 for _ in range(1002)]
ans = [0] * (N + 1)
for i in range(N):
    ly, lx, ry, rx = map(int, input().split())
    G[ly][lx] += 1
    G[ly][rx] -= 1
    G[ry][lx] -= 1
    G[ry][rx] += 1

# 横に足す
for i in range(1002):
    for j in range(1, 1002):
        G[i][j] += G[i][j - 1]
# 縦に足す
for i in range(1002):
    for j in range(1, 1002):
        G[j][i] += G[j - 1][i]

for i in range(1001):
    for j in range(1001):
        if 1 <= G[i][j]:
            ans[G[i][j]] += 1
for i in range(1, N + 1):
    print(ans[i])
