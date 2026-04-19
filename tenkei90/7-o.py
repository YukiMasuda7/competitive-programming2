# 二分探索
import bisect

N = int(input())
A = list(map(int, input().split()))
A.sort()
Q = int(input())
for i in range(Q):
    B = int(input())
    ind = bisect.bisect_left(A, B)
    if ind == 0:
        ans = abs(B - A[0])
    elif ind == N:
        ans = abs(B - A[N - 1])
    else:
        ans = min(abs(B - A[ind]), abs(B - A[ind - 1]))
    print(ans)
