# 上界を考える。問題の固有の設定に注目する。

# dpっぽいな（やっぱ無理）
# 貪欲法で良いかも？

# ->A[i]-B[i], B[i](1回あたりに得られる点数)を全て出してからソート
# 条件よりB[i]>A[i]-B[i]なので、満点が部分点より先に選ばれることはない

N, K = map(int, input().split())
scores = []
for i in range(N):
    A, B = map(int, input().split())
    scores.append(B)
    scores.append(A - B)
scores.sort(reverse=True)
ans = sum(scores[:K])
print(ans)
