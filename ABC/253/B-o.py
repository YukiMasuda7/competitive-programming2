# マンハッタン距離
H, W = map(int, input().split())
S = []
for i in range(H):
    s = input()
    s = list(s)
    S.append(s)
tokens = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            tokens.append([i, j])
ans = abs(tokens[0][0] - tokens[1][0]) + abs(tokens[0][1] - tokens[1][1])
print(ans)
