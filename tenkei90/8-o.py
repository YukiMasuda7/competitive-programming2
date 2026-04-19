# あるt(i番目)より前にaがnこあればcnt[i]+=nを繰り返す
from collections import Counter

mod = 10**9 + 7

N = int(input())
S = input()
a = t = c = o = d = e = r = 0
ans = 0
for i in range(len(S)):
    if S[i] == "a":
        a += 1
        a %= mod
    elif S[i] == "t":
        t += a
        t %= mod
    elif S[i] == "c":
        c += t
        c %= mod
    elif S[i] == "o":
        o += c
        o %= mod
    elif S[i] == "d":
        d += o
        d %= mod
    elif S[i] == "e":
        e += d
        e %= mod
    elif S[i] == "r":
        r += e
        r %= mod
print(r)
