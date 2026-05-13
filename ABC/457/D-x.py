# K<=10**18
# 2**10=10**3より
# K<=2**60
# heapqの貪欲法はだめ
# 答えを2分探索？


N, K = map(int, input().split())
A = list(map(int, input().split()))
L = 10**18


# 全てX以上にできるか
def check(x):
    cnt = 0
    for i in range(N):
        if A[i] < x:
            y = x - A[i]
            cnt += (y + i) // (i + 1)

    return cnt <= K


l = 0
r = L
# l<rなら、r=l+1の時にm=lとなり無限ループになるので注意
while r - l > 1:
    m = (l + r) // 2
    if check(m):
        l = m
    else:
        r = m

print(l)
