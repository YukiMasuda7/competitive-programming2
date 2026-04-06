N, W = map(int, input().split())
A = list(map(int, input().split()))
nums = set()
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if A[i] + A[j] + A[k] <= W:
                nums.add(A[i] + A[j] + A[k])

for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i] + A[j] <= W:
            nums.add(A[i] + A[j])
for i in range(N):
    if A[i] <= W:
        nums.add(A[i])
print(len(nums))
