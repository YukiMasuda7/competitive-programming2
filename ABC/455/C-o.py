from collections import defaultdict

N, K = map(int, input().split())
A = list(map(int, input().split()))
D = defaultdict(int)
for i in range(N):
    D[A[i]] += 1
sum = []
ans = 0
for d in D:
    sum.append(D[d] * d)
    ans += D[d] * d

sum.sort(reverse=True)
for i in range(min(K, len(sum))):
    ans -= sum[i]
print(ans)
