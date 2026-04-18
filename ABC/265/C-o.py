H, W = map(int, input().split())
G = [input() for _ in range(H)]

ny = 0
nx = 0
cnt = 0
flag = True
while flag:
    if G[ny][nx] == "U":
        if ny == 0:
            flag = False
        else:
            ny -= 1
    elif G[ny][nx] == "R":
        if nx == W - 1:
            flag = False
        else:
            nx += 1
    elif G[ny][nx] == "D":
        if ny == H - 1:
            flag = False
        else:
            ny += 1

    else:
        if nx == 0:
            flag = False
        else:
            nx -= 1

    cnt += 1
    if cnt > 10**8:
        print(-1)
        exit()

print(ny + 1, nx + 1)
