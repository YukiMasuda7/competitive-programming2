N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + A[i]
for i in range(Q):
    L, R = map(int, input().split())
    ans = S[R] - S[L - 1]
    print(ans)
