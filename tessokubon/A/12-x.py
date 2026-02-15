# 答えについての二分探索
# t秒までに印刷された数はΣ(t//A[i])
# O(Nlog10**9) ≒ O(30N)


# 答えがx以下か判定
def check(x, N, K, A):
    sum = 0
    for a in A:
        sum += x // a

    if sum >= K:
        return True
    else:
        return False


N, K = map(int, input().split())
A = list(map(int, input().split()))

l = 1
r = 10**9
while l < r:
    m = (l + r) // 2
    ans = check(m, N, K, A)

    if not ans:
        l = m + 1
    if ans:
        r = m

print(l)
