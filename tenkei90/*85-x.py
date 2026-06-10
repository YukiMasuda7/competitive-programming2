# 範囲を絞り込んだとしてもK<=10**12全探索では間に合わない
# 探索の範囲をKの約数に絞り込む -> 約数の最大値は√K<10**6個
# 約数の個数自体は役6720にまでへる -> ２重ループでも間に合う


def f(N):
    yakusuu = []
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            if i != N // i:
                yakusuu.append(i)
                yakusuu.append(N // i)
            else:
                yakusuu.append(i)
    return yakusuu


K = int(input())
yakusuu = f(K)
yakusuu.sort()
ans = 0
for i in range(len(yakusuu)):
    a = yakusuu[i]
    for j in range(i, len(yakusuu)):
        b = yakusuu[j]

        # cが整数か、Cがb以上か確認
        if K % (a * b) == 0:
            if K // (a * b) >= b:
                ans += 1
print(ans)
