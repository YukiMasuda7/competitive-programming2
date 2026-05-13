from collections import deque

INF = 10**18
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

H, W = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
sy -= 1
sx -= 1
gy -= 1
gx -= 1
S = [input().strip() for _ in range(H)]

dist = [[[INF] * 4 for _ in range(W)] for _ in range(H)]
dq = deque()

for d in range(4):
    dist[sy][sx][d] = 0
    dq.append((sy, sx, d))

while dq:
    y, x, pd = dq.popleft()
    cur = dist[y][x][pd]

    for nd, (dy, dx) in enumerate(dirs):
        ny, nx = y + dy, x + dx
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        if S[ny][nx] == "#":
            continue

        ndist = cur + (0 if nd == pd else 1)
        if ndist < dist[ny][nx][nd]:
            dist[ny][nx][nd] = ndist
            # 同じ方向の移動(コスト0の遷移)を優先する
            if nd == pd:
                dq.appendleft((ny, nx, nd))
            else:
                dq.append((ny, nx, nd))

ans = min(dist[gy][gx])
print(ans if ans < INF else -1)
