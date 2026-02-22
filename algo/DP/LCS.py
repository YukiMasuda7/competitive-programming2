# LCS（Longest Common Subsequence、最長共通部分列）
# O(|S| * |T|)

# dp[i][j]:(i,j)に達するまでに通る、斜めの矢印((i-1,j-1) -> (i,j))の本数の最大値

# dp[i][j]への移動方法は下の3つがあって
# 1. (i-1,j)から下へ
# 2. (i,j-1)から右へ
# 3. (i-1,j-1)から斜めへ
# それぞれ下の値にdp[i][j]を更新する
# 1. dp[i-1][j]
# 2. dp[i][j-1]
# 3. dp[i-1][j-1] + 1
# i=0 or j=0の場合を考慮する1と2が出来ない事もあるので、
# さらに場合分けが生じる
# a. S[i]==T[i]の時
#    dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
# b. S[i]!=T[i]の時
#    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 鉄則4.5

S = input()
T = input()
N = len(S)
M = len(T)

# 動的計画法
dp = [[None] * (M + 1) for i in range(N + 1)]
dp[0][0] = 0
for i in range(0, N + 1):
    for j in range(0, M + 1):
        if i >= 1 and j >= 1 and S[i - 1] == T[j - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
        elif i >= 1 and j >= 1:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        elif i >= 1:
            dp[i][j] = dp[i - 1][j]
        elif j >= 1:
            dp[i][j] = dp[i][j - 1]

# 出力
print(dp[N][M])
