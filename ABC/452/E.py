# 全て1_indexで進める

# Σの順番を入れ替えるとmodが固定されるので楽
mod = 998244353
N, M = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

# A[i]*iを計算しておく
AA = 0
for i in range(1, N + 1):
    AA += A[i] * i % mod
    AA %= mod
print(3 % 1)
# AAA[i]はAA%iをあらかじめ計算したもの
AAA = [0] * (M + 1)
for i in range(1, M + 1):
    AAA[i] = (AA % i) % mod
print(AAA)
ans = 0
for i in range(1, M + 1):
    ans += B[i] * AAA[i] % mod
    ans %= mod
print(ans)
