# 区間のL,Rのうち10**iの位の数がその桁の中でどの区間にあるかを記録
# 10**iの数が[l,r]にあるとすると黒板に描かれる文字の数は
# i*(l+(L+1)+...+r) = i*(r-l+1)(l+r)/2

mod = 10**9 + 7
L, R = map(int, input().split())
l = len(str(L)) - 1
r = len(str(R)) - 1
kukan = [[0, 0] for _ in range(19)]
for i in range(19):
    if i < l:
        continue
    elif i == l:
        kukan[i][0] = L
        if i == r:
            kukan[i][1] = R
        elif i < r:
            kukan[i][1] = 10 ** (i + 1) - 1
    elif l < i:
        if 10**i <= R:
            kukan[i][0] = 10**i
        if i == r:
            kukan[i][1] = R
        elif i < r:
            kukan[i][1] = 10 ** (i + 1) - 1
ans = 0
for i in range(19):
    ans += (i + 1) * (kukan[i][1] - kukan[i][0] + 1) * (kukan[i][0] + kukan[i][1]) // 2
    ans %= mod
print(ans)
