# 二つの火がぶつかる時刻は片側から火をつけて全て燃え切るまでの時間の半分
# -> 向きは違えど2つの火の進んだ距離の総和は、片側からの火が進む距離と同じなので

# 上で分かった時刻を元に左からシミュレーションすればいい
N = int(input())
X = []
T = 0
for i in range(N):
    A, B = map(int, input().split())
    X.append([A, B])
    T += A / B

i=0
while True:
    t=X[i][0]/X[i][1]
    if T > 