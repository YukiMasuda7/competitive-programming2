# 実際の入れ替えは間に合わない
N, Q = map(int, input().split())
A = list(map(int, input().split()))
shift = 0
ans = []
ind = [i for i in range(N)]
for i in range(Q):
    T, x, y = map(int, input().split())
    x -= 1
    y -= 1
    if T == 1:
        A[(y + shift) % N], A[(x + shift) % N] = (
            A[(x + shift) % N],
            A[(y + shift) % N],
        )

    elif T == 2:
        # 右シフトした後のindexがxなので元の数列では-shift前を参照すべき
        shift -= 1
    else:
        ans.append(A[(x + shift) % N])
for a in ans:
    print(a)
