# 人iが照らされるのに必要な最小の明かりの強さは、
# 人iから最も近い明かりを持っている人との距離に等しい。

# 明かりを持っている人は必ず照らされるので、明かりを持っていない人全員に対して↑を行う
# その最大値が答え
# N<=10**3なのでO(N**2)でも間に合う

N, K = map(int, input().split())
A = list(map(int, input().split()))
P = [list(map(int, input().split())) for _ in range(N)]
A = set(A)
ans = -1
for i in range(N):
    if i + 1 in A:
        continue
    d = 10**10
    for j in range(N):
        if j == i or j + 1 not in A:
            continue
        d = min(d, ((P[i][0] - P[j][0]) ** 2 + (P[i][1] - P[j][1]) ** 2) ** 0.5)
    ans = max(ans, d)
print(ans)
