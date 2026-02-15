# 辞書
Q = int(input())
d = {}
for i in range(Q):
    q = list(map(str, input().split()))
    if q[0] == "1":
        d[q[1]] = q[2]
    else:
        print(d[q[1]])
