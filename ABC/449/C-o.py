N, L, R = map(int, input().split())
S = input()
S = list(S)
T = [0] * len(S)
num_cnt = [0] * 26
for i in range(len(S)):
    T[i] = ord(S[i]) - ord("a")

limit = min(R + 1, N)
for i in range(L, limit):
    num_cnt[T[i]] += 1

ans = 0
ans += num_cnt[T[0]]
l = min(L, N - 1)
r = min(R, N - 1)
for i in range(1, N):
    head = T[i]
    if 0 <= l < N:
        num_cnt[T[l]] -= 1
        l += 1
    if 0 <= r + 1 < N:
        num_cnt[T[r + 1]] += 1
        r += 1
    ans += num_cnt[head]
print(ans)
