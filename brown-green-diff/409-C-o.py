# 三点間の距離が同じなら正三角形
# 距離がL//3ずつになるような(a,b,c)の数を求める
# そもそもLが3の倍数じゃないなら正三角形はできない

N, L = map(int, input().split())
d = list(map(int, input().split()))
if L % 3 != 0:
    print(0)
    exit()
# 位置ごとの点の数を数える
cnt = [0] * L
cnt[0] = 1
tmp_pos = 0
for i in range(N - 1):
    tmp_pos = (tmp_pos + d[i]) % L
    cnt[tmp_pos] += 1
ans = 0
for i in range(L // 3):
    tmp = cnt[i]
    tmp *= cnt[(i + L // 3) % L]
    tmp *= cnt[(i + 2 * L // 3) % L]
    ans += tmp
print(ans)
