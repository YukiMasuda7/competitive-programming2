# スタートを全探索して
# 各スタートからのBFSで見つかった最大コストたちのうち最大のものが答え
from collections import deque

directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def bfs(
    s,
    G,
):
    q = deque([s])
    cost = [[-1] * (W + 1) for _ in range(H + 1)]
    cost[s[0]][s[1]] = 0
    max_cost = -1
    while q:
        now = q.popleft()
        for d in directions:
            if 1 <= now[0] + d[0] <= H and 1 <= now[1] + d[1] <= W:
                if cost[now[0] + d[0]][now[1] + d[1]] == -1:
                    if G[now[0] + d[0]][now[1] + d[1]] == ".":
                        cost[now[0] + d[0]][now[1] + d[1]] = cost[now[0]][now[1]] + 1
                        max_cost = cost[now[0]][now[1]] + 1
                        q.append((now[0] + d[0], now[1] + d[1]))
    return max_cost


H, W = map(int, input().split())
G = [["#"] * (W + 1)]
for i in range(H):
    S = input()
    S = ["#"] + list(S)
    G.append(S)
stars = []
for i in range(H + 1):
    for j in range(W + 1):
        if G[i][j] == ".":
            stars.append((i, j))
ans = -(10**10)
for s in stars:
    ans = max(ans, bfs(s, G))
print(ans)
