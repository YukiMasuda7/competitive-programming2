# b=1の時、面積は7a + 3で 7*200 +3>1000なので200までで十分
N = int(input())
S = list(map(int, input().split()))
area = set()
for a in range(1, 201):
    for b in range(a, 201):
        s = 4 * a * b + 3 * a + 3 * b
        if s <= 1000:
            area.add(s)
ans = 0
for i in range(N):
    if S[i] not in area:
        ans += 1
print(ans)
