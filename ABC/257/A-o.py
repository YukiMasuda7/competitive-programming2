N, X = map(int, input().split())
d = [""] * 26
for i in range(26):
    x = chr(ord("A") + i)
    d[i] = x
X -= 1
a = X // N
print(d[a])
