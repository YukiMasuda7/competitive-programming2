N = int(input())
cost = []
for i in range(N - 1):
    C = list(map(int, input().split()))
    cost.append(C)

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            cost1 = cost[i][j - i - 1] + cost[j][k - j - 1]
            cost2 = cost[i][k - i - 1]
            if cost1 < cost2:
                print("Yes")
                exit()
print("No")
