N = int(input())
ans = ""
for i in range(N, 0, -1):
    if i != 1:
        ans += str(i) + ","
    else:
        ans += str(i)
print(ans)
