# Nの約数列挙問題
# N √Nまで調べれば十分

N = int(input())
ans = []
for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
        if i != N // i:
            ans.append(i)
            ans.append(N // i)
        else:
            ans.append(i)
ans.sort()
for a in ans:
    print(a)
