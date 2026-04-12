T, X = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for i in range(T + 1):
    if i == 0:
        ans.append([i, A[i]])
        now = A[0]
    else:
        if abs(now - A[i]) >= X:
            ans.append([i, A[i]])
            now = A[i]
for a in ans:
    print(*a)
