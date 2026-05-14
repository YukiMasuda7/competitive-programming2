# 単純に計算すると6**Nで間に合わない
mod = 10**9 + 7
N = int(input())
S = [0] * N
for i in range(N):
    A = list(map(int, input().split()))
    S[i] = sum(A) % mod
ans = 1
for i in range(N):
    ans *= S[i]
    ans %= mod
print(ans)
