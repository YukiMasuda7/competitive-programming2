K = int(input())
if K >= 60:
    H = "22"
else:
    H = "21"

if K % 60 < 10:
    M = "0" + str(K % 60)
else:
    M = str(K % 60)

ans = H + ":" + M
print(ans)
