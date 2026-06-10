H, W, K = map(int, input().split())
G = [[0] * W for _ in range(H)]
for i in range(H):
    S = input()
    S = list(S)
    for j in range(W):
        G[i][j] = int(S[j])
for i in range(H):
    for j in range(1, W):
        G[i][j] += G[i][j - 1]

for i in range(W):
    for j in range(1, H):
        G[j][i] += G[j - 1][i]
print(G)

def f(r1,c1,r2,c2):
    ans=G[r1][c1]-G[r1-1][c2]-G[r2][c1-1]+G[r1-1][c1-1]
    print(ans)
