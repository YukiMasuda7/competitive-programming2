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
