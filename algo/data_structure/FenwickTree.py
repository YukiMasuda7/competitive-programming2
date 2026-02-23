# FenwickTree(BIT)
# 累積和の高速計算(O(logN))・更新(O(logN))ができる

# 使い道

# ① 転倒数（inversion count）
# i<j かつ A[i]>A[j]となる(i,j)の数

# ② 「◯◯より小さい数が何個あるか」
# 動的に数を追加しながら
# x未満の個数, x以下の合計
# を高速に求められる。

# ③ 区間加算＋一点取得（テクニック）
# 工夫すると
# 区間更新, 区間取得
# も可能。

# ④ 座標圧縮と組み合わせ
# 値が10^9でも → 圧縮してBITで処理


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


# 初期化【O(N)】：変数名=FenwickTree(要素数)
Fen = FenwickTree(10)
# 加算【O(logN)】：add(インデックス番号,加算する数)
Fen.add(7, 3)
# 区間和の計算【O(logN)】：sum(左インデックス番号,右インデックス番号)
print(Fen.sum(2, 8))
# 値の参照【O(logN)】：select(インデックス番号)
print(Fen.select(7))
