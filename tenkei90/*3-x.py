# 木であることに注目
# 木におけるある頂点からある頂点への単純パスは1つしかない

# 最長路のループを作りたい
# -> 最長路の長さ(木の直径)に+1したものが答え

# 木の直径の求め方(2回bfs or dfs)
# (1)適当な点uを選ぶ
# (2)uから最も遠い点vを求める
# (3)vから最も遠い点wを求める

# パスv-wの長さが木の直径

from collections import deque


def bfs(start):
    q = deque([start])
    cost = [-1] * N
    cost[start] = 0
    while q:
        now = q.popleft()
        for to in edges[now]:
            if cost[to] == -1:
                cost[to] = cost[now] + 1
                q.append(to)
    max_cost = max(cost)
    for i in range(N):
        if cost[i] == max_cost:
            ans = i
    return [ans, cost[ans]]


N = int(input())
edges = [[] for _ in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    edges[A].append(B)
    edges[B].append(A)

# 0からの最長距離を考えてみる
v = bfs(0)[0]
# vからの最長距離を考える
ans = bfs(v)[1] + 1
print(ans)
