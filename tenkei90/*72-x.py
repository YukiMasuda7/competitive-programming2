H, W = map(int, input().split())
C = [list(input().strip()) for _ in range(H)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
used = [[False] * W for _ in range(H)]


def dfs(sy, sx, y, x):
    # 開始地点に戻ってきた（かつ開始地点は既に訪問済み）なら長さ0で終了
    if y == sy and x == sx and used[y][x]:
        return 0

    used[y][x] = True
    best = -(10**9)
    for dy, dx in dirs:
        ny, nx = y + dy, x + dx
        if not (0 <= ny < H and 0 <= nx < W):
            continue
        if C[ny][nx] == "#":
            continue
        # 開始地点以外の既訪問マスは通れない
        if (ny != sy or nx != sx) and used[ny][nx]:
            continue
        v = dfs(sy, sx, ny, nx)
        best = max(best, v + 1)
    used[y][x] = False
    return best


ans = -1
for i in range(H):
    for j in range(W):
        if C[i][j] == ".":
            ans = max(ans, dfs(i, j, i, j))

print(ans if ans > 2 else -1)
