# UnionFindは辺の削除は出来ないことに注意
# 1,2,3...,Nの順に消す
# -> N,N-1,N-2, ..., 1の順にノードを追加していくと下の状態を復元できる
# 連結成分数nは自分で管理する
# ノードを追加するとn+=1、
# そのノードから辺を張る時に、違うグループのノードならば
# n-=1する

# 一見TLEしそうだが
# 各辺は「高い方のノードからのみ」しかmergeしないので、
# 無駄な重複がない。だからTLEしない


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
uf = UnionFind(N)
edges = [[] for _ in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    edges[A].append(B)
    edges[B].append(A)
ans = [0] * N
ans[N - 1] = 1
for i in range(N - 2, -1, -1):
    ans[i] = ans[i + 1]
    ans[i] += 1
    for to in edges[i]:
        if to > i:
            if not uf.same(i, to):
                ans[i] -= 1
                uf.merge(i, to)
ans = ans[1:]
ans.append(0)
for a in ans:
    print(a)
