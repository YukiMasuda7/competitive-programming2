# Aをソートしたい
# BはAのソート前のインデックスであることに注意

import bisect
from collections import defaultdict

N, Q = map(int, input().split())
A = list(map(int, input().split()))
d = defaultdict(int)
AA = sorted(A)
ind = [0] * N
for i in range(N):
    ind[i] = bisect.bisect_left(AA, A[i]) + d[A[i]]
    d[A[i]] += 1

m = min(A)
for i in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    min = m
    for i in range(K):
        if min == AA[ind[B[i] - 1]]:
            min += 1
    print(min)
