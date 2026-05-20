dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
H, W = map(int, input().split())
ans = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        cnt = 0
        for dy, dx in dir:
            ny = i + dy
            nx = j + dx
            if 0 <= ny < H and 0 <= nx < W:
                cnt += 1

        ans[i][j] = cnt
for a in ans:
    print(*a)
