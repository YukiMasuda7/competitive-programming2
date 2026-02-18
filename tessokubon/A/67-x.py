# 最小全域木問題
# 最小全域木(MST):
# 「連結な無向重み付きグラフ」において、
# 全てのノードを含む木のうち、コストが最小のもの

# クラスカル法
# 同じグループにない２つのノードのうち、
# コストの最も小さい辺から追加していく方法(貪欲法)で解ける
# 実装は配列のソートとUnion-Findで実装できる。O(MlogM + N)


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


N, M = map(int, input().split())
edges_with_cost = [list(map(int, input().split())) for _ in range(M)]
# 辺を長さの小さい順にソートする
edges_with_cost.sort(key=lambda x: x[2])

U = UnionFind(N + 1)
ans = 0
for a, b, c in edges_with_cost:
    if not U.same(a, b):
        U.merge(a, b)
        ans += c

print(ans)
