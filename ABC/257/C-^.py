N = int(input())
S = input()
S = list(S)
T = [int(s) for s in S]
W = list(map(int, input().split()))
X = []
for i in range(N):
    X.append([W[i], T[i]])
X.sort()
# ソートされたbool(大人と子供の判定)の累積和を計算しておく
A = [0] * N
A[0] = X[0][1]
for i in range(1, N):
    A[i] = A[i - 1] + X[i][1]

ans = -1
# 子供と大人の境目を全探索
# 境目lの時、子供l人、大人N-l人と予想
# 実際の数は、子供l-A[l-1]人、大人A[N-1]-A[l-1]人
for i in range(N + 1):
    if i == 0:
        tmp = A[N - 1]
    elif i == N:
        tmp = N - A[N - 1]
    else:
        # 同じW1が連続するところでは区切れない
        if X[i - 1][0] != X[i][0]:
            tmp = (i - A[i - 1]) + A[N - 1] - A[i - 1]
    ans = max(ans, tmp)
print(ans)
