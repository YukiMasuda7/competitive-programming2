# 貪欲法?
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
cnt = 0
for i in range(H - 1):
    for j in range(W - 1):
        if A[i][j] != B[i][j]:
            x = B[i][j] - A[i][j]
            A[i][j] += x
            A[i + 1][j] += x
            A[i][j + 1] += x
            A[i + 1][j + 1] += x
            cnt += abs(x)
flag = True
for i in range(H):
    for j in range(W):
        if A[i][j] != B[i][j]:
            flag = False

if flag:
    print("Yes")
    print(cnt)
else:
    print("No")
