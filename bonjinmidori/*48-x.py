# 全探索じゃあ間に合わない
# マンハッタン距離 -> チェビシェフ距離 の変換

# マンハッタン距離: |x1 - x2| + |y1 - y2|
# チェビシェフ距離: max(|x1 - x2|, |y1 - y2|)

#   (x1, y1), (x2, y2)間のマンハッタン距離
# = (x1+y1, x1-y1), (x2+y2, x2-y2)間のチェビシェフ距離
# = max(|(x1+y1) - (x2+y2)|, |(x1-y1) - (x2-y2)|)

# 証明 -> p5999

# (x, y) -> (x+y, x-y)の変換
# これらのチェビシェフ距離が(x, y)のマンハッタン距離なので
# 変換後のx座標(つまりx+y)のmax - min
# 変換後のy座標(つまりx-y)のmax - min
# のうち大きい方が答え


N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]
converted_x = [0] * N
converted_y = [0] * N
for i in range(N):
    x = points[i][0]
    y = points[i][1]
    converted_x[i] = x + y
    converted_y[i] = x - y

ans = max(max(converted_x) - min(converted_x), (max(converted_y) - min(converted_y)))
print(ans)
