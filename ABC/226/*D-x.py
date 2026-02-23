# 同一直線上の街は全て1つの魔法で移動できる
# ../algo/maht/colinearity.pyを参照

# n<500だからO(N**2)は間に合う　-> 全ての点の間の方向ベクトルはわかる
# これを単位ベクトルに直した時一致すれば...
# ↑ (x,y) -> 1 / |(x,y)| (x,y)
# 割り算の誤差で一致しないかも

# 単位ベクトルに直すのではなく,
# x,yをそれぞれgcd(x,y)で割れば、
# x,yがどちらも整数で表せる大きさのみを最小にしたベクトルになる
# 方向は変わらない

import math


def f(a, b, c, d):
    return [a - c, b - d]


magics = set()
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        a = points[i][0]
        b = points[i][1]
        c = points[j][0]
        d = points[j][1]

        x = f(a, b, c, d)[0]
        y = f(a, b, c, d)[1]
        gcd = math.gcd(x, y)
        x //= gcd
        y //= gcd
        magics.add((x, y))


print(len(magics))
