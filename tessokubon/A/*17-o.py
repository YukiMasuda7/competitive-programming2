# パスはゴールから辿ればわかる

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [0] * (N + 1)
dp[0] = 10**10
dp[2] = A[0]
for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + A[i - 2], dp[i - 2] + B[i - 3])
path = [N]
now = N
while now != 1:
    if dp[now] - dp[now - 1] == A[now - 2]:
        path.append(now - 1)
        now -= 1
    elif dp[now] - dp[now - 2] == B[now - 3]:
        path.append(now - 2)
        now -= 2
path = path[::-1]
print(len(path))
print(*path)
