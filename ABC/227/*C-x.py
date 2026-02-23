# 条件付きmax,min問題
# a,bが決まれば、Cはすぐ出る
# a<=b<=c かつabc<=N(N<=10**11)なのでa**3<=N。
# aを固定した時、bc<=N/A。よって
# b**2<N/A
# 割り算はなるべくなくす

N = int(input())
ans = 0
A = 1
while A**3 <= N:
    B = A
    while A * B**2 <= N:
        ans += int(N / (A * B)) - B + 1
        B += 1
    A += 1
print(ans)
