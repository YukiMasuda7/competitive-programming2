H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
row_sum = [0] * H
col_sum = [0] * W
for i in range(H):
    for j in range(W):
        row_sum[i] += A[i][j]
        col_sum[j] += A[i][j]

ans = [[0] * W for i in range(H)]
for i in range(H):
    for j in range(W):
        ans[i][j] = row_sum[i] + col_sum[j] - A[i][j]
for a in ans:
    print(*a)
