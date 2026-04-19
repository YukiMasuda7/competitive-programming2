N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
for i in range(N):
    cnt += abs(A[i] - B[i])


flag = False
if cnt == K:
    flag = True
elif cnt < K and (cnt - K) % 2 == 0:
    flag = True
if flag:
    print("Yes")
else:
    print("No")
