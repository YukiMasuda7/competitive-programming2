N = int(input())
if N >= 42:
    ans = "AGC" + "0" * (3 - len(str(N + 1))) + str(N + 1)
else:
    ans = "AGC" + "0" * (3 - len(str(N + 1))) + str(N)
print(ans)
