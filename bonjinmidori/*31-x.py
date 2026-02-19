# 貪欲法

# DPっぽい？
# i回目まで最大得点をDPで求めていけばいい？
# i回目の結果がi-k回目の結果に依存するのもDPっぽい？
# dp[i][j]: i回目にj(j=0,1,2の順にr,s,p)を出して勝った時の最大点数

# しかし、勝ちの判、K回目に同じ手を出せないなどの条件が面倒
# ↑貪欲法でいける


# 相手の手xに対して何を出せば勝てるかを返す
def f(x, R, S, P):
    if x == "r":
        return ["p", P]
    elif x == "s":
        return ["r", R]
    else:
        return ["s", S]


N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
hand = [None] * N
ans = 0
for i in range(N):
    if (i - K >= 0 and hand[i - K] != f(T[i], R, S, P)[0]) or i - K < 0:
        ans += f(T[i], R, S, P)[1]
        hand[i] = f(T[i], R, S, P)[0]
    # 相手に勝てる手がK回前に出ていた場合、
    # それ以外の2つのどちらかを次のK回後に勝てる手と
    # 被らないように出せばいい(aとしておく))
    else:
        hand[i] = "a"
print(ans)
