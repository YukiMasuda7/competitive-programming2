# 2行目を決めていく。1, 2, 3列をそれぞれ
h1, h2, h3, w1, w2, w3 = map(int, input().split())
# a b c
# d e f
# g h i
# とする。

# 1行目を固定する。
ans = 0
for a in range(1, h1 - 1):
    for b in range(1, h1 - 1):
        c = h1 - a - b
        if 1 <= c <= h1 - 2:
            # 2行目を決める
            for d in range(1, w1 - 1):
                for e in range(1, w2 - 1):
                    f = h2 - d - e
                    if 1 <= f <= h2 - 2:
                        g = w1 - a - d
                        h = w2 - e - b
                        i = w3 - c - f
                        if 1 <= g and 1 <= h and 1 <= i and g + h + i == h3:
                            ans += 1
print(ans)
