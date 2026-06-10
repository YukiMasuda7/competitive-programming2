N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(N):
    A[i] *= 2
A.sort(reverse=True)
B.sort(reverse=True)
l = min(M, N)
ans = 0
j = 0
for i in range(M):
    if j < N:
        if A[j] >= B[i]:
            ans += 1
            j += 1
print(ans)
