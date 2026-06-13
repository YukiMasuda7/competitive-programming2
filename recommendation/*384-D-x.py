# 無限数列は間にAを挟むから、右、左にはみ出た部分の和を全て求めておけばいい
# -> 区間和がxかx以上かなどの判定
# -> ①尺取り法
# -> ②累積和とset
N, S = map(int, input().split())
A = list(map(int, input().split()))

T = sum(A)
S %= T
if S == 0:
    print("Yes")
    exit()
B = A * 2
BS = [0] * len(B)
BS[0] = B[0]
for i in range(1, len(B)):
    BS[i] = BS[i - 1] + B[i]

# 尺取り法
R = [0] * len(BS)

for i in range(len(BS) - 1):
    # 右端のスタート地点を決める
    if i == 0:
        R[i] = 0
    else:
        R[i] = R[i - 1]

    while R[i] < len(BS) - 1 and BS[R[i] + 1] - BS[i] <= S:
        if BS[R[i] + 1] - BS[i] == S:
            print("Yes")
            exit()
        R[i] += 1

print("No")
