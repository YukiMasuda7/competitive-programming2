# 尺取り法っぽい -> l,rを動かすごとにその区間のmax,minを更新していけばいい？
# セグ木は -> それぞれのノードに[min, max]を持たせる


def segfunc(x: list, y: list):
    m = min(x[0], y[0])
    M = max(x[1], y[1])
    return [m, M]


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


inf = 10**10

N, D = map(int, input().split())
A = list(map(int, input().split()))
X = [[A[i], A[i]] for i in range(N)]
ST = SegTree(X, [inf, -inf], segfunc)
