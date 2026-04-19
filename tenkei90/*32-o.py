# 全パターンを探索しても10!=3.6*10**6
from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dislike = [set() for _ in range(N)]
M = int(input())
for i in range(M):
    X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    dislike[X].add(Y)
    dislike[Y].add(X)
ans = 10**10
P = permutations(range(N))
for p in P:
    tmp = A[p[0]][0]
    cnt = 1
    for i in range(1, N):
        if p[i - 1] in dislike[p[i]]:
            break
        tmp += A[p[i]][i]
        cnt += 1

    if cnt == N:
        ans = min(ans, tmp)
if ans != 10**10:
    print(ans)
else:
    print(-1)
