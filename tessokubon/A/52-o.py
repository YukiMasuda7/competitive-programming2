from collections import deque

d = deque()
Q = int(input())
for i in range(Q):
    q = list(map(str, input().split()))

    if q[0] == "1":
        d.append(q[1])
    elif q[0] == "2":
        print(d[0])
    else:
        d.popleft()
