# 間に合わないし、規則性などもない
# -> DP
# dp[i][j]=i個目まで操作して先頭がjの場合の数

mod = 998244353

N = int(input())
A = list(map(int, input().split()))

dp = [[0] * 10 for _ in range(N)]
dp[0][A[0]] = 1

for i in range(1, N):

    for j in range(10):
        x = (j + A[i]) % 10
        y = (j * A[i]) % 10

        dp[i][x] += dp[i - 1][j]
        dp[i][y] += dp[i - 1][j]
        dp[i][x] %= mod
        dp[i][y] %= mod

for i in range(10):
    print(dp[-1][i])
