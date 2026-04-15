def judge(i, j):
    if A[i][j] == "D" and A[j][i] == "D":
        return True
    if A[i][j] == "W" and A[j][i] == "L":
        return True
    if A[i][j] == "L" and A[j][i] == "W":
        return True
    return False


N = int(input())
A = []
for i in range(N):
    a = input()
    a = list(a)
    A.append(a)
for i in range(N):
    for j in range(i + 1, N):
        if not judge(i, j):
            print("incorrect")
            exit()
print("correct")
