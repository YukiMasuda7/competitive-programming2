# 木に対する動的計画法

N = int(input())
A = [0] * 2 + list(map(int, input().split()))

# Gは自分の部下を格納するリスト
G = [[] for _ in range(N + 1)]
for i in range(2, N + 1):
    G[A[i]].append(i)

# dp[x]: 社員xの部下の数
# 今回は上司のind < 部下のind の制約があるので
# 部下の数0の人(indの大きい人)から探索、dpの確定を行う
# もし制約がないならind=1からの距離を求めて(BFS)、
# ソートして、遠い人(部下が0の人)から同じことを行う

dp = [0] * (N + 1)
for i in range(N, 0, -1):
    for j in G[i]:
        dp[i] += dp[j] + 1

print(*dp[1:])
