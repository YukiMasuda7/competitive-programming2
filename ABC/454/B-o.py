N, M = map(int, input().split())
F = list(map(int, input().split()))
s = set()
ans1 = "Yes"
for i in range(N):
    if F[i] in s:
        ans1 = "No"
    else:
        s.add(F[i])
if len(s) == M:
    ans2 = "Yes"
else:
    ans2 = "No"
print(ans1)
print(ans2)
