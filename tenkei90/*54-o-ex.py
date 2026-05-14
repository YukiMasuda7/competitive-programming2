# ダブリングではなく周期性で解く
# ありうる状態は高々10**5なのでそれ以下の回数のループで遷移している
# vist[bool]で管理してもし一度使った値に遷移したらそこからループだとわかる


def convert(N: int):
    x = N
    S = str(N)
    S = list(S)
    y = 0
    for s in S:
        y += int(s)
    z = (x + y) % 10**5
    return z


N, K = map(int, input().split())
visit = [False] * 10**5
now = N
cnt = 0
loop = [0] * 10**5
while not visit[now]:
    loop[cnt] = now
    visit[now] = True
    now = convert(now)
    cnt += 1
ans = loop[K % cnt]
print(ans)
