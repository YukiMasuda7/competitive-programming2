N = int(input())
SA = [0] * (N + 1)
SB = [0] * (N + 1)
for i in range(N):
    C, P = map(int, input().split())
    if C == 1:
        SA[i + 1] = P
    else:
        SB[i + 1] = P
for i in range(1, N + 1):
    SA[i] += SA[i - 1]
    SB[i] += SB[i - 1]
Q = int(input())
for i in range(Q):
    L, R = map(int, input().split())
    ans1 = SA[R] - SA[L - 1]
    ans2 = SB[R] - SB[L - 1]
    print(ans1, ans2)
