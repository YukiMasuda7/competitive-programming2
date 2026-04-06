S = input()
l = len(S)
if l == 1:
    ans = S * 6
elif l == 2:
    ans = S * 3
else:
    ans = S * 2
print(ans)
