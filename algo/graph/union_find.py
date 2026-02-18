# ① 連結成分の管理（グラフ）

# ✔ できること
# 2頂点が同じ連結成分か判定
# 連結成分の数を管理
# 辺の追加に応じて統合

# 典型問題
# 無向グラフの連結成分数を求める
# クエリで「uとvはつながっているか？」
# 動的に辺が追加される問題

# ② 最小全域木（MST）
# ✔ 有名アルゴリズム
# Kruskal法
# 辺を重み順に見て、
# まだつながっていないなら採用
# すでに同じ集合ならスキップ（サイクル回避）
# で使います。

# ③ サイクル検出（無向グラフ）
# 辺 (u, v) を追加するとき
# find(u) == find(v) → サイクル発生
# という判定が一瞬でできる。

# ④ グループ分け問題
# 例えば：
# 「友達関係」
# 「同じ文字を入れ替え可能」
# 「同じ種類に分類される」
# 例
# 「a と b は同じグループ」
# 「b と c は同じグループ」
# → a, b, c は同じ集合

# ⑤ 2Dグリッド問題
# 島の個数（Unionで上下左右を結合）
# 動的に土地を追加する問題（LeetCodeで頻出）

# ⑥ 重み付きUnion-Find
# 拡張版として：
# 「x と y の差が d」
# 「x は y の3倍」
# のような関係式管理もできる。

# 🔴 逆に苦手なこと
# ❌ 辺の削除
# ❌ 経路そのものを求める
# ❌ 最短距離
# ❌ 有向グラフの到達判定

# 🎯 使うべき問題の特徴
# 次のワードがあればUnion-Findを疑う：
# 「同じグループ」
# 「連結か判定」
# 「マージする」
# 「代表元」
# 「サイクル判定」
# 「クラス分け」


# UnionFind
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent_size = [-1] * n

    def leader(self, a):
        if self.parent_size[a] < 0:
            return a
        self.parent_size[a] = self.leader(self.parent_size[a])
        return self.parent_size[a]

    def merge(self, a, b):
        x, y = self.leader(a), self.leader(b)
        if x == y:
            return
        if abs(self.parent_size[x]) < abs(self.parent_size[y]):
            x, y = y, x
        self.parent_size[x] += self.parent_size[y]
        self.parent_size[y] = x
        return

    def same(self, a, b):
        return self.leader(a) == self.leader(b)

    def size(self, a):
        return abs(self.parent_size[self.leader(a)])

    def groups(self):
        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[self.leader(i)].append(i)
        return [r for r in result if r != []]


# ・初期化：変数名=UnionFind(要素の数)
# ・グループリーダー(根)の確認：変数名.leader(要素番号)
# ・グループ化：変数名.merge(要素番号1,要素番号2)
# ・同一グループかの確認：変数名.same(要素番号1,要素番号2)
# 　(同一ならTrue,違うグループならFalseを返す)
# ・所属するグループのサイズ確認：変数名.size(要素番号)
# ・グループ全体の確認：変数名.groups()

N, Q = map(int, input().split())
# 1-indexで
U = UnionFind(N + 1)
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        U.merge(q[1], q[2])
    else:
        if U.same(q[1], q[2]):
            print("Yes")
        else:
            print("No")
