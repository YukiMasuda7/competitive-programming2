N, X = map(str, input().split())
N = int(N)
d = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
x = d[X]
for i in range(N):
    S = input()
    if S[x] == "o":
        print("Yes")
        exit()
print("No")
