# dfsを全てのkに対して回すとO(N*(頂点の＋辺の数))で間に合わない
# 木の単純パスが一意に定まるので途中で被りがあるならそれ以降も被りあり

# 被りが生じているかをdupフラグで管理
# 再帰関数の実行のされ方に注意dupはdfsごとに他に影響されない異なる値を持てる。
# ↓
# 実行スタックの上の方が実行され尽くしてそのdfsに戻ってきた時に(if cnt >= 1: 以下が実行されるときに)
# 以前割り当てられたdupがdfsごとに保存されている

import sys

sys.setrecursionlimit(10**7)


def dfs(cnt: int, now: int):
    visited[now] = True

    dup = 0
    if A[now] in nums:
        dup = 1
    else:
        nums.add(A[now])

    cnt += dup
    ans[now] = cnt > 0

    for to in edges[now]:
        if not visited[to]:
            dfs(cnt, to)

    # このノードでnumsに追加しているならnumsから値を削除する
    if dup == 0:
        nums.remove(A[now])


N = int(input())
A = list(map(int, input().split()))
edges = [[] for _ in range(N)]
cnt = 0
visited = [False] * N
nums = set()
ans = [False] * N
for i in range(N - 1):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    edges[U].append(V)
    edges[V].append(U)

dfs(cnt, 0)
for a in ans:
    if a:
        print("Yes")
    else:
        print("No")
