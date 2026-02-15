# 10進法->8進法の関数を定義
def f(N):
    q = N
    result = []
    while q >= 8:
        r = q % 8
        q //= 8
        result.append(str(r))
    result.append(str(q))
    result = result[::-1]
    return int("".join(result))


N = int(input())
ans = 0
for i in range(1, N + 1):
    if "7" not in str(i) and "7" not in str(f(i)):
        ans += 1
print(ans)
