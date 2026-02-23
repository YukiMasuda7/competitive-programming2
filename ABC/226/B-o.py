N = int(input())
set_A = set()
for i in range(N):
    X = list(map(int, input().split()))
    set_A.add(tuple(X[1:]))
print(len(set_A))
