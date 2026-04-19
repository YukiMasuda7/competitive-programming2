# N<20なので生成自体はbit全探索でいける0(2**20=10**6)
# (なら+1、)なら-1で途中で-にならなければOK
N = int(input())
ans = []
for mask in range(1 << N):
    cnt = 0
    S = ""
    flag = True
    for shift in range(N):
        if mask >> N - 1 - shift & 1:
            cnt += 1
            S += "("
        else:
            cnt -= 1
            S += ")"
        if cnt < 0:
            flag = False
            break
    if flag and cnt == 0:
        ans.append(S)
ans.sort()
for a in ans:
    print(a)
