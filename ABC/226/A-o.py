X = input()
a = X[:-4]
b = X[-3]
a = int(a)
b = int(b)
if b < 5:
    ans = a
else:
    ans = a + 1
print(ans)
