# 最小値の最大化 -> 二分探索
# 答えで二分探索

N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))


# 全てx以上のようかんをk+1以上作れるか?
# k+1個ちょうどでなくてもいいのがミソ
# O(N)
def check(x):
    cnt = 0
    prev = 0
    for i in range(N):
        if A[i] - prev >= x:
            cnt += 1
            prev = A[i]

    if L - prev >= x:
        cnt += 1

    return cnt >= K + 1


# チェックをforで回すとO(NL)で間に合わない
# O(NlogL)に抑える
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
