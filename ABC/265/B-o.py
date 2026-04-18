N, M, T = map(int, input().split())
A = list(map(int, input().split()))

bonuses = [0] * N

for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    bonuses[x] = y

for i in range(N - 1):
    T += bonuses[i]
    T -= A[i]
    if T <= 0:
        print("No")
        exit()
print("Yes")
