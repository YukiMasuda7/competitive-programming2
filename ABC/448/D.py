# 探索の途中で被りがあるなら抜け出す


def dfs(now, goal, edges, visited, num, A):
    visited[now] = True
    num.add(A[now])
    for to in edges[now]:
        if to == goal:
            if A[to] in num:
                return True
            else:
                return False

        if not visited[to]:
            if A[to] in num:
                return True
            else:
                return dfs(to, goal, edges, visited, num, A)


N = int(input())
A = list(map(int, input().split()))
edges = [[] for _ in range(N)]
for i in range(N - 1):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    edges[U].append(V)
    edges[V].append(U)

for goal in range(N):
    visited = [False] * N
    num = set()
    visited[0] = True
    num.add(A[0])
    print(goal, dfs(0, goal, edges, visited, num, A))
    if dfs(0, goal, edges, visited, num, A):
        print("Yes")
    else:
        print("No")
