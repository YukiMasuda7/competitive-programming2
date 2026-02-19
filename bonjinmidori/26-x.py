# O(SQ)<10**10よりだめ
# 20番の問題みたいに通常状態・反転状態を管理する？
# 実際に反転、追加をすると間に合わない
# -> 文字のインデクス管理をすればいい？

# ↑そんなことしなくていい
# 今回は「先頭、末尾への追加」だけなのでdequeでO(1)で行える
# listのままだと末尾追加はO(1)だが、末尾追加はO(N)かかる
# 反転状態では　先頭->末尾、末尾->先頭、にして追加
# 最後、反転状態なら、反転を実行

from collections import deque

S = input()
Q = int(input())

q = deque()
reverse = False

for s in S:
    q.append(s)

for _ in range(Q):
    a = list(map(str, input().split()))

    if a[0] == "1":
        reverse = not reverse
    else:
        F = a[1]
        C = a[2]

        if not reverse:
            if F == "1":
                q.appendleft(C)
            else:
                q.append(C)
        else:
            if F == "1":
                q.append(C)
            else:
                q.appendleft(C)
ans = "".join(q)

if reverse:
    ans = ans[::-1]
print(ans)
