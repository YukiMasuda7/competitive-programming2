# 全探索だと間に合わない
# a[i]==iのものは個別に計算
# 他に関してはa[i]!=i かつ a[j]!=jで
# a[i]=jかつa[j]=iとなればいい

N = int(input())
A = list(map(int, input().split()))
kaburi = 0
ans = 0
for i in range(N):
    if A[i] == i + 1:
        kaburi += 1
    else:
        if i < A[i] - 1 and A[A[i] - 1] == i + 1:
            ans += 1
if kaburi >= 1:
    ans += kaburi * (kaburi - 1) // 2
print(ans)
