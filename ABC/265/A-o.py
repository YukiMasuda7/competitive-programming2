X, Y, N = map(int, input().split())
if X <= Y / 3:
    ans = X * N
else:
    n = N - (N // 3) * 3
    ans = Y * (N // 3) + X * n
print(ans)
