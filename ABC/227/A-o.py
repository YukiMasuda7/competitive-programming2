N, K, A = map(int, input().split())
ans = (A - 1 + K - 1) % N + 1
print(ans)
