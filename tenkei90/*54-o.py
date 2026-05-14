# K(<10**18)後の遷移を知りたい
# ダブリング or 周期性?
# dp[i][j]: j番目の要素から2**i回遷移した時の状態
# 2**10 > 10**3なので
# 2**60 > 10**18
# つまりdpの縦60あればOK
def convert(N: int):
    x = N
    S = str(N)
    S = list(S)
    y = 0
    for s in S:
        y += int(s)
    z = (x + y) % 10**5
    return z


N, K = map(int, input().split())
dp = [[0] * 10**5 for _ in range(60)]
# 1行目を埋める
for i in range(10**5):
    dp[0][i] = convert(i)
# dpを埋める
for i in range(1, 60):
    for j in range(10**5):
        dp[i][j] = dp[i - 1][dp[i - 1][j]]

now = N
for shift in range(60):
    if K >> shift & 1:
        now = dp[shift][now]
print(now)
