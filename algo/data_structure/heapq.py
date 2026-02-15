# 優先度付きキュー
# 最小の要素を取得、削除できる
# 追加 -> heapq.heappush(T,x)
# T[0]が最小の値
# 最小値の取得 -> heapq.heappop(T)

import heapq

T = []
Q = int(input())
for i in range(Q):
    q = list(map(str, input().split()))

    if q[0] == "1":
        heapq.heappush(T, int(q[1]))
    elif q[0] == "2":
        print(T[0])
    else:
        heapq.heappop(T)
