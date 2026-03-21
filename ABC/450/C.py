# 各点をスタートとするBFSをする
# グリッドから出たら数えず終わり
# そのスタートがもう数えたものであるかはboolで管理
from collections import deque

dir = [(0, 1), (-1, 0), (0, -1), (1, 0)]

H, W = map(int, input().split())
G = []
for i in range(H):
    s = input()
    s = list(s)
    G.append(s)
ans = 0
visited = [[False] * W for _ in range(H)]


for i in range(H):
    for j in range(W):
        flag=True
        if G[i][j]=="." and visited[i][j]==False:
            q=deque()
            q.append((i,j))
            while q and flag:
                now =q.popleft()
                visited[now[0]][now[1]]=True

                for d in dir:
                    if not(0<=i+d[0]<H and 0<=j+d[1]<W):
                        flag=False
                        break


