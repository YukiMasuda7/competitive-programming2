# 制約大事
H, W, Q = map(int, input().split())
S = [input() for _ in range(H)]
dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]
buldings = {}
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "B":
            buldings[(i, j)] = False
            for dy, dx in dir:
                ny = i + dy
                nx = j + dx
                if 0 <= ny < H and 0 <= nx < W:
                    if S[ny][nx] == "R":
                        buldings[(i, j)] = True
                        ans += 1

for i in range(Q):
    U, D, L, R = map(int, input().split())
    U -= 1
    D -= 1
    L -= 1
    R -= 1
    # 左辺, 右辺
    for j in range(U, D + 1):
        if L - 1 >= 0:
            if (j, L - 1) in buldings:
                if not buldings[(j, L - 1)]:
                    ans += 1
                    buldings[(j, L - 1)] = True
        if R + 1 < W:
            if (j, R + 1) in buldings:
                if not buldings[(j, R + 1)]:
                    ans += 1
                    buldings[(j, R + 1)] = True
    # 上辺、下辺
    for j in range(L, R + 1):
        if U - 1 >= 0:
            if (U - 1, j) in buldings:
                if not buldings[(U - 1, j)]:
                    ans += 1
                    buldings[(U - 1, j)] = True

        if D + 1 < H:
            if (D + 1, j) in buldings:
                if not buldings[(D + 1, j)]:
                    ans += 1
                    buldings[(D + 1, j)] = True
    print(ans)
