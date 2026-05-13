# A,B,Cの要素をmod46であらかじめ仕分ける
# 46**3に落とし込む

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
a = [0] * 46
b = [0] * 46
c = [0] * 46
for i in range(N):
    a[A[i] % 46] += 1
    b[B[i] % 46] += 1
    c[C[i] % 46] += 1
ans = 0
l = 46
for i in range(l):
    for j in range(l):
        for k in range(l):
            if (i + j + k) % l == 0:
                ans += a[i] * b[j] * c[k]
print(ans)
