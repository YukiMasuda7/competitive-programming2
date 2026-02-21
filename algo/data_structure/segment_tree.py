# セグメント木(RMQ)：　ある区間のに含まれる要素の最大値を木を使って高速に求める

# (1)完全二分木の深さhの要素数は2**h
# (2)2**0 + 2**1 + 2**2 + ... + 2**h = 2**(h+1) - 1
# (根を1として)親iの左の子が2*i、右の子が2*i+1。
# 逆にiの親はi//2である。

# 葉ノードはx_list[i]のみを格納する。aを2**(a-1) < len(X_list) < 2**aを満たすとして、
# <つまりa=len(x_list).bit_length()である>
# 葉ノードは余分に2**a用意する。またこの時のはノードの深さはaである。<(1)より>
# 深さ１から深さh-1までのノード数は2**a - 1になるので<(2)より>、計 2**(a+1) - 1のノードが必要。
# つまり余分に2**(a+1)のノードを用意すればいい。


# 解説なし(根ノードを１とする)
def segfunc(x, y):
    return x ^ y


class SegTree:
    def __init__(self, x_list, init, segfunc):
        self.init = init
        self.segfunc = segfunc
        self.Height = len(x_list).bit_length() + 1
        self.Tree = [init] * (2**self.Height)
        self.num = 2 ** (self.Height - 1)
        for i in range(len(x_list)):
            self.Tree[2 ** (self.Height - 1) + i] = x_list[i]
        for i in range(2 ** (self.Height - 1) - 1, 0, -1):
            self.Tree[i] = segfunc(self.Tree[2 * i], self.Tree[2 * i + 1])

    def select(self, k):
        return self.Tree[k + self.num]

    def update(self, k, x):
        i = k + self.num
        self.Tree[i] = x
        while i > 1:
            if i % 2 == 0:
                self.Tree[i // 2] = self.segfunc(self.Tree[i], self.Tree[i + 1])
            else:
                self.Tree[i // 2] = self.segfunc(self.Tree[i - 1], self.Tree[i])
            i //= 2

    def query(self, l, r):
        result = self.init
        l += self.num
        r += self.num + 1

        while l < r:
            if l % 2 == 1:
                result = self.segfunc(result, self.Tree[l])
                l += 1
            if r % 2 == 1:
                result = self.segfunc(result, self.Tree[r - 1])
            l //= 2
            r //= 2
        return result


# 鉄則A58

N, Q = map(int, input().split())
A = [0] * N
ST = SegTree(A, -(10**10), segfunc)
for i in range(Q):
    q = input().split()
    if q[0] == "1":
        ST.update(int(q[1]) - 1, int(q[2]))
    else:
        print(ST.query(int(q[1]) - 1, int(q[2]) - 2))


# コード(解説あり)
# ここは変える
def segfunc(x, y):
    return x ^ y


class SegTree:
    def __init__(self, x_list, init, segfunc):
        self.init = init  # ノードの初期値
        self.segfunc = segfunc
        self.Height = len(x_list).bit_length() + 1
        self.Tree = [init] * (2**self.Height)
        self.num = 2 ** (self.Height - 1)  # 葉の開始インデックス
        # 葉ノードをA[i]で埋める
        for i in range(len(x_list)):
            self.Tree[2 ** (self.Height - 1) + i] = x_list[i]
        # 左右の子ノードを元に親のノードの値を出す。(2番目に深い層の最後のノードから根まで逆順に)
        for i in range(2 ** (self.Height - 1) - 1, 0, -1):
            self.Tree[i] = segfunc(self.Tree[2 * i], self.Tree[2 * i + 1])

    # 元データのk番目の値を取得（葉の位置にずらしてアクセス）
    def select(self, k):
        return self.Tree[k + self.num]

    def update(self, k, x):
        i = k + self.num
        # 葉ノードの書き換え
        self.Tree[i] = x
        # 葉ノードの更新を親に伝搬していく
        while i > 1:
            # iが左の子 -> 右の子との結果を親に伝搬
            if i % 2 == 0:
                self.Tree[i // 2] = self.segfunc(self.Tree[i], self.Tree[i + 1])
            # iが右の子 -> 左の子との結果を親に伝搬
            else:
                self.Tree[i // 2] = self.segfunc(self.Tree[i - 1], self.Tree[i])
            i //= 2

    # 区間[l, r]に対する問い合わせ
    def query(self, l, r):
        result = self.init
        # 葉ノードに移動
        l += self.num
        r += self.num + 1

        while l < r:
            # 親に上がる時に情報が失われる場合はその情報をresultに反映してから親に上がる。

            # lが左の子なら(親は右の子の情報もを反映したデータなので)、そのまま親に上がってOK
            # lが右の子なら、
            # その親は左の子(左の子は範囲外)の結果も反映した値なので親に上がるとまずい。
            # 代わりに右の子の情報をresultに反映させてから
            # 右の兄弟の左の子にlを狭める
            if l % 2 == 1:
                result = self.segfunc(result, self.Tree[l])
                l += 1
            # rが右の子なら、
            # r-1の情報をresultに反映させる
            if r % 2 == 1:
                result = self.segfunc(result, self.Tree[r - 1])
            l //= 2
            r //= 2
        return result
