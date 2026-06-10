# 明らかに尺取り法
# ループするからあらかじめ大きさを2倍にしておく
N = int(input())
A = list(map(int, input().split()))
K = sum(A) / 10
A = 2 * A
S = [0] * (2 * N)

if K != int(K):
    print("No")
    exit()

for i in range(2 * N):
    if i == 0:
        S[i] = A[i]
    else:
        S[i] = S[i - 1] + A[i]

R = [0] * (2 * N)
flag = False
for i in range(N):
    l = i

    if i == 0:
        R[i] = 0
    else:
        R[i] = R[i - 1]

    while l <= N - 1 and R[i] < 2 * N and S[R[i] + 1] - S[l] < K:
        R[i] += 1

    if S[R[i] + 1] - S[l] == K:
        flag = True
        break

if flag:
    print("Yes")
else:
    print("No")
