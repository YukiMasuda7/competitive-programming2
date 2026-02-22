# 重み付き最短経路問題 -> ダイクストラ
import heapq

inf = 10**20

N, M, X, Y = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for i in range(M):
    A, B, T, K = map(int, input().split())
    edges[A].append((B, T, K))
    edges[B].append((A, T, K))

decide = [False] * (N + 1)
time = [inf] * (N + 1)
time[X] = 0
q = []
# pushタプルの第一引数はtime -> 未確定の最小コストのノードから決定するため
# if not decide[now[1]]: のcontinueがないとTLEになる
heapq.heappush(q, (time[X], X))

while q:
    now = heapq.heappop(q)
    if not decide[now[1]]:
        decide[now[1]] = True
    else:
        continue
    for to in edges[now[1]]:
        if not decide[to[0]]:
            if now[0] % to[2] == 0:
                t = 0
            else:
                t = to[2] - now[0] % to[2]
            if time[to[0]] > now[0] + to[1] + t:
                time[to[0]] = now[0] + to[1] + t
                heapq.heappush(q, (time[to[0]], to[0]))

if time[Y] != inf:
    print(time[Y])
else:
    print(-1)
