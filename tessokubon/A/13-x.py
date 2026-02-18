# 尺取り法

N, K = map(int, input().split())
A = list(map(int, input().split()))
# 右端の限界位置を格納する
R = [None] * N

for i in range(N - 1):
    # 右端のスタート地点を決める
    if i == 0:
        R[i] = 0
    else:
        R[i] = R[i - 1]

    while R[i] < N - 1 and A[R[i] + 1] - A[i] <= K:
        R[i] += 1

ans = 0
for i in range(N - 1):
    ans += R[i] - i
print(ans)
