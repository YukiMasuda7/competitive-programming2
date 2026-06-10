# 同じ色を選んで良いのはK-M回まで
from collections import defaultdict

N, K, M = map(int, input().split())
jwels = []
for i in range(N):
    C, V = map(int, input().split())
    jwels.append([V, C])
jwels.sort(reverse=True)


d = defaultdict(int)
same_limit = K - M
same = 0
cnt = 0
ans = 0
for i in range(N):
    color = jwels[i][1]
    value = jwels[i][0]
    if cnt == K:
        break
    if d[color] == 0:
        cnt += 1
        ans += value
        d[color] += 1
    else:
        if same < same_limit:
            same += 1
            cnt += 1
            ans += value
            d[color] += 1
        else:
            continue
print(ans)
