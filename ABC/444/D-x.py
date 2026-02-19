# いちいちBiを作成すると間に合わない
# imosで+1,-1のみしておく

N = int(input())
A = list(map(int, input().split()))
l = max(A) + 1
C = [0] * (l)
C[0] = N
for i in range(N):
    C[A[i]] -= 1
CC = [0] * (l)
CC[0] = N
for i in range(1, l):
    CC[i] = CC[i - 1] + C[i]
ans = []
for i in range(1, l):
    ans.append(str(CC[i - 1] % 10))
    CC[i] += CC[i - 1] // 10

# 最後C[l-1]に123456みたいな大きな数が貯まる可能性があるので、それを処理
num = CC[l - 1]
while num > 0:
    ans.append(str(num % 10))
    num //= 10

ans = ans[::-1]
print("".join(ans))
