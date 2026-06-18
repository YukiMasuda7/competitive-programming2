N = int(input())
T = list(map(int, input().split()))
m = 10**10
M = -1
for i in range(1, N):
    m = min(m, T[i] - T[i - 1])
    M = max(M, T[i] - T[i - 1])
print(m, M)
