H, W, N = map(int, input().split())
Z = [[0] * (W + 2) for _ in range(H + 2)]
for i in range(N):
    A, B, C, D = map(int, input().split())
    Z[A][B] += 1
    Z[A][D + 1] -= 1
    Z[C + 1][B] -= 1
    Z[C + 1][D + 1] += 1

# 横向きに足す
for i in range(1, H + 1):
    for j in range(W):
        Z[i][j + 1] += Z[i][j]

# 縦向きに足す
for i in range(1, W + 1):
    for j in range(H):
        Z[j + 1][i] += Z[j][i]

for i in range(1, H + 1):
    print(*Z[i][1 : W + 1])
