# 1/p + 2/p + ... + p/p = (p+1)/2なので
# 1からpまでの目を持つサイコロの目の期待値は(p+1)/2
# よってa番目からb番目までのサイコロの目の期待値の和は
# (pa+1)/2 + (p(a+1)+1)/2 + ... + (pb+1)/2
# =　(pa + p(a+1) + ... + pb + b - a + 1)　/　2

# ↑難しく考えすぎ。
# 区間長がKで固定であることを見落としていた。
# 各サイコロの期待値を出して区間長Kでの区間和でfor文で回せばいい

N, K = map(int, input().split())
P = list(map(int, input().split()))
E = [(P[i] + 1) / 2 for i in range(N)]
S = [0] * (N + 1)
for i in range(N):
    S[i + 1] = S[i] + E[i]
ans = -1
for i in range(N - K + 1):
    ans = max(ans, S[i + K] - S[i])
print(ans)
