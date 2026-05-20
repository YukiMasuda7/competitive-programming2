# 8進数→9進数は難しいので10進数を経由したい
def f(N):
    N = str(N)
    ans = 0
    for i in range(len(N)):
        ans += int(N[len(N) - 1 - i]) * 8**i
    return ans


def g(N):
    q = N
    result = []
    while q >= 9:
        r = q % 9
        q //= 9
        result.append(str(r))
    result.append(str(q))
    result = result[::-1]
    return int("".join(result))


N, K = map(int, input().split())
for i in range(K):
    N = f(N)
    N = g(N)
    N = list(str(N))
    for i in range(len(N)):
        if N[i] == "8":
            N[i] = "5"
    N = int("".join(N))
print(N)
