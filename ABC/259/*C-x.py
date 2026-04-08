# ランレングス圧縮のような感じ？
# 圧縮の結果が同じならYes
# x*i (i>=3)をxxに圧縮
# 実際に圧縮していくと間に合わない

S = input() + "#"
T = input() + "#"

RS = []
RT = []
S_combo = 1
T_combo = 1
for i in range(1, len(S)):
    if S[i] != S[i - 1]:
        RS.append((S[i - 1], S_combo))
        S_combo = 1
    else:
        S_combo += 1

for i in range(1, len(T)):
    if T[i] != T[i - 1]:
        RT.append((T[i - 1], T_combo))
        T_combo = 1
    else:
        T_combo += 1
if len(RS) != len(RT):
    print("No")
    exit()
else:
    for i in range(len(RS)):
        if RS[i][0] != RT[i][0]:
            print("No")
            exit()
        else:
            if RS[i][1] == RT[i][1]:
                continue
            elif RS[i][1] > RT[i][1]:
                print("No")
                exit()
            else:
                if RS[i][1] == 1:
                    print("No")
                    exit()
print("Yes")
