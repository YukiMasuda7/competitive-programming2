import heapq
from collections import defaultdict

mx = []  # 最大値取得用（負値で管理）
mn = []  # 最小値取得用
cnt = defaultdict(int)

q = int(input())

for _ in range(q):
    query = list(map(int, input().split()))
    t = query[0]

    if t == 1:
        x = query[1]
        cnt[x] += 1
        heapq.heappush(mx, -x)
        heapq.heappush(mn, x)

    elif t == 2:
        x, c = query[1], query[2]
        cnt[x] = max(0, cnt[x] - c)

    else:
        while mx and cnt[-mx[0]] == 0:
            heapq.heappop(mx)
        while mn and cnt[mn[0]] == 0:
            heapq.heappop(mn)
        print(-mx[0] - mn[0])
