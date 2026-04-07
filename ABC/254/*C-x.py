# index=iの要素が動けるのはi+k, i+2k, ...の場所のみ
# 逆にindex= i, i+k, i+2k, .. はその中で自由に並び替えできる

# (i, i+k, i+2k, ...), (i=0, 1, 2, .. k-1)のk個のグループに分けて
# 各々をソートし、それをAに戻した時に、昇順になっていればOK


N, K = map(int, input().split())
A = list(map(int, input().split()))
B = [[] for _ in range(K)]

for i in range(N):
    B[i % K].append(A[i])

for i in range(K):
    B[i].sort()

C = [0] * N
for i in range(K):
    for j in range(len(B[i])):
        C[i + K * j] = B[i][j]
A.sort()
if C == A:
    print("Yes")
else:
    print("No")
