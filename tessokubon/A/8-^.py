H, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(H)]
# (H+1)*(W+1)に拡張
S = [[0] * (W + 1) for _ in range(H + 1)]
for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] = X[i][j]
# 横向きに足す
for i in range(H):
    for j in range(W):
        S[i + 1][j + 1] += S[i + 1][j]
# 縦向きに足す
for i in range(W):
    for j in range(H):
        S[j + 1][i + 1] += S[j][i + 1]

Q = int(input())
for i in range(Q):
    A, B, C, D = map(int, input().split())
    ans = S[C][D] - S[C][B - 1] - S[A - 1][D] + S[A - 1][B - 1]
    print(ans)
