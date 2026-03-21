H, W, Q = map(int, input().split())
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        print(q[1] * W)
        H -= q[1]
    else:
        print(q[1] * H)
        W -= q[1]
