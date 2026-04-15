N = int(input())
P = list(map(int, input().split()))
now = N
ans = 0
while now > 1:
    now = P[now - 2]
    ans += 1
print(ans)
