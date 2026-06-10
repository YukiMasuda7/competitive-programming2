T = int(input())
for _ in range(T):
    S = list(map(int, input().split()))
    x1 = S[0]
    y1 = S[1]
    r1 = S[2]
    x2 = S[3]
    y2 = S[4]
    r2 = S[5]
    d = (x1 - x2) ** 2 + (y1 - y2) ** 2
    if (r1 - r2) ** 2 <= d <= (r1 + r2) ** 2:
        print("Yes")
    else:
        print("No")
