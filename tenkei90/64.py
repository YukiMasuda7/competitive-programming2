# 区間の更新
# 不便さが変わるのは地殻変動の起こる端とその隣だけ
N, Q = map(int, input().split())
A = list(map(int, input().split()))
unsatisfaction = [0] * (N - 1)
ans = 0
for i in range(1, N):
    unsatisfaction[i - 1] = A[i] - A[i - 1]
    ans += A[i] - A[i - 1]
ans = 0
for i in range(Q):
    L, R, V = map(int, input().split())
    L -= 1
    R -= 1
    if L > 0:
        tmp = unsatisfaction[L - 1]
        unsatisfaction[L - 1] = abs(A[L] + V - A[L - 1])
        ans += abs(tmp - unsatisfaction[L - 1])
    if R < N - 1:
        tmp = unsatisfaction[R + 1]
        unsatisfaction[R + 1] = abs(A[R] + V - A[R + 1])
        ans += abs(tmp - unsatisfaction[R + 1])
    print(ans)
