# 部分和問題(Aから任意の要素を選んでXを作れるか？)

# 2**10 = 10**3
# なので2**60 = 10**18

# bit全探索では間に合わない

# dp[i][j]: i枚目までのカードを使って合計jを達成できるか
# N<60と小さいのもdpと気付けるポイント
# ↑Nが小さくないとdpの2次元の表を作れない

# i枚目のカードを入れる・入れないの2パターン

N, S = map(int, input().split())
A = [0] + list(map(int, input().split()))
dp = [[False] * (S + 1) for _ in range(N + 1)]

for i in range(N + 1):
    dp[i][0] = True
for i in range(1, N + 1):
    for j in range(1, S + 1):
        if dp[i - 1][j]:
            dp[i][j] = True
        if j - A[i] >= 0:
            if dp[i - 1][j - A[i]]:
                dp[i][j] = True
for i in range(N + 1):
    if dp[i][S]:
        print("Yes")
        exit()
print("No")
