# O(N**4)じゃ間に合わない
# 半分全列挙

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

ans = 0

S = set()
T = set()
for i in range(N):
    for j in range(N):
        S.add(A[i] + B[j])
        T.add(C[i] + D[j])

for s in S:
    if K - s in T:
        print("Yes")
        exit()
print("No")
