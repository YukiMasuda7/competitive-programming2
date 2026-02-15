N, K = map(int, input().split())
ans = 0
for i in range(N + 1):
    I = str(i)
    I = list(I)
    sum = 0
    for c in I:
        sum += int(c)

    if sum == K:
        ans += 1
print(ans)
