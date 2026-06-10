K = 10**100
H, W = map(int, input().split())
G = [list(input().strip()) for _ in range(H)]
dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def step(grid):
    H = len(grid)
    W = len(grid[0])
    nxt_flag = [[False] * W for _ in range(H)]
    # 初期値: 現在 '.' のところを True（以降の判定で上書き）
    for i in range(H):
        for j in range(W):
            if grid[i][j] == ".":
                nxt_flag[i][j] = True

    # 変換ルール（元コードの意図をそのまま反映）
    for i in range(H):
        for j in range(W):
            if grid[i][j] == "#":
                nxt_flag[i][j] = True
            else:
                # '.' のセルで周囲に '#' があれば False にする
                f = False
                for dy, dx in dirs:
                    ny, nx = i + dy, j + dx
                    if 0 <= ny < H and 0 <= nx < W and grid[ny][nx] == "#":
                        f = True
                        break
                if f:
                    nxt_flag[i][j] = False

    new_grid = [["#"] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            new_grid[i][j] = "." if nxt_flag[i][j] else "#"
    return new_grid


# 周期検出
seen = {}  # state_key -> index
states = []
now = ["".join(row) for row in G]
while True:
    key = tuple(now)
    if key in seen:
        mu = seen[key]
        lam = len(states) - mu
        break
    seen[key] = len(states)
    states.append([list(row) for row in now])
    # 次状態
    grid = [list(row) for row in now]
    grid = step(grid)
    now = ["".join(row) for row in grid]

# K に対応するインデックスを決定
if K < len(states):
    ans_grid = states[K]
else:
    idx = mu + (K - mu) % lam
    ans_grid = states[idx]

for row in ans_grid:
    print("".join(row))
