# 凸四角形の判定
# 外積の正負を使う
# https://output-zakki.com/python_convex_polygon/


def cross(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1


ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())
dx, dy = map(int, input().split())

x = cross(ax - dx, ay - dy, bx - ax, by - ay)
y = cross()
