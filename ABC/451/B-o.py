N, M = map(int, input().split())
now = [0] * M
next = [0] * M
for i in range(N):
    a, b = map(int, input().split())
    now[a - 1] += 1
    next[b - 1] += 1
for i in range(M):
    print(next[i] - now[i])
