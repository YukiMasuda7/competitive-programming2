# どこかでループしそう
# 周期2の繰り返し？→10**100%2==0なので2回目のみ求めればいい？
H, W = map(int, input().split())
G = [list(input().strip()) for _ in range(H)]
dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
for k in range(32):
    # Trueが白、Falseが黒
    flag = [[False] * W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if G[i][j] == ".":
                flag[i][j] = True

    for i in range(H):
        for j in range(W):
            if G[i][j] == "#":
                flag[i][j] = True
            else:
                f = False
                for dy, dx in dir:
                    ny = i + dy
                    nx = j + dx
                    if 0 <= ny < H and 0 <= nx < W and G[ny][nx] == "#":
                        f = True
                        break
                if f:
                    flag[i][j] = False

    for i in range(H):
        for j in range(W):
            if flag[i][j] == True:
                G[i][j] = "."
            else:
                G[i][j] = "#"
    # print(k + 1)
    # for i in range(H):
    #     print("".join(G[i]))


for i in range(H):
    print("".join(G[i]))
