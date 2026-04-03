# 二分探索で近い数字を探せばいい
import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
ans = 10**10
for a in A:
    b = bisect.bisect_left(B, a)
    if b == 0:
        ans = min(ans, abs(a - B[0]))
    elif b == M:
        ans = min(ans, abs(a - B[M - 1]))
    else:
        ans = min(ans, abs(a - B[b]))
        ans = min(ans, abs(a - B[b - 1]))
print(ans)
