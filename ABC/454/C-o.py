# DFSっぽい？
# 448-Dっぽい
import sys

sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)
visited = set()


def dfs(now):
    visited.add(now)
    for to in edges[now]:
        if to not in visited:
            dfs(to)


dfs(1)
print(len(visited))
