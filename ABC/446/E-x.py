# ASn-1とBSn-2のmodMを管理すればいい？
M, A, B = map(int, input().split())


def f(x, y):
    return A * x + B * y

ans=0
for x in range(10**3+1):
    for y in range(10**3+1):
        