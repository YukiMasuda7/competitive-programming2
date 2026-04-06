M, D = map(int, input().split())
ans = False
if M == 1 and D == 7:
    ans = True
elif M == 3 and D == 3:
    ans = True
elif M == 5 and D == 5:
    ans = True
elif M == 7 and D == 7:
    ans = True
elif M == 9 and D == 9:
    ans = True

if ans:
    print("Yes")
else:
    print("No")
