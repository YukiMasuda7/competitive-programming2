# 行をbit全探索→2**8=196なので列を全探索しても間に合う
# 選んだ全て行について、全て同じ数字の書かれている列の数を数える
from collections import defaultdict

H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]
ans = -1
for mask in range(2**H):
    row = []
    for shift in range(H):
        if mask >> shift & 1:
            row.append(shift)

    l = len(row)
    num_count = defaultdict(int)
    for c in range(W):
        is_all_same = True

        if l == 0:
            is_all_same = False
        elif l == 1:
            num_count[P[row[0]][c]] += 1
        else:
            for r in range(1, l):
                if P[row[r]][c] != P[row[r - 1]][c]:
                    is_all_same = False
            if is_all_same:
                num_count[P[row[0]][c]] += l
    if num_count:
        ans = max(ans, max(num_count.values()))
print(ans)
