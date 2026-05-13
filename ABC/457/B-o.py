N = int(input())
L = []
for i in range(N):
    Z = list(map(int, input().split()))
    L.append(Z[1:])
X, Y = map(int, input().split())
print(L[X - 1][Y - 1])
