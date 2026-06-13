N = int(input())
ans = [[] for _ in range(N)]
for i in range(N):
    X = list(map(int, input().split()))
    M = X[0]
    for j in range(M):
        ans[X[j + 1] - 1].append(i + 1)

for a in ans:
    a = [len(a)] + a
    print(*a)
