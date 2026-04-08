N = int(input())
A = list(map(int, input().split()))
pos = [0] * N
for i in range(N):
    for j in range(i, N):
        pos[i] += A[j]
ans = 0
for p in pos:
    if p >= 4:
        ans += 1
print(ans)
