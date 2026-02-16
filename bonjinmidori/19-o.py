X, K, D = map(int, input().split())
cnt = K
if X >= 0:
    cnt -= min(K, X // D)
    X -= D * min(K, X // D)
    if cnt % 2 == 0:
        ans = abs(X)
    else:
        ans = abs(X - D)
else:
    cnt -= min(K, abs(X) // D)
    X += D * min(K, abs(X) // D)
    if cnt % 2 == 0:
        ans = abs(X)
    else:
        ans = X + D
print(ans)
