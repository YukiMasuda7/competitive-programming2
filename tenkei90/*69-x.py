# a**b(mod m)をpowを使って高速に求める
mod = 10**9 + 7
N, K = map(int, input().split())
if N == 1:
    ans = K
    ans %= mod
elif N == 2:
    ans = K * (K - 1)
    ans %= mod
else:
    tmp = K * (K - 1)
    tmp %= mod
    tmp2 = pow(K - 2, N - 2, mod)
    ans = tmp * tmp2
    ans %= mod
print(ans)
