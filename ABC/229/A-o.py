# ↓やりすぎ
# "No"のパターンは#が対角上に並んだ2パターンだけ

from collections import deque

G = [list(input()) for _ in range(2)]
blacks = []
directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
for i in range(2):
    for j in range(2):
        if G[i][j] == "#":
            blacks.append((i, j))
visited = [[False] * 2 for _ in range(2)]
q = deque([blacks[0]])
visited[blacks[0][0]][blacks[0][1]] = True
while q:
    now = q.popleft()
    for d in directions:
        x = now[0] + d[0]
        y = now[1] + d[1]
        if 0 <= x <= 1 and 0 <= y <= 1 and visited[x][y] == False and G[x][y] == "#":
            q.append((x, y))
            visited[x][y] = True
visit_count = 0
for i in range(2):
    for j in range(2):
        if visited[i][j]:
            visit_count += 1
if visit_count == len(blacks):
    print("Yes")
else:
    print("No")
