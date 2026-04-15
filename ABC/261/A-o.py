L1, R1, L2, R2 = map(int, input().split())
X = [0] * 102
X[L1] += 1
X[R1 + 1] -= 1
X[L2] += 1
X[R2 + 1] -= 1
S = [0] * 102
S[0] = X[0]
for i in range(1, 101):
    S[i] = S[i - 1] + X[i]
cnt = 0
for i in range(101):
    if S[i] == 2:
        cnt += 1
ans = max(0, cnt - 1)
print(ans)
