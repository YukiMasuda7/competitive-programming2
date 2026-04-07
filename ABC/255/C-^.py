# Dの正負で最大値と最小値の式が反対になることに注意
# Xに1ずつ足していっても十分間に合う

X, A, D, N = map(int, input().split())
if D > 0:
    m = A
    M = A + D * (N - 1)
else:
    m = A + D * (N - 1)
    M = A

if X <= m:
    print(m - X)
elif M <= X:
    print(X - M)
else:
    plus = X
    minus = X
    # +を試す
    for i in range(10**6 + 1):
        if (plus + i - A) % D == 0:
            ans = i
            break
    # -を試す
    for i in range(10**6 + 1):
        if (minus - i - A) % D == 0:
            ans = min(ans, i)
            break
    print(ans)
