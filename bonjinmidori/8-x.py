# 一気に書かず、関数ごとに分割するのが良い
# "00234"のint化は234になる(0は自動的にきえる)
def g1(x):
    x = str(x)
    x = list(x)
    x.sort(reverse=True)
    x = "".join(x)
    return int(x)


def g2(x):
    x = str(x)
    x = list(x)
    x.sort()
    x = "".join(x)
    return int(x)


def f(x):
    return g1(x) - g2(x)


N, K = map(int, input().split())
for _ in range(K):
    N = f(N)
print(N)
