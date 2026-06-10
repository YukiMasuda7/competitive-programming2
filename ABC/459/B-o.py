N = int(input())
ans = ""
S = list(map(str, input().split()))
for s in S:
    x = s[0]
    if x == "a" or x == "b" or x == "c":
        ans += "2"
    elif x == "d" or x == "e" or x == "f":
        ans += "3"
    elif x == "g" or x == "h" or x == "i":
        ans += "4"
    elif x == "j" or x == "k" or x == "l":
        ans += "5"
    elif x == "m" or x == "n" or x == "o":
        ans += "6"
    elif x == "p" or x == "q" or x == "r" or x == "s":
        ans += "7"
    elif x == "t" or x == "u" or x == "v":
        ans += "8"
    elif x == "w" or x == "x" or x == "y" or x == "z":
        ans += "9"
print(ans)
