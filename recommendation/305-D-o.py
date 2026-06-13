# l,rに対して二分探索？
# 内側の区間の睡眠は累積和から出る?
import bisect

N = int(input())
A = list(map(int, input().split()))
S = [0] * N
for i in range(2, N):
    if i % 2 == 0:
        S[i] = A[i] - A[i - 1] + S[i - 2]
    else:
        S[i] = S[i - 1]
Q = int(input())
for i in range(Q):
    ans = 0
    l, r = map(int, input().split())
    ll = bisect.bisect_right(A, l)
    rr = bisect.bisect_left(A, r)

    if ll == rr and ll % 2 == 0:
        ans += r - l
    else:
        if ll % 2 == 0:
            ans += A[ll] - l
            ll += 1
        if rr % 2 == 0:
            ans += r - A[rr - 1]
            rr -= 1
        ans += S[rr] - S[ll]
    print(ans)
