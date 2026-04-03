# 「全てのクエリに対する K の総和は 4×10**5以下」に注意
# for _ in range(Q):
#     for _ in range(K):
# の計算量が4*10**5で済むということ
# forの中でheappop,heappushを回してもO(1)なので間に合う
# heappopで最小のうち,B削除対象でないものが答え

# 配列の要素のindex管理の方法
# -> (A[index], index)に直しておく

import heapq

N, Q = map(int, input().split())
A = list(map(int, input().split()))
C = []
for i in range(N):
    C.append((A[i], i + 1))
C.sort()
for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    B = set(B)
    i = 0
    ans = 10**10
    while True:
        if not C[i][1] in B:
            ans = C[i][0]
            break
        i += 1
    print(ans)
