from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
r = 0
cnt = 0
ans = 0

for l in range(N):
    while r < N:
        x = A[r]
        if d[x] == 0 and cnt == K:
            break
        if d[x] == 0:
            cnt += 1
        d[x] += 1
        r += 1

    ans = max(ans, r - l)

    y = A[l]
    d[y] -= 1
    if d[y] == 0:
        cnt -= 1

print(ans)
