# 全探索O(N**2)では間に合わない
# S=ΣAiとする
# ΣΣAi*Aj = Σ(Ai*(S-(A0+A1+A2+...+Ai)))でかける
# こまめにmodで割ってオーバーフローを防ぐ

N = int(input())
A = list(map(int, input().split()))
mod = 10**9 + 7
S = sum(A) % mod
ans = 0
for i in range(N):
    S = (S - A[i]) % mod
    x = A[i] * S % mod
    ans = (ans + x) % mod
print(ans)
