H, W = map(int, input().split())
G = [["."] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i == 0 or i == H - 1 or j == 0 or j == W - 1:
            G[i][j] = "#"

for i in range(H):
    print("".join(G[i]))
