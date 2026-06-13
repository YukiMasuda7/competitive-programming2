# コストを考えない最短距離を考えても意味ない->縦横の数が同じ
# コストの小さい方をたくさん使いたい->反転するから連続で
# 負を絶対値を取って無視して考えてもOK?

# Goalまでのマンハッタン距離が一番短くなるまでlow_costだけで近づく？

T = int(input())
for case in range(T):
    tmp_cost = 0
    A, B, X, Y = map(int, input().split())

    low_cost = min(A, B)
    high_cost = max(A, B)

    X = abs(X)
    Y = abs(Y)

    near = min(X, Y)
    tmp_cost += low_cost * 2 * near
    X -= near
    Y -= near
    if X == 0 and Y == 0:
        print(tmp_cost)
    else:
        if X != 0:
            left_dist = X
        else:
            left_dist = Y

        if low_cost * 3 <= high_cost:
            if left_dist % 2 == 0:
                tmp_cost += low_cost * 2 * left_dist
            else:
                tmp_cost += low_cost * 2 * (left_dist - 1)
                tmp_cost += low_cost * 3
        else:
            if left_dist % 2 == 0:
                tmp_cost += (high_cost + low_cost) * (left_dist // 2)
            else:
                tmp_cost += (high_cost + low_cost) * ((left_dist - 1) // 2)
                tmp_cost += high_cost
        print(tmp_cost)
