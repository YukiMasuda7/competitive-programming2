T = int(input())
for _ in range(T):
    cnt = [0] * 26
    S = input()
    l = len(S)
    for s in S:
        cnt[ord(s) - ord("a")] += 1
    M = max(cnt)
    Mcnt = 0
    m = -1
    for c in cnt:
        if c == M:
            Mcnt += 1
        if c < M:
            m = max(m, c)
    M -= m
    print(M, m, Mcnt)
    if Mcnt == 1 and M >= 2:
        print("No")
    else:
        print("Yes")
