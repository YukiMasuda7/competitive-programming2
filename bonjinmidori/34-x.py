# まず、Nを素因数分解する
# ある素数pに対してp**1, p**2, p**3, ...で割っていけばいい
# Σi = (1/2) * N * (N + 1)なので
# pがm個ある時
# (1/2) * n * (n + 1) < mを満たす最大のnが答え

# 等比数列の和の公式(初項a, 公比r, 項数n)
# a*r**1 + a*r**2 + ... + a*r**n =
# (1) i = 1の時
# na
# (2) i != 1の時
# a*(r**n - 1) / (r - 1)


def prime_factorize(N):
    if N == 1:
        return [1]
    prime_list = []
    i = 2
    while i * i <= N:
        if N % i == 0:
            prime_list.append(i)
            N //= i
        else:
            i += 1
    if N != 1:
        prime_list.append(N)
    return prime_list


N = int(input())
if N == 1:
    print(0)
    exit()

prime = prime_factorize(N)
prime = set(prime)

ans = 0

for p in prime:
    for e in range(1, 10**10):
        if N % (p**e) == 0:
            ans += 1
            N //= p**e
        else:
            break
print(ans)
