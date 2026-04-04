# bit全探索でどの数字をA,Bに割り振るかを決めて
# A,Bそれぞれで要素を昇順にしてかければいい(大きい数同士をかければ積も大きくなる)
N = input()
N = list(N)
ans = -1
for mask in range(1 << len(N)):
    A = []
    B = []
    for shift in range(len(N)):
        if mask >> shift & 1:
            A.append(N[shift])
        else:
            B.append(N[shift])
    if not len(A) or not len(B):
        continue

    A.sort(reverse=True)
    B.sort(reverse=True)

    a = int("".join(A))
    b = int("".join(B))
    ans = max(ans, a * b)
print(ans)
