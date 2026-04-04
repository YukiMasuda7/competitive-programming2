# 初めてもらうのは高橋にもらうor他のすぬけからもらうのうち早い方
# DP？すぬけ1の最短時間がわかればすぬけ２の最短時間は 髙橋経由 or すぬけ1経由 のどちらかになる
N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))
# SS: すぬけiからすぬけ1に渡るまでにかかる時間
SS = [0] * N
SS[N - 1] = S[N - 1]
for i in range(N - 1, 0, -1):
    SS[i - 1] = SS[i] + S[i - 1]

dp = T
# dp[0]を求めていく(dp[0]=T[0])
# for i in range(1, N):
#     dp[0] = min(dp[0], SS[i] + T[i])
dp[0] = T[0]
# dpを更新
for i in range(1, N):
    dp[i] = min(dp[i], dp[i - 1] + S[i - 1])
for i in range(N):
    print(dp[i])
