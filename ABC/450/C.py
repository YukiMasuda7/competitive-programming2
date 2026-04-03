# 領域内の1マスbfsすれば(その際に領域内のマスはvisited=Trueにする)
# その領域が最外周を含むのかがわかる

H, W = map(int, input().split())
S = [input() for _ in range(H)]

dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
visited = [[False] * W for _ in range(H)]


def bfs(y, x):
    out = False
    visited[y][x] = True
    q = [(y, x)]
    for i, j in q:
        if i == 0 or i == H - 1 or j == 0 or j == W - 1:
            out = True
        for dy, dx in dir:
            ii = i + dy
            jj = j + dx
            if 0 <= ii < H and 0 <= jj < W and S[ii][jj] == "." and not visited[ii][jj]:
                q.append((ii, jj))
                visited[ii][jj] = True
    return out


ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == "." and not visited[i][j]:
            if not bfs(i, j):
                ans += 1
print(ans)
