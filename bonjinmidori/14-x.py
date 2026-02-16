# N<10**2なので全探索O(N**3)で十分間に合う

# 3点が同一直線上にあるか判定したい
# 傾きは切り捨て誤差の関係上使えない
# (x1, y1),(x2, y2)を通る直線の式は
# y - y1 = ((y2 -y1) / (x2 - x1)) * (x - x1)
# つまり(y - y1) * (x2 - x1) = (y2 - y1) * (x -x1)
# この式が(x , y) = (x3, y3)で成り立てば3点は同一直線上

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
for i in range(N - 2):
    x1 = points[i][0]
    y1 = points[i][1]
    for j in range(i + 1, N - 1):
        x2 = points[j][0]
        y2 = points[j][1]
        for k in range(j + 1, N):
            x3 = points[k][0]
            y3 = points[k][1]

            if (y3 - y1) * (x2 - x1) == (y2 - y1) * (x3 - x1):
                print("Yes")
                exit()
print("No")
