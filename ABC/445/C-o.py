# ダブリングっぽい？ -> 10**100は流石に無理か？
# 高々N(<5 * 10**5)のパターンの繰り返しでは？
# dp[i][j]: j番目の要素から2**i回遷移した時の状態
# キリよくs=0がi回後(1<=i<=10**6)にどこにいるかを配列Pで持っとけばいい？

N = int(input())
A = list(map(int, input().split()))

LEVELS = 30
dp = [[None] * N for i in range(LEVELS)]
# 2**0 = 1 しか移動しない場合 -> A[i]-1に移動
for i in range(0, N):
    dp[0][i] = A[i] - 1
# 1日後の1日後が2日後、2日後の2日後が4日後、4日後の4日後が8日後
for d in range(1, LEVELS):
    for i in range(0, N):
        dp[d][i] = dp[d - 1][dp[d - 1][i]]

ans = []
for i in range(N):
    ans.append(dp[29][i] + 1)

print(*ans)
