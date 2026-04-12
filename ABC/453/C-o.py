# 2**20 = 10**6くらいなので全て試せばいい
N = int(input())
L = list(map(int, input().split()))
ans = -1
for mask in range(2**N):
    tmp_ans = 0
    pos = 0.5
    # Trueが正、Falseが負
    hugou = True
    for shift in range(N):
        x = mask >> shift & 1
        # 正に進む
        if x:
            pos += L[shift]
            # 負->正
            if not hugou and pos > 0:
                hugou = True
                tmp_ans += 1
        # 負に進む
        else:
            pos -= L[shift]
            # 正->負
            if hugou and pos < 0:
                hugou = False
                tmp_ans += 1
    ans = max(ans, tmp_ans)
print(ans)
