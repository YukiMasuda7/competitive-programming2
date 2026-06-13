N = int(input())
x_sort = []
y_sort = []
isOK = [True] * N
for i in range(N):
    X, Y = map(int, input().split())
    x_sort.append([X - 1, Y - 1, i])
    y_sort.append([Y - 1, X - 1, i])

x_sort.sort()
y_sort.sort()
x_min = x_sort[0][1]
y_min = y_sort[0][1]

for i in range(1, N):
    if x_sort[i][1] > x_min:
        isOK[x_sort[i][2]] = False
    else:
        x_min = x_sort[i][1]

    if y_sort[i][1] > y_min:
        isOK[y_sort[i][2]] = False
    else:
        y_min = y_sort[i][1]

ans = 0
for i in range(N):
    if isOK[i]:
        ans += 1
print(ans)
