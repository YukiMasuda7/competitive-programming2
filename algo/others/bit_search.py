# bit全探索
# 各要素について選ぶ・選ばないの2択 -> bit全探索

# 167-C

# 2**10=1024なので2**12は間に合う
N, M, X = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(N)]
min_cost = 10**10
for i in range(1 << N):
    flag = True
    understand = [0] * M
    cost = 0
    for shift in range(N):
        if i >> shift & 1:
            cost += books[shift][0]
            for j in range(M):
                understand[j] += books[shift][j + 1]

    for u in understand:
        if u < X:
            flag = False
            break

    if flag:
        min_cost = min(min_cost, cost)

if min_cost == 10**10:
    print(-1)
else:
    print(min_cost)
