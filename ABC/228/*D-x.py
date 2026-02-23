# BITと二分探索

# while A[h] != -1:
#    h = (h + 1) % N
# だと間に合わない。
# A[h] != -1の場合にh<iかつA[i] == -1
# となるiを高速に求めたい -> heapq?（違う）


class FenwickTree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def _sum(self, r):
        s = 0
        while 0 < r:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def sum(self, l, r):
        r += 1
        return self._sum(r) - self._sum(l)

    def select(self, p):
        return self.sum(p, p)


N = 2**20
Q = int(input())
A = [-1] * N
Fen = FenwickTree(N)
# Fen[p]=1ならば更新されていない(A[p]=-1)
# Fen[p]=0ならば更新されている(A[p]≠-1)
# 最初は全て1にする
for i in range(N):
    Fen.add(i, 1)


# 二分探索
def Nibutan(l, r):

    # 1<右端-左端　の間
    while 1 < r - l:
        # 中央
        c = (l + r) // 2
        # 区間Fen[左端~中央]に「1」があれば⇔区間和が1以上であれば
        if 1 <= Fen.sum(l, c):
            # 右端を更新
            r = c
        # そうでなければ
        # ⇔区間Fen[左端~中央]に「1」がなければ⇔区間和が0であれば
        else:
            # 左端を更新
            l = c

    # 右端を返す
    return r


# Q回
for i in range(Q):
    # 入力を受け取る
    t, x = map(int, input().split())

    # h=x mod N
    h = x % N

    # t=1の場合
    if t == 1:
        # A[h]=-1ならば
        if A[h] == -1:
            # A[h]を更新
            A[h] = x
            # A[h]≠-1となったからFen[h]=0にする⇔-1する
            Fen.add(h, -1)

        # A[h]≠-1ならば
        else:
            # Fen[h~(N-1)]の区間和が1以上
            # ⇔h~(N-1)の区間にAが-1になっているものが少なくとも1つある
            if 1 <= Fen.sum(h, N - 1):
                # pを二分探索で探す
                p = Nibutan(h, N - 1)

            # Fen[h~(N-1)]の区間和が1以上
            # ⇔h~(N-1)の区間にAが-1になっているものがない
            # ⇔0~(x-1)の区間を探索
            else:
                # A[0]=-1ならば
                if A[0] == -1:
                    # p=0となる
                    p = 0
                # A[0]≠-1ならば
                else:
                    # pを二分探索で探す
                    p = Nibutan(0, h - 1)

            # A[p]を更新
            A[p] = x

            # A[h]≠-1となったからFen[h]=0にする⇔-1する
            Fen.add(p, -1)

    # t=2の場合
    else:
        # 出力
        print(A[h])
