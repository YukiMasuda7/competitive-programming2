from collections import Counter

S = input()
cnt = Counter(S)
for c in cnt:
    if cnt[c] == 1:
        print(c)
        exit()
print(-1)
