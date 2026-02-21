# 高い商品に多くの割引券を使った方が安くなる
# どの順番で買っていっても答えは変わらない
# 現時点で一番高い商品に割引券を使うを繰り返せばいい
# maxを高速で出したい -> heapq

# 1より小さい数は2で割っても切り捨てられるだけなので
# int(x/2)をK回するのとint(/2**K)は変わらない

# //と/からのint化では負の数に対する挙動が違う
# -5 // 2 → -3（-2.5を小さい方に切り捨てて-3）
# int(-5 / 2) → int(-2.5) → -2（0方向に切り捨て）


import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    A[i] *= -1
heapq.heapify(A)
for _ in range(M):
    M = heapq.heappop(A)
    M /= 2
    M = int(M)
    heapq.heappush(A, M)

for i in range(N):
    A[i] = -A[i]
ans = sum(A)
print(ans)
