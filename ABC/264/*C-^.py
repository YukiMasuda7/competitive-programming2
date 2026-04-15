# 削除の決め方は高々20回なので2**20=10**6
# 消してない行、列を復元してBと一致するかを調べる
# 残った行や列を座標圧縮してBのindexの範囲に揃える
# Xdict = {x:i+1 for i,x in enumerate(sorted(list(set(X))))}


H1, W1 = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H1)]
H2, W2 = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H2)]

for mask in range(1 << H1 + W1):
    row = []
    col = []
    del_row = []
    del_col = []
    for shift in range(H1 + W1):
        if mask >> shift & 1:
            if shift < H1:
                del_row.append(shift)
            else:
                del_col.append(shift - H1)
        else:
            if shift < H1:
                row.append(shift)
            else:
                col.append(shift - H1)

    if not (H1 - len(del_row) == H2 and W1 - len(del_col) == W2):
        continue

    row_dict = {x: i for i, x in enumerate(sorted(list(set(row))))}
    col_dict = {x: i for i, x in enumerate(sorted(list(set(col))))}

    ok = True
    for rd in row_dict:
        for cd in col_dict:
            if A[rd][cd] != B[row_dict[rd]][col_dict[cd]]:
                ok = False
                break
        if not ok:
            break

    if ok:
        print("Yes")
        exit()

print("No")
