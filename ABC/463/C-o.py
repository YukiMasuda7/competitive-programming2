# 優先度付きキュー？
# 二分探索でいけるはず
import bisect

N = int(input())
l = []
h = []
for i in range(N):
    H, L = map(int, input().split())
    l.append(L)
    h.append(H)
S = [-1] * (N + 1)
for i in range(N - 1, -1, -1):
    S[i] = max(h[i], S[i + 1])

Q = int(input())
T = list(map(int, input().split()))

for i in range(Q):
    t = T[i]
    ind = bisect.bisect_right(l, t)
    if ind == N:
        print(0)
    else:
        print(S[ind])
