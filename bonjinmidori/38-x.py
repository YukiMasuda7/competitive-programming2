# bit全探索
# Aの各要素の間に区切りを入れる、入れないの2択
# -> bit全探索っぽい
# N<=20と小さいことからも勘付ける

# 空の区間を作ってはダメなので、
# 要素n子に対してn-1この区切りが必要
# 2**19 = 10**6くらいなのでOK

# or  : |
# xor : ^

# A[0]の右の仕切りを0番とする
ans = 2**40
N = int(input())
A = list(map(int, input().split()))
for i in range(1 << (N)):
    sep = []
    for shift in range(N):
        if i >> shift & 1:
            sep.append(shift)

    if not sep:
        continue
    else:
        group = []
        group.append(A[: sep[0] + 1])
        for j in range(len(sep) - 1):
            group.append(A[sep[j] + 1 : sep[j + 1] + 1])
        group.append(A[sep[len(sep) - 1] + 1 :])

        ORs = []
        for g in group:
            if len(g) == 1:
                ORs.append(g[0])
            else:
                tmp = 0
                for k in range(len(g)):
                    tmp = tmp | g[k]
                ORs.append(tmp)

        tmp_ans = ORs[0]
        for l in range(1, len(ORs)):
            tmp_ans = tmp_ans ^ ORs[l]

        ans = min(ans, tmp_ans)

print(ans)
