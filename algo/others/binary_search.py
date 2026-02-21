# 鉄則A11
# 整数 x が何番目に存在するかを返す関数
def search(x, A):
    L = 0
    R = N - 1
    while L <= R:
        M = (L + R) // 2
        if x < A[M]:
            R = M - 1
        if x == A[M]:
            return M
        if x > A[M]:
            L = M + 1
    return -1  # 整数 x が存在しない（注：この問題の制約で -1 が返されることはない）


# 入力（配列 X が 0 番目から始まることに注意）
N, X = map(int, input().split())
A = list(map(int, input().split()))

# 二分探索を行う（配列が 0 番目から始まるので、答えに 1 を足している）
Answer = search(X, A)
print(Answer + 1)


# 146C (条件を満たす最大値を探す)
# ↑と条件が違うことに注意
# 今回mの最大値を探しているから
# f(m)がちょうどXにならなくても
# f(m)<=Xであればansを更新する


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
