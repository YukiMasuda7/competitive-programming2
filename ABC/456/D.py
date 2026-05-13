# その要素よりも含め右側にあるa, b, cの数を管理？

mod = 998244353
S = input()
l = len(S)
total = {"a": 0, "b": 0, "c": 0}
cnt = {"a": 0, "b": 0, "c": 0}
for i in range(l - 1, -1, -1):
    cnt[S[i]] += 1
    if i == l - 1:
        total[S[i]] += 1
    else:
        total[S[i]] *= 2
        for j in total:
            if S[i] != j:
                total[S[i]] += total[j]
        total[S[i]] += 1
        print(i, j, S[i], j)
        print("total:" + str(total))
        print("cnt:" + str(cnt))
