# 毎回1本しか追加しないので
# 全体で高々Q本の削除しか行わない
# 切る時に最小の方から消していけば良い -> heapq

import heapq

Q = int(input())

trees = []
heapq.heapify(trees)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heapq.heappush(trees, q[1])
    else:
        while trees and trees[0] <= q[1]:
            heapq.heappop(trees)
    print(len(trees))
