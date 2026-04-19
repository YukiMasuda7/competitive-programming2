N = int(input())
s = set()
ans = []
for i in range(N):
    S = input()
    if S not in s:
        s.add(S)
        ans.append(i + 1)
for a in ans:
    print(a)
