# 左右それぞれからの今までの最大値を管理すればいい

N = int(input())
A = list(map(int, input().split()))
D = int(input())
LM = [A[0]] * N
RM = [A[-1]] * N
for i in range(N - 1):
    LM[i + 1] = max(LM[i], A[i + 1])
    RM[-(i + 2)] = max(RM[-(i + 1)], A[-(i + 2)])
for i in range(D):
    L, R = map(int, input().split())
    L -= 1
    R -= 1
    ans = max(LM[L - 1], RM[R + 1])
    print(ans)
