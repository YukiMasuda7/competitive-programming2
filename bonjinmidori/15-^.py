# 格桁の和が3なら3の倍数
# 格桁のmodを管理すればよい？->全探索を避けられる

from collections import defaultdict

d = defaultdict(int)
N = int(input())
now = 0
N = list(str(N))
l = len(N)
for n in N:
    n = int(n)
    n %= 3
    d[n] += 1
    now += n
now %= 3

if now == 0:
    print(0)
elif now == 2:
    if d[2] >= 1 and l - 1 > 0:
        print(1)
    elif d[1] >= 2 and l - 2 > 0:
        print(2)
    else:
        print(-1)
else:
    if d[1] >= 1 and l - 1 > 0:
        print(1)
    elif d[2] >= 2 and l - 2 > 0:
        print(2)
    else:
        print(-1)
