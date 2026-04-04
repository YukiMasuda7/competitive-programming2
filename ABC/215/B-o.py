N = int(input())
ans = -1
for i in range(60):
    if 2**i <= N:
        ans = max(ans, i)
print(ans)
