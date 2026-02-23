N, X = map(int, input().split())
A = [0] + list(map(int, input().split()))
now = X
know = [False] * (N + 1)
ans = 1
know[now] = True
while not know[A[now]]:
    ans += 1
    know[A[now]] = True
    now = A[now]
print(ans)
