# 貪欲法でいい？1gあたりの美味しさが大きいのから消費していけばいい

N, W = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]
cheese.sort(reverse=True)
ans = 0
for i in range(N):
    if cheese[i][1] <= W:
        W -= cheese[i][1]
        ans += cheese[i][0] * cheese[i][1]
    else:
        ans += cheese[i][0] * W
        W = 0
print(ans)
