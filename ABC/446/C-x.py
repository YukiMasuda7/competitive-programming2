T = int(input())
for i in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = [0] + A
    B = [0] + B
    # N-D日目までの数
    a = sum(A[1 : N - D + 1])
    b = sum(B[1 : N - D + 1])
    # N - D + 1日以降
    aa = sum(A[N - D + 1 :])
    bb = sum(B[N - D + 1 :])
    leave = a - b - bb
    if leave >= 0:
        ans = aa
    else:
        ans = aa + leave
    print(a, b, aa, bb, ans)
    print(ans)
