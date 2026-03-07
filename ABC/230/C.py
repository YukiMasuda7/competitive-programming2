# 実装が大変な問題
# ↓黒く塗る範囲の全探索では間に合わない

# N, A, B = map(int, input().split())
# P, Q, R, S = map(int, input().split())

# a = max(1 - A, 1 - B)
# b = min(N - A, N - B)
# c = max(1 - A, B - N)
# d = min(N - A, B - 1)
# ans = [["."] * (S - R + 1) for _ in range(Q - P + 1)]
# for i in range(a, b + 1):
#     if P <= A + i <= Q and R <= B + i <= S:
#         ans[A + i - P][B + i - R] = "#"

# for i in range(c, d + 1):
#     if P <= A + i <= Q and R <= B - i <= S:
#         ans[A + i - P][B - i - R] = "#"
# for i in range(Q - P + 1):
#     print("".join(ans[i]))


# 出力範囲の各マス
N, A, B = map(int, input().split())
P, Q, R, S = map(int, input().split())

for i in range(P, Q + 1):
    row = []
    for j in range(R, S + 1):
        # 斜め（A+B同時増加）
        if max(1 - A, 1 - B) <= i - A <= min(N - A, N - B) and j - B == i - A:
            row.append("#")
        # 斜め（A増加B減少）
        elif max(1 - A, B - N) <= i - A <= min(N - A, B - 1) and j - B == -(i - A):
            row.append("#")
        else:
            row.append(".")
    print("".join(row))