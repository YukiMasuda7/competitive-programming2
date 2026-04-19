import math

T = int(input())
L, X, Y = map(int, input().split())
w = 2 * math.pi / T


def y(t):
    return -L / 2 * math.sin(w * t)


def z(t):
    return L / 2 - L / 2 * math.cos(w * t)


Q = int(input())
for i in range(Q):
    E = int(input())
    dxy = math.sqrt(X**2 + (Y - y(E)) ** 2)
    dz = z(E)
    if dxy == 0:
        ans = 0
    else:
        ans = math.atan(dz / dxy)
        ans = math.degrees(ans)
    print(ans)
