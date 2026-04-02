# 二分探索ではない？
# 毎回、追加とソートしてたら間に合わない
# 毎回削除は間に合わない→切られた数を管理？
# キュー
import bisect
Q=int(input())
trees=[]
cut=[]
for q in range(Q):
    q=list(map(int,input().split()))
    if q[0]==1:
        trees.append(q[1])
    else:
        cut.append(q[1])

now=0
next_cut=q[0]
for q in range(Q):
    q=list(map(int,input().split()))
    if q[0]==1:
        trees.append(q[1])
    else:
        cut.append(q[1])