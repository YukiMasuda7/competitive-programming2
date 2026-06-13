# imosっぽい
# その時刻に犯行を開始できた人の数をimosで求める。
# nC2で人数が出る

N, D = map(int, input().split())
A = [0] * (10**6 + 10)
for i in range(N):
    S, T = map(int, input().split())
    if T - S >= D:
        A[S] += 1
        A[T - D + 1] -= 1
for i in range(1, 10**6 + 10):
    A[i] += A[i - 1]
ans = 0
for i in range(10**6 + 10):
    if A[i] >= 2:
        tmp = (A[i] * (A[i] - 1)) // 2
        ans += tmp
print(ans)
