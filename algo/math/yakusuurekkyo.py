# Nの約数列挙(O(N))
# 並び替えてもいいけどO(NlogN)かかる


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
