# 最長増加部分列(LIS)の限定的なバージョン
# d[i][v] を「A[1]からA[i]までの連続部分列のみを考えた時に、
# 末尾の要素が v であるような条件を満たす部分列の長さの最大値」とします。
# 求める答えは d[i][v] の最大値です。

from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)
for v in a:
    d[v] = max(d[v], d[v - 1] + 1)
print(max(d.values()))
