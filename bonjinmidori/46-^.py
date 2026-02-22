# 自力でできた！
# Nが小さい(<10**3)のが引っかかる
# DPっぽい？
# dp[i]:i以上のダメージを与えるための最小コスト

H, N = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
X = sorted(X, key=lambda x: x[1])

dp = [10**10] * (H + 1)
dp[0] = X[0][1]
for i in range(1, H + 1):
    m = 10**10
    for j in range(N):
        if X[j][0] >= i:
            m = min(m, X[j][1])
        if i - X[j][0] >= 0:
            m = min(m, dp[i - X[j][0]] + X[j][1])
        dp[i] = m
print(dp[-1])
