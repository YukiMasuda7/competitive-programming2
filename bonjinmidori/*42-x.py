# 二次元DP
# ナップザック問題
# dp[i][j]: i品目まで使って、重さjまでの荷物までで出せる最大価値
# dp[i][j]の求め方は

N, W = map(int, input().split())
value = [0] * (N + 1)
weight = [0] * (N + 1)

for i in range(1, N + 1):
    w, v = map(int, input().split())
    value[i] = v
    weight[i] = w

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(W + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= weight[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - weight[i]] + value[i])
ans = -1
for i in range(N + 1):
    ans = max(ans, dp[i][-1])
print(ans)
