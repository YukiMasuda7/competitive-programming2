N, M = map(int, input().split())
for i in range(1, M + 1):
    if 2 * i - 1 > N:
        print("No")
        exit()
print("Yes")
