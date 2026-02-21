# K(<10**18)後の遷移を知りたい
# ダブリングっぽいか周期性
# dp[i][j]: j番目の要素から2**i回遷移した時の状態
# 2**10 > 10**3なので
# 2**60 > 10**18
# つまりdpの縦60あればOK(怖いので70くらい用意しておく)

N, K = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A[i] -= 1
dp = [[-1] * N for _ in range(70)]
# 一行目を埋める
for i in range(N):
    dp[0][i] = A[i]
for i in range(1, 70):
    for j in range(N):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]

now = 0
# 7 = 2**0 + 2**1 + 2**2
# のようにKも分解できる
for shift in range(70):
    if K >> shift & 1:
        now = dp[shift][now]
print(now + 1)
