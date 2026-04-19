# 値段の大きい硬貨から使うべきとは限らない
N = int(input())
coins = list(map(int, input().split()))
coins.sort()
A = coins[0]
B = coins[1]
C = coins[2]
cl = N // C
ans = 10**10
for ci in range(cl, -1, -1):
    bl = (N - C * ci) // B
    for bi in range(bl, -1, -1):
        if (N - C * ci - B * bi) % A == 0:
            ai = (N - C * ci - B * bi) // A
            ans = min(ans, ai + bi + ci)
print(ans)
