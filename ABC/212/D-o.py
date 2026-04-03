# 明らかにheapq。
# 毎回全ての要素にXiを足すと間に合わないので今まで足された数を管理して
# 取り出す時にそれを足した数を出力する。
# 追加の時に今まで足されたの際に今まで足された数だけ引いた数をheappushしておけば、
# heapq内での要素同士の差は正しく管理できるi

import heapq

Q = int(input())
q = []
add = 0
for _ in range(Q):
    X = list(map(int, input().split()))
    if X[0] == 1:
        heapq.heappush(q, X[1] - add)
    elif X[0] == 2:
        add += X[1]
    else:
        print(heapq.heappop(q) + add)
