dirs = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
N = int(input())
A = []
for i in range(N):
    a = input()
    a = list(a)
    A.append(a)
ans = -1
for i in range(N):
    for j in range(N):
        for d in dirs:
            ny = i
            nx = j
            tmp = A[ny][nx]
            for _ in range(N - 1):
                ny = (ny + d[0]) % N
                nx = (nx + d[1]) % N
                tmp += A[ny][nx]
            tmp = int(tmp)
            ans = max(ans, tmp)
print(ans)
