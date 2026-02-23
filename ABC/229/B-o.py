# 下の桁から各桁に注目していけばいい
A, B = map(str, input().split())
A = A[::-1]
B = B[::-1]
m = min(len(A), len(B))
for i in range(m):
    if int(A[i]) + int(B[i]) >= 10:
        print("Hard")
        exit()
print("Easy")
