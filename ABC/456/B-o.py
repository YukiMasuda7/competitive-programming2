from collections import defaultdict

A = [list(map(int, input().split())) for _ in range(3)]
d = [defaultdict(int), defaultdict(int), defaultdict(int)]
for i in range(3):
    for j in range(6):
        d[i][A[i][j]] += 1

x = (
    d[0][4] * d[1][5] * d[2][6]
    + d[1][4] * d[2][5] * d[0][6]
    + d[2][4] * d[0][5] * d[1][6]
    + d[0][4] * d[1][6] * d[2][5]
    + d[1][4] * d[2][6] * d[0][5]
    + d[2][4] * d[0][6] * d[1][5]
)
ans = x / 216
print(ans)
