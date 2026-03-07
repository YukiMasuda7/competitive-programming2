# 計算で一発では解けない
# シミュレーションが必要

# 古い卵から使う -> FIFOだからキューと気付ける
# i日目に追加された卵をキューにiと書いて入れておく

# "各テストケースのNの総和が10**5以下"

# ↑大事

# つまり
# for test in range(T):
#       for i in range(N):
# が10**5以下。

# 先頭を見たい時、
# if q.popleft()==x:
# だと取り出しも行われてしまう
# 取り出したくない時は
# if q[0]==x:

from collections import deque

T = int(input())
for t in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    q = deque()
    for i in range(N):
        for _ in range(A[i]):
            q.append(i)
        for _ in range(B[i]):
            if q:
                q.popleft()
        while q and q[0] == i - D:
            q.popleft()
    print(len(q))
