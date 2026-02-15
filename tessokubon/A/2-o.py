n, x = map(int, input().split())
A = list(map(int, input().split()))
for a in A:
    if a == x:
        print("Yes")
        exit()
print("No")
