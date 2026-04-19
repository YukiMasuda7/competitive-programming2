# 連結判定->UnionFind

# 毎回dfsなどで到達できるか調べてたら間に合わない
# グリッド上の連結判定もUnionFindで行ける(i, j)-> i*W + j
# 逆アッカーマン関数の計算量は、ほぼ定数
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]


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


H, W = map(int, input().split())
Q = int(input())
G = [[False] * W for _ in range(H)]
uf = UnionFind(H * W)
for i in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        ny = q[1] - 1
        nx = q[2] - 1
        G[ny][nx] = True
        for dir in directions:
            if 0 <= ny + dir[0] < H and 0 <= nx + dir[1] < W:
                if G[ny + dir[0]][nx + dir[1]]:
                    uf.merge(ny * W + nx, (ny + dir[0]) * W + nx + dir[1])
    else:
        ry = q[1] - 1
        rx = q[2] - 1
        by = q[3] - 1
        bx = q[4] - 1
        if G[ry][rx] and G[by][bx] and uf.same(ry * W + rx, by * W + bx):
            print("Yes")
        else:
            print("No")
