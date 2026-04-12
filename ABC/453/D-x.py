# 方向状態つきBFSの経路復元
# 同じマスであってもどっち方向から入ってきたかでコストを変えないといけない
# 直前の移動方向はqに一緒に渡せばいい
# 上、右、下、左の順に0, 1, 2, 3を割り当てる

from collections import deque

directions = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]

H, W = map(int, input().split())
S = []
for _ in range(H):
    s = input()
    s = list(s)
    S.append(s)

# 開始状態は方向を持たないので4に割り当て
start = [0, 0, 4]
goal = [0, 0, 4]
for i in range(H):
    for j in range(W):
        if S[i][j] == "S":
            start[0] = i
            start[1] = j
        if S[i][j] == "G":
            goal[0] = i
            goal[1] = j

# costs[i][j][k]: k方向から(i, j)に入った時のコスト
# 開始状態は方向を持たないので4に割り当て
# H*W*5の書き方注意
costs = [[[-1] * 5 for _ in range(W)] for _ in range(H)]
costs[start[0]][start[1]][4] = 0


q = deque([start])
while q:
    now = q.popleft()
    ny = now[0]
    nx = now[1]
    prev = now[2]
    for dir in range(len(directions)):
        dy = ny + directions[dir][0]
        dx = nx + directions[dir][1]
        if 0 <= dy <= H - 1 and 0 <= dx <= W - 1:
            if costs[dy][dx][dir] == -1:
                if S[dy][dx] == "#":
                    continue
                if S[ny][nx] == "o" and prev != dir:
                    continue
                if S[ny][nx] == "x" and prev == dir:
                    continue

                costs[dy][dx][dir] = costs[ny][nx][prev] + 1
                q.append([dy, dx, dir])

# 経路復元(S[i][j][])
ans = []
