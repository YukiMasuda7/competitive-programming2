# DFSでコストを管理していけばOK？(現コストの管理が面倒)
# ↑toがなくてreturnする際にnow_costを-1するなど、面倒
# 一度訪れた辺は訪れたくないのでvisited(bool)で判定

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
