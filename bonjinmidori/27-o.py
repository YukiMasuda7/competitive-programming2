# 各ノードをスタートとしてdfsで訪れることのできるノードを探索
# visitedをsetで管理

import sys

sys.setrecursionlimit(10**6)


# s: スタート
# now: 現在地
def dfs(s, now, edges, visited):
    for to in edges[now]:
        if to not in visited[s]:
            visited[s].add(to)
            dfs(s, to, edges, visited)


N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)

visited = [set([i]) for i in range(N + 1)]

ans = 0
for s in range(1, N + 1):
    dfs(s, s, edges, visited)
for i in range(1, N + 1):
    ans += len(visited[i])
print(ans)
