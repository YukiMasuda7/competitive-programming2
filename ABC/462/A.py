num = set(str(i) for i in range(10))
S = input()
ans = ""
for s in S:
    if s in num:
        ans += s
print(ans)
