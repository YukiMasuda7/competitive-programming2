# 自分で制約を設けてみる
# 平方数判定の方法

# (1)p<qと(2)q<=pで場合分け
# (1)はp<10**7で全探索-> q=N/p**2
# (2)はq<10**7で全探索-> p=(N/q**2)**0.5


T = int(input())
for _ in range(T):
    found = False
    N = int(input())
    for p in range(2, 10**7):
        if N % p**2 == 0:
            print(p, N // p**2)
            found = True
            break
    if not found:
        for q in range(2, 10**7):
            if N % q == 0:
                ## N//qが平方数か判定
                N //= q
                if N % int(N**0.5) == 0:
                    print(int(N**0.5), q)
