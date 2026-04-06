# オリジナルの物だけ残しておき、その中からmaxを探す
# ソートの順番を引数によって変えたい -> -1をかける
N = int(input())
original_strings = set()
ranked_strings = []
for i in range(N):
    S, T = map(str, input().split())
    T = int(T)
    if not S in original_strings:
        original_strings.add(S)
        ranked_strings.append([T, -(i + 1)])
ranked_strings.sort(reverse=True)
ans = (-1) * ranked_strings[0][1]
print(ans)
