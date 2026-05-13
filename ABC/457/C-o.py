import bisect

N, K = map(int, input().split())
L = []
A = [[] for _ in range(N)]
for i in range(N):
    X = list(map(int, input().split()))
    L.append(X[0])
    A[i] = X[1:]
C = list(map(int, input().split()))
K -= 1
cnt = [0] * (N + 1)
for i in range(1, N + 1):
    if i == 1:
        cnt[i] = L[i - 1] * C[i - 1]
    else:
        cnt[i] = cnt[i - 1] + L[i - 1] * C[i - 1]
K_in = bisect.bisect_right(cnt, K)

print(A[K_in - 1][(K - cnt[K_in]) % L[K_in - 1]])

