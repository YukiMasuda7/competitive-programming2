S = input()
S = list(S)
cnt = [0] * 26
for s in S:
    cnt[ord(s) - ord("a")] += 1
num = max(cnt)
x = []
for i in range(26):
    if cnt[i] == num:
        x.append(i)
ans = ""
for s in S:
    if ord(s) - ord("a") in x:
        continue
    else:
        ans += s
print(ans)
