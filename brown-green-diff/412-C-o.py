# S1より小さく、SNより大きいドミノは無視していい
import bisect

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    if S[0] > S[N - 1]:
        print(2)
        continue
    s = S[0]
    g = S[N - 1]
    S.sort()
    U = [s]
    l = 1
    for j in range(N):
        if s < S[j] < g:
            U.append(S[j])
            l += 1
    U.append(g)
    l += 1

    # 倒せるコマのうち最大のものを二分探索で探していくそれがgに到達するまで繰り返す
    now = 0
    ans = 1
    flag = False
    while now < l - 1:
        prev = now
        now = bisect.bisect_right(U, U[now] * 2) - 1
        ans += 1
        if now == prev:
            flag = True
            break
    if flag:
        print(-1)
    else:
        print(ans)
