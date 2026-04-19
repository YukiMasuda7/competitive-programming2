# 木 & 隣り合わない (木は2部グラフ(2彩色)であることは当たり前)
# -> ある葉から数えた距離の偶奇でグループ分けできる
# サイズの大きい方のグループからN/2頂点選べばいい

from collections import deque

N = int(input())
edges = [[] for _ in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edges[A].append(B)
    edges[B].append(A)

# 葉は隣接ノードが1個
for i in range(N):
    if len(edges[i]) == 1:
        leaf = i

q = deque([leaf])
cost = [-1] * N
cost[leaf] = 0

while q:
    now = q.popleft()
    for to in edges[now]:
        if cost[to] == -1:
            q.append(to)
            cost[to] = cost[now] + 1

groupA = []
groupB = []
for i in range(N):
    if cost[i] % 2 == 0:
        groupA.append(i)
    else:
        groupB.append(i)
tmp = []
if len(groupA) >= len(groupB):
    for a in groupA:
        tmp.append(a)
else:
    for b in groupB:
        tmp.append(b)

ans = []
for i in range(N // 2):
    ans.append(tmp[i] + 1)
print(*ans)
