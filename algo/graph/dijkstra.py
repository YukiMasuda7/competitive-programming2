# Dijkstra(優先度付きキューを使う)
# 確定済みノードをdecidedで管理
# ダイクストラでは未確定のうち最小コストのノードから確定させていく


# ① 重み付き最短経路
# 辺ごとにコストが違う

# ② グリッド＋移動コスト
# マスによってコストが違う

# ③ 通信・交通系問題
# 距離最小
# 料金最小

# 🔹 キーワードで判断
# 「最小コスト」
# 「重み付きグラフ」
# 「距離の合計最小」

# 🔹 使えないケース
# 負の辺がある → ベルマンフォード

# 🔹 特徴まとめ
# 優先度付きキュー使用
# O((N+M) log N)
# 「コスト最小」ならほぼこれ


import heapq

inf = 10**10

N, M = map(int, input().split())
edges_with_cost = [[] for _ in range(N + 1)]
for i in range(M):
    A, B, C = map(int, input().split())
    edges_with_cost[A].append((B, C))
    edges_with_cost[B].append((A, C))

q = []
decided = [False] * (N + 1)
costs = [inf] * (N + 1)
costs[1] = 0
heapq.heappush(q, (costs[1], 1))

while q:
    now = heapq.heappop(q)[1]
    if decided[now]:
        continue
    else:
        decided[now] = True

    for to in edges_with_cost[now]:
        if costs[now] + to[1] < costs[to[0]]:
            costs[to[0]] = costs[now] + to[1]
            heapq.heappush(q, (costs[to[0]], to[0]))

for i in range(1, N + 1):
    if costs[i] != inf:
        print(costs[i])
    else:
        print(-1)
