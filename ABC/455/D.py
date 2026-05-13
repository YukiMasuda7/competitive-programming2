from collections import deque

N, Q = map(int, input().split())
pile = [deque([i]) for i in range(N)]
d = {}
for i in range(N):
    d[i] = i
for i in range(Q):
    C, P = map(int, input().split())
    C -= 1
    P -= 1
    # 対象のカードがあるパイルのインデックス
    c = d[C]
    p = d[P]

    tmp = deque([])
    while True:
        x = pile[c].pop()
        d[x] = d[p]
        tmp.append(x)
        if x == C:
            while tmp:
                y = tmp.pop()
                pile[p].append(y)
            break
ans = [0] * N
for i in range(N):
    ans[i] = len(pile[i])
print(*ans)
