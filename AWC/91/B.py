N, K = map(int, input().split())
evaluations = [0] * N
for i in range(N):
    C = int(input())
    V = list(map(int, input().split()))
    V.sort()
    evaluations[i] = V[C // 2]

evaluations.sort(reverse=True)
ans = 0
i = 0
while True:
    if i >= N:
        break
    if evaluations[i] < 0 or i >= K:
        break
    ans += evaluations[i]
    i += 1
print(ans)
