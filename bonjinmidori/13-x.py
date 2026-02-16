# 切捨ての際の誤差でWAになる例
# 小数は避けるべき
N, X = map(int, input().split())
alcohol = 0
for i in range(N):
    V, P = map(int, input().split())
    alcohol += V * P
    if alcohol > X * 100:
        print(i + 1)
        exit()
print(-1)
