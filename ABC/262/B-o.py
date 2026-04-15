N, M = map(int, input().split())
edges = [[False] * N for _ in range(N)]
for i in range(M):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    edges[U][V] = True
    edges[V][U] = True
ans = 0
for a in range(N - 2):
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N):
            if edges[a][b] and edges[b][c] and edges[c][a]:
                ans += 1
print(ans)
