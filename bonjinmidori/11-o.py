N, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]
X.sort()

now = 0
for i in range(N):
    if K - (X[i][0] - now) >= 0:
        K -= X[i][0] - now
        now = X[i][0]
        K += X[i][1]
    else:
        break
print(now + K)
