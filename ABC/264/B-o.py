# 真ん中からの(チェス距離)の偶奇で判定
R, C = map(int, input().split())
cy = 8
cx = 8
d = max(abs(R - cx), abs(C - cy))
if d % 2 == 0:
    print("white")
else:
    print("black")
