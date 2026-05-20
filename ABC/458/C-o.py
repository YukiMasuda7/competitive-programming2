S = input()
ans = 0
for i in range(len(S)):
    if S[i] == "C":
        ans += min(i, len(S) - i - 1) + 1
print(ans)
