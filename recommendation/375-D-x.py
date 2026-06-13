# どこを固定するか(forで回すか)次第で複雑性が減る
# 3文字の回文の問題

# 英子文字の数が26しかないことに注目
# O(N*26)は余裕で間に合う

# jをforで回して, S[j]の左と右に文字の分布を調べる。
# 右左から同じ文字を選べばいいのでその選び方の数を答えに加算する。
from collections import defaultdict

S = input()
ans = 0
L = defaultdict(int)
R = defaultdict(int)
for i in range(1, len(S)):
    R[S[i]] += 1

for i in range(1, len(S)):
    L[S[i - 1]] += 1
    R[S[i]] -= 1

    for x in L:
        ans += L[x] * R[x]
print(ans)
