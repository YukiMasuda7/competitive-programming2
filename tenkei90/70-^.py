# 各点との絶対的な距離が最小->中央値
# x, yそれぞれの中央値になるように座標をおけばいい

# マンハッタン距離
# abs(x1 - x2) + abs(y1 - y2)

N = int(input())
x = []
y = []
for i in range(N):
    A, B = map(int, input().split())
    x.append(A)
    y.append(B)
x = sorted(x)
y = sorted(y)
if N % 2 == 0:
    mx = (x[N // 2 - 1] + x[N // 2]) / 2
    my = (y[N // 2 - 1] + y[N // 2]) / 2
else:
    mx = x[N // 2]
    my = y[N // 2]
ans = 0
for i in range(N):
    ans += abs(x[i] - mx) + abs(y[i] - my)
print(int(ans))
