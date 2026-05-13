# 格桁の和がKかつ9の倍数のもの

# dp[i] = 桁和が i になる並び方の数
# とすると、
# dp[i-1] に 1 を足す
# dp[i-2] に 2 を足す
# ...
# dp[i-9] に 9 を足す
# ので、
# dp[i] = dp[i-1] + ... + dp[i-9]

MOD = 10**9 + 7
K = int(input())

if K % 9 != 0:
    print(0)
else:
    dp = [0] * (K + 1)
    dp[0] = 1

    for i in range(1, K + 1):
        for x in range(1, 10):
            if i - x >= 0:
                dp[i] = (dp[i] + dp[i - x]) % MOD

    print(dp[K])
