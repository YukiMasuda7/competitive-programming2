S, T, X = map(int, input().split())
if S < T:
    if S <= X < T:
        ans = "Yes"
    else:
        ans = "No"
else:
    if S <= X or X < T:
        ans = "Yes"
    else:
        ans = "No"
print(ans)
