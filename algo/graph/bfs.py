# BFS (O(N+M))

# BFS自体が何か値を返すわけではなく、
# 外部で用意したlistなどに操作を行うvoid関数として使う
# その操作されたlistなどを元に答えを出す

# ---------------------------------------------

# 使い道

# ① 単位重みの最短経路
# すべての辺の重みが1

# ② グリッド問題
# マス移動
# 壁あり迷路

# ③ 状態遷移問題
# パズル
# ビット状態探索

# ④ 二部グラフ判定
# 距離の偶奇で判定

# ✅ 使う場面
# 最短距離（辺の重みがすべて1）
# グリッドの最短経路
# 距離を求める問題

# 🔹 特徴まとめ
# 「最小回数」が出たら疑う
# 重みが全部同じならBFS

# ------------------------------------------------

# BFSならスタートからの距離を管理しやすい
# (BFSはキューで実装するので、スタートから等距離のノードから実行されるから)

# コストを扱う時、cost = -1がコスト無限(初期状態)に対応して、
# cost == -1 なら visited[pos]== False 、
# cost != -1 なら visited[pos]== True
# とすればvisitedの管理をしなくていい！

from collections import deque

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)

costs = [-1] * (N + 1)
costs[1] = 0
q = deque([1])

while q:
    now = q.popleft()
    for to in edges[now]:
        if costs[to] == -1:
            costs[to] = costs[now] + 1
            q.append(to)

for i in range(1, N + 1):
    print(costs[i])
