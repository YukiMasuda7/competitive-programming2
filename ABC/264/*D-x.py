# 転倒数
# 交点の数が入れ替えの数(転倒数)
# ABC264-D解説放送

S = input()
T = "atcoder"

rank = {ch: i for i, ch in enumerate(T)}  # {'a':0, 't':1, 'c':2, ...}
P = [rank[ch] for ch in S]  # 例: "tacoder" -> [1,0,2,3,4,5,6]

ans = 0
n = len(P)
for i in range(n):
    for j in range(i + 1, n):
        if P[i] > P[j]:
            ans += 1

print(ans)
