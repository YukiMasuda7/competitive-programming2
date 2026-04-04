# 独自のソートルールの定義
X = input()
N = int(input())
S = [input() for _ in range(N)]

newdict = {}
for i in range(26):
    newdict[X[i]] = i

# １文字列sを比較用の数列に変換してからsort

S.sort(key=lambda s: [newdict[c] for c in s])

for a in S:
    print(a)
