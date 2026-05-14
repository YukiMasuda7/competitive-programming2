# 明らかにdpっぽい
# dp[i]: i段目への到達方法の数
mod = 10**9 + 7

N, L = map(int, input().split())
dp = [0] * (N + 1)
dp[0] = 1
for i in range(1, N + 1):
    dp[i] += dp[i - 1]
    if i - L >= 0:
        dp[i] += dp[i - L]
    dp[i] %= mod
print(dp[-1])
