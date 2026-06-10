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
l = len(prime_factorize(N))
for i in range(40):
    if 2**i >= l:
        ans = i
        break
print(ans)
