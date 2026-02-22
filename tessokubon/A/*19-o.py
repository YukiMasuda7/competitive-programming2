# ナップザック問題
# dp[i][j]: i品目まで使って、重さj以下で実現できる価値の最大値

N, W = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, W + 1):
        dp[i][j] = dp[i - 1][j]
        if j - X[i - 1][0] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - X[i - 1][0]] + X[i - 1][1])
ans = -1
for i in range(N + 1):
    ans = max(ans, dp[i][W])
print(ans)
