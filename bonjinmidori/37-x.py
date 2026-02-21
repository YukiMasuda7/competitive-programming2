# BFSで各ノードから1までの最短パスを探す
# 最初に訪れるノードが答え

# ↑は間に合わない
# ゴールから探索していき、訪れたノードはもう訪れないようにすれば
# 1からのm最短経路(これはmから1の最短経路の逆)がわかる
from collections import deque

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)

q = deque([1])
visited = [False] * (N + 1)
visited[1] = True
mark = [-1] * (N + 1)

while q:
    now = q.popleft()
    for to in edges[now]:
        if not visited[to]:
            q.append(to)
            visited[to] = True
            mark[to] = now
print("Yes")
for i in range(2, N + 1):
    print(mark[i])
