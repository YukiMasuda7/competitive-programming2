N, K = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(N)]
Total = [(sum(scores[i]), i + 1) for i in range(N)]
Total.sort(reverse=True)
ans = [False] * (N + 1)
for i in range(N):
    if i <= K - 1:
        ans[Total[i][1]] = True
    else:
        if Total[i][0] + 300 >= Total[K - 1][0]:
            ans[Total[i][1]] = True
        else:
            ans[Total[i][1]] = False

for i in range(1, N + 1):
    if ans[i]:
        print("Yes")
    else:
        print("No")
