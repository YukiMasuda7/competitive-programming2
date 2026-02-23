# 区間に含まれる.の数は.の数の累積和からわかる
# (l,r)の全探索だとO(N**2)で無理
# -> 区間の全探索をO(N)で行える(使える条件はある)尺取り法
# 区間内の.の数がKを超えるまではrを増やし続ける
# r,lを動かす中で取りうる最大の区間長が答え
S = ["0"] + list(input())
N = len(S)
K = int(input())
cnt = [0] * N
for i in range(N):
    if S[i] == ".":
        cnt[i] = 1
sum_cnt = [0] * N
for i in range(1, N):
    sum_cnt[i] = sum_cnt[i - 1] + cnt[i]

r = 1
ans = 0
for l in range(1, N):
    while r < N and sum_cnt[r] - sum_cnt[l - 1] <= K:
        r += 1
    ans = max(ans, r - l)
