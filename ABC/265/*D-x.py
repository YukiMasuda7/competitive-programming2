# xを全探索
# 累積和を考える
# S[y]-S[x]=P。つまりS[y]=S[x]+PとなるS[y]を二分探索で探す
# あとも同様
import bisect

N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (N + 1)
for i in range(1, N + 1):
    S[i] = S[i - 1] + A[i - 1]
print(S)
