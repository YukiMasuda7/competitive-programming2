# 辺が高々10**5個なので全探索でいける?
N, M = map(int, input().split())
cnt = [0] * N
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a < b:
        cnt[b] += 1
    else:
        cnt[a] += 1
ans = 0
for i in range(N):
    if cnt[i] == 1:
        ans += 1
print(ans)
