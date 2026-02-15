N = int(input())

ans = []
q = N
while q != 1:
    r = q % 2
    q = q // 2
    ans.append(str(r))
ans.append("1")
ans.reverse()
ans = ["0"] * (10 - len(ans)) + ans
ans = "".join(ans)
print(ans)
