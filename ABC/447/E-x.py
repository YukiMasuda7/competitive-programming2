# ufで辺のコストが最大になる辺からつないでいく。
# 連結成分が1になりそうなら繋がない(貪欲法)
# 連結成分の数をcntで管理(はじめはどのノードも繋がっていないのでn)

# 2**iはとても大きくなるのでTLEの原因になり得る
# pow(base, exp, modだと
# たとえば exp = 13 (二進: 1101) の場合、繰り返し2乗法によって下のようにO(log(exp))で計算できる
# 2^13 = 2^(8+4+1) = 2^8 * 2^4 * 2^1.
# 競プロでは「大きな指数に対しては常に pow(base, exp, mod) を使う

# 2**1 + 2**2 + 2**3 + ... + 2**M = 2*(2**M-1)

# カットセットの問題？


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


mod = 998244353
N, M = map(int, input().split())
ans = 2 * (pow(2, M, mod) - 1)
edges = []
for i in range(M):
    U, V = map(int, input().split())
    edges.append((U - 1, V - 1, pow(2, i + 1, mod)))

cnt = N
cost = 0
uf = UnionFind(N)
for i in range(M - 1, -1, -1):
    if uf.same(edges[i][0], edges[i][1]):
        uf.merge(edges[i][0], edges[i][1])
        cost += edges[i][2]
        cost %= mod
    else:
        if cnt > 2:
            uf.merge(edges[i][0], edges[i][1])
            cost += edges[i][2]
            cost %= mod
            cnt -= 1
        else:
            continue
print((ans - cost) % mod)
