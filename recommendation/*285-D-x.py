# グラフのサイクル判定
# ->dfs, bfs, unionfind

# グラフにループが一つでもあったら"No"
# (ただし始点をすべての試すとO(N**2)なのでvisitedを管理して訪れた場所は無視する)
# (S,Tそれぞれにに被りのない)"有向グラフの"連結判定
# -> 始点に戻ってきたらループ

# 始点を全探索した場合、O(N*(V+E))[今回はO(N**2)]になるけど始点の全探索の時点で
# その始点を一度訪れているならスキップするようにすれば各ノード1度までしか訪れないので間に合うO(N)


import sys

sys.setrecursionlimit(10**7)

N = int(input())
edges = {}
visited = {}
for i in range(N):
    S, T = map(str, input().split())
    edges[S] = T
    visited[S] = False


def isConnected(start, now):
    visited[now] = True

    to = edges[now]
    if to not in edges:
        return False
    if to == start:
        return True

    return isConnected(start, to)


for d in edges:
    if visited[d]:
        continue
    if isConnected(d, d):
        print("No")
        exit()
print("Yes")
