N, M = map(int, input().split())
C = [0] + list(map(int, input().split()))
pepper = [0] * (M + 1)
for i in range(N):
    A, B = map(int, input().split())
    pepper[A] += B
ans = 0
for i in range(M + 1):
    ans += min(C[i], pepper[i])
print(ans)
