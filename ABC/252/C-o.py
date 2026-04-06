# どの文字を揃えるかで全探索？
N = int(input())
S = []
for i in range(N):
    s = input()
    s = list(s)
    S.append(s)
ans = 10**10
for i in range(10):
    # ind[i]: i番目の数が何個あるか
    ind = [0] * 10
    for j in range(N):
        for k in range(10):
            if S[j][k] == str(i):
                ind[k] += 1
    last = 0
    m = max(ind)
    for j in range(9, -1, -1):
        if ind[j] == m:
            last = j
            break
    ans = min(ans, 10 * (ind[last] - 1) + last)
print(ans)
