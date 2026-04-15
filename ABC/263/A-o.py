X = list(map(int, input().split()))
X.sort()
if X[0] == X[1] and X[1] != X[2] and X[2] == X[3] == X[4]:
    print("Yes")
elif X[4] == X[3] and X[3] != X[2] and X[2] == X[1] == X[0]:
    print("Yes")
else:
    print("No")
