N, M, X, T, D = map(int, input().split())
height = [0] * (N + 1)
for i in range(N, -1, -1):
    if i >= X:
        height[i] = T
    else:
        height[i] = height[i + 1] - D
print(height[M])
