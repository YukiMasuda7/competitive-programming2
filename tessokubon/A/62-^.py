# DFS
# 再帰とstackの二つの実装方法がある

# 連結判定 (union findでも出来る)
# どこからスタートしても同じ
# 訪れたノードlistのsetがNなら連結
# 終了条件を明示しないと無限ループになる

# ---------------------------------------------------

# 再帰

import sys

# 再帰呼び出しの深さの上限を 120000 に設定
sys.setrecursionlimit(120000)


# 深さ優先探索を行う関数（pos は現在位置、visited[x] は頂点 x が青色かどうかを表す真偽値）
def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)


# 入力
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

# 隣接リストの作成
G = [list() for i in range(N + 1)]  # G[i] は頂点 i に隣接する頂点のリスト
for a, b in edges:
    G[a].append(b)  # 頂点 a に隣接する頂点として b を追加
    G[b].append(a)  # 頂点 b に隣接する頂点として a を追加

# 深さ優先探索
visited = [False] * (N + 1)
dfs(1, G, visited)

# 連結かどうかの判定（answer = True のとき連結）
answer = True
for i in range(1, N + 1):
    if visited[i] == False:
        answer = False

if answer == True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")

# ---------------------------------------------------

# stackでの実装

from collections import deque

N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    edges[A].append(B)
    edges[B].append(A)

q = deque([1])
visited = {1}

while q:
    now = q.pop()
    visited.add(now)
    for to in edges[now]:
        if to not in visited:
            q.append(to)

if len(visited) == N:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
