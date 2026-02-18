# 隣接リストを作る(無向 or 双方向限定はリストで十分)
# 有向グラフは行列じゃないと無理

N, M = map(int, input().split())
ans = [[] for _ in range(N + 1)]
for i in range(M):
    A, B = map(int, input().split())
    ans[A].append(str(B))
    ans[B].append(str(A))
for i in range(1, N + 1):
    print(str(i) + ": " + "{" + ", ".join(ans[i]) + "}")
