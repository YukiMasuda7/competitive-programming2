# S、TのA以外の文字の数、順番が一致してれば作れる
# S,TのA以外の文字の間のAの数を管理して、その差の絶対値の和が答え？
S = list(input())
T = list(input())

if S == T:
    print(0)
    exit()

notA_S = []
notA_T = []
for s in S:
    if s != "A":
        notA_S.append(s)
for t in T:
    if t != "A":
        notA_T.append(t)

if notA_T != notA_S:
    print(-1)
else:
    l = len(notA_S)
    BS = [0] * (l + 1)
    BT = [0] * (l + 1)

    i = 0
    j = 0
    for s in S:
        if s == "A":
            BS[i] += 1
        else:
            i += 1

    for t in T:
        if t == "A":
            BT[j] += 1
        else:
            j += 1

    ans = 0
    for i in range(l + 1):
        ans += abs(BS[i] - BT[i])
    print(ans)
