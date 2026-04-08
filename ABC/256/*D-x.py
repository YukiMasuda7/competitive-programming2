# 区間同士のたし算
# 区間の重なりの数を数える(imos法)
# 1以上なら区間が存在する
# [L, R)なのでRを含めない
# -> A[R+1]-=1だと弊区間になって誤り

N = int(input())
# 左端、右端を余分に作っておく
A = [0] * (2 * 10**5 + 2)
for i in range(N):
    L, R = map(int, input().split())
    A[L] += 1
    A[R] -= 1
for i in range(1, 2 * 10**5 + 2):
    A[i] += A[i - 1]
ans = []
flag = False
for i in range(2 * 10**5 + 1):
    if A[i] != 0 and not flag:
        l = i
        flag = True
    elif A[i] == 0 and flag:
        # 今区間の右端Rはカウントしていないので、0になった初めのところが開区間の右端
        r = i
        ans.append([l, r])
        flag = False
for a in ans:
    print(*a)
