N, Q = map(int, input().split())
cnt = [0] * (N + 1)
cnt2 = [0] * (10**6)
delete = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        cnt[q[1]] += 1
        cnt2[cnt[q[1]]] += 1
        if cnt2[delete + 1] == N:
            delete += 1
    else:
        print(cnt2[q[1] + delete])
