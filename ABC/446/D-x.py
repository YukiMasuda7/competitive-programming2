# i番目に小さい数がどこにあるかを管理
N = int(input())
A = list(map(int, input().split()))
# i番目に小さい数は何か
H = [0] * (N)
for i in range(N):
    H[i] = A[i]
H = list(set(H))

# i番目に小さい数はどこにあるか？
pos = [[] for _ in range(len(H))]
for i in range(N):
    pos[H.index(A[i])].append(i)
