#imos法

# 区間加算や区間更新を高速に処理するための「差分配列」テクニック。
# 区間の始点に+1、終点+1に-1をして、
# 累積和を取ることで区間ごとの値を一括で求める。
# 主に「区間加算」「区間カウント」などで使う。


# 鉄則A-7
D = int(input())
N = int(input())
A = [0] * (D + 2)
for i in range(N):
    L, R = map(int, input().split())
    A[L] += 1
    A[R + 1] -= 1

S = [0] * (D + 2)
for i in range(D + 1):
    S[i + 1] = S[i] + A[i + 1]

for i in range(1, D + 1):
    print(S[i])