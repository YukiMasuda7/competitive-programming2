S = input()
T = "oxx" * 100
for i in range(3):
    if S == T[i : i + len(S)]:
        print("Yes")
        exit()
print("No")
