# 1. 一番大きいのが分裂していないパターン -> 一番大きいのがL
# 2. 分裂しているパターン -> 一番大きい ＋ 一番小さい = L(?)
# つまりLは１個か２個しかない？

N = int(input())
A = list(map(int, input().split()))
AA = A.copy()
A.sort()
AA.sort()
m = min(A)
M = max(A)
S = sum(A)

ans = []

# 1のパターン
if S % M == 0:
    A = [x for x in A if x != M]
    if len(A) % 2 == 0:
        flag = True
        for i in range(len(A) // 2):
            if A[i] + A[-(i + 1)] != M:
                flag = False
        if flag:
            ans.append(M)

# 2のパターン
X = M + m
if S % X == 0:
    AA = [x for x in AA if x != X]
    if len(AA) % 2 == 0:
        flag = True
        for i in range(len(AA) // 2):
            if AA[i] + AA[-(i + 1)] != X:
                flag = False
        if flag:
            ans.append(X)
print(*ans)
