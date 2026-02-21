# 2分探索
# n=1~10**9でnが大きくなるほど値段も高くなる
# 単調増加なら二分探索が使える


def f(n, A, B):
    return A * n + B * len(str(n))


A, B, X = map(int, input().split())
l = 1
r = 10**9
ans = 0

while l <= r:
    m = (l + r) // 2
    if f(m, A, B) <= X:
        ans = m
        l = m + 1
    else:
        r = m - 1
print(ans)
