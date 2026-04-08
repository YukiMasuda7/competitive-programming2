# なるべく小さいB[i]を繰り返したい
# 繰り返しクリアは、最新ステージでかつ、最後以外で行う必要がない
# 繰り返すステージを全探索すればいい
# 初期値を十分大きくしないと通らない
N, X = map(int, input().split())
A = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]
init_time = 0
ans = 10**30
for i in range(1, min(N + 1, X + 1)):
    cnt = i
    init_time += A[i][0] + A[i][1]
    tmp_time = init_time
    if cnt < X:
        tmp_time += (X - cnt) * A[i][1]
    ans = min(ans, tmp_time)
print(ans)
