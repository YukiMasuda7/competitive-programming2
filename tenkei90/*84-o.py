# スタートを全探索
# 一番近い異符号のindは二分探索で求められる
# 別解もチェック
import bisect

N = int(input())
S = input()
maru = []
batu = []
for i in range(N):
    if S[i] == "o":
        maru.append(i)
    else:
        batu.append(i)
ans = 0
for i in range(N - 1):
    if S[i] == "o":
        x = bisect.bisect_left(batu, i)
        if x == len(batu):
            continue
        else:
            ans += N - batu[x]

    else:
        x = bisect.bisect_left(maru, i)
        if x == len(maru):
            continue
        else:
            ans += N - maru[x]
print(ans)
