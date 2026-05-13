# 異なる文字だけの文字列の部分列は1+2+3+...+len(S)=n*(n+1)/2
mod = 998244353
cnt = []
S = input()
l = len(S)
i = 0
n = 1
while i < l - 1:
    if S[i + 1] == S[i]:
        cnt.append(n)
        n = 1
    else:
        n += 1
    i += 1
if S[l - 2] != S[l - 1]:
    cnt.append(n)
else:
    cnt.append(1)
ans = 0
for c in cnt:
    ans += c * (c + 1) // 2
    ans %= mod
print(ans)
