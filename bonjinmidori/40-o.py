# ベクトル(x,y)をθ回転すると
# (x', y') = (xcosθ−ysinθ, xsinθ+ycosθ)になる


# import math
# theta = 2 * math.pi / θ
# s = math.sin(theta)
# c = math.cos(theta)

# 与えられた2点から中点がわかる
# 中点からp0へのベクトルを(1/N)rad回転させれば
# 中点からp1へのベクトルがもとまる
import math

N = int(input())
x, y = map(int, input().split())
xx, yy = map(int, input().split())
mx = (x + xx) / 2
my = (y + yy) / 2

dx = x - mx
dy = y - my

theta = 2 * math.pi / N
s = math.sin(theta)
c = math.cos(theta)

nx = dx * c - dy * s
ny = dx * s + dy * c

ans = [mx + nx, my + ny]
print(*ans)
