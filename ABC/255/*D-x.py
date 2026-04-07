# ただシミュレーションするだけではO(NQ)で間に合わない
# Aを並び替えても結果は変わらない
# A内でのXの位置を二分探索して見つける

# A[0] <= A[1] <= ... <= A[k] <= X <= A[k+1] ...に対して
# ans = Σ(X-A[a]) + Σ(A[b]-X) (0 <= a <= k-1, k <= b <= N-1)
# 左は k*X - ΣA[a], 右は ΣA[b] - (N-k)*X
# ΣA[i]はAの累積和から求められる

import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * N
S[0] = A[0]
for i in range(1, N):
    S[i] = S[i - 1] + A[i]
for i in range(Q):
    X = int(input())
    pos = bisect.bisect_left(A, X)
    if pos == N - 1:
        ans = N * X + S[N - 1]
    elif pos == 0:
        ans = N * X + S[N - 1]
