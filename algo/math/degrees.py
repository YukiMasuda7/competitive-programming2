import math

# 度 → ラジアン
deg = 60
rad = math.radians(deg)  # = deg * pi / 180

# ラジアン → 度
deg2 = math.degrees(rad)

# 三角関数（引数はラジアン）
s = math.sin(rad)
c = math.cos(rad)
t = math.tan(rad)

# 逆三角関数（戻り値はラジアン）
x = 0.5
a = math.asin(x)
a_deg = math.degrees(a)

# (a, b)を原点中心にd度回転
a, b, d = map(int, input().split())
theta = math.radians(d)

x = a * math.cos(theta) - b * math.sin(theta)
y = a * math.sin(theta) + b * math.cos(theta)

# 2点から角度（-pi～pi）
dx, dy = 1, 1
theta = math.atan2(dy, dx)
theta_deg = math.degrees(theta)

# 角度の正規化
# 0～360度
norm360 = theta_deg % 360
# -180～180度
norm180 = (theta_deg + 180) % 360 - 180
