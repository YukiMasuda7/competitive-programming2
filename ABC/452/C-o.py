N = int(input())
sakotu = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
# 文字列の長さごとに格納
# strigs[i][j]: 長さiの文字列のj番目の文字
strings = [[set() for _ in range(11)] for _ in range(11)]
T = []
for i in range(M):
    S = input()
    T.append(S)
    l = len(S)
    for j in range(l):
        strings[l][j + 1].add(S[j])

for i in range(M):
    flag = True
    l = len(T[i])
    if l != N:
        flag = False
    else:
        for j in range(N):
            if not T[i][j] in strings[sakotu[j][0]][sakotu[j][1]]:
                flag = False
    if flag:
        print("Yes")
    else:
        print("No")
