N, K, Q = map(int, input().split())
A = [0] + list(map(int, input().split()))
L = [0] + list(map(int, input().split()))
pos = [0] * (K + 1)

for i in range(1, K + 1):
    pos[i] = A[i]

for i in range(1, Q + 1):
    if pos[L[i]] == N:
        continue
    if L[i] != K:
        if pos[L[i] + 1] == pos[L[i]] + 1:
            continue
    pos[L[i]] += 1

for i in range(1, K + 1):
    print(pos[i])
