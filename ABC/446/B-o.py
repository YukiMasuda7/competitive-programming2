N, M = map(int, input().split())
lists = []
used = [False] * (M + 1)
ans = [0] * N
for i in range(N):
    L = int(input())
    X = list(map(int, input().split()))
    for j in range(L):
        if not used[X[j]]:
            used[X[j]] = True
            ans[i] = X[j]
            break
        else:
            continue
for a in ans:
    print(a)
