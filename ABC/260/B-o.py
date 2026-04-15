# ソートの昇順、降順を変える時は-1倍
N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
score1 = []
score2 = []
score3 = []
ans = set()
for i in range(N):
    score1.append([A[i], -i])
    score2.append([B[i], -i])
    score3.append([A[i] + B[i], -i])

score1.sort(reverse=True)
score2.sort(reverse=True)
score3.sort(reverse=True)

cnt = 0
i = 0
while cnt < X and i < N:
    if -score1[i][1] not in ans:
        cnt += 1
        ans.add(-score1[i][1])
    i += 1

cnt = 0
i = 0
while cnt < Y and i < N:
    if -score2[i][1] not in ans:
        cnt += 1
        ans.add(-score2[i][1])
    i += 1

cnt = 0
i = 0
while cnt < Z and i < N:
    if -score3[i][1] not in ans:
        cnt += 1
        ans.add(-score3[i][1])
    i += 1

ans = list(ans)
ans.sort()
for a in ans:
    print(a + 1)
