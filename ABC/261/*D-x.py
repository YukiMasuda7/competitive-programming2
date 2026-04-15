from collections import defaultdict

N, M = map(int, input().split())
X = [0] + list(map(int, input().split()))
bonus = defaultdict(int)

for _ in range(M):
    C, Y = map(int, input().split())
    bonus[C] = Y

INF = 10**30
dp = [[-INF] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0

for j in range(N):  # いま j 回終わっている
    for i in range(j + 1):  # 連続表回数 i は 0..j
        if dp[i][j] == -INF:
            continue
        # 裏
        dp[0][j + 1] = max(dp[0][j + 1], dp[i][j])
        # 表（j+1 回目のコイン）
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + X[j + 1] + bonus[i + 1])

print(max(dp[i][N] for i in range(N + 1)))
