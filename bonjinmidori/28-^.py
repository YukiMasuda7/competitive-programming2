# H,W<6なのでH,Wそれぞれにbit全探索しても間に合う
# 2次元配列のコピーは深いコピーcopy.deepcopy出ないと正しくコピーされない
import copy

H, W, K = map(int, input().split())
G = [list(input()) for _ in range(H)]
ans = 0
for i in range(1 << H):
    for j in range(1 << W):
        cnt = 0
        g = copy.deepcopy(G)
        for shifth in range(H):
            if i >> shifth & 1:
                for x in range(W):
                    g[shifth][x] = "*"
            for shiftw in range(W):
                if j >> shiftw & 1:
                    for x in range(H):
                        g[x][shiftw] = "*"

        for a in range(H):
            for b in range(W):
                if g[a][b] == "#":
                    cnt += 1
        if cnt == K:
            ans += 1
print(ans)
