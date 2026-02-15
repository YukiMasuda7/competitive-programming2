import bisect

N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = bisect.bisect_left(A, X) + 1
print(ans)
