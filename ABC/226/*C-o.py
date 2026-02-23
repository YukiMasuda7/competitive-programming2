# DPは無理そう？
# 最短コスト -> ゴールからのBFS?
# DFS or BFSでpathを調べる(取得しないといけない技一覧)
# pathのコストの合計が答え

from collections import deque

N = int(input())
T = [0] * (N + 1)
K = [0] * (N + 1)
A = [[0]]
completed = [False] * (N + 1)

for i in range(1, N + 1):
    X = list(map(int, input().split()))
    T[i] = X[0]
    K[i] = X[1]
    if K[i] > 0:
        A.append(X[2:])
    else:
        A.append([])
q = deque([N])
visited = [False] * (N + 1)
while q:
    now = q.popleft()
    visited[now] = True
    for to in A[now]:
        if visited[to]:
            continue
        else:
            q.append(to)

ans = 0
for i in range(1, N + 1):
    if visited[i]:
        ans += T[i]
print(ans)
