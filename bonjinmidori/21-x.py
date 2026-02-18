# 条件を満たす中でのmax, minを求める問題
# 答えの候補をfor文で回して条件を満たすかチェクする
# A,Bを回すのではなく答えXを回す
# 一個当たりの重さ（平均の重さW*1000/Xグラム）がAからBの範囲にあればよい
# つまりA*X<=1000*W<=B*Xが成立すれば条件を満たす
# B=1,W=1000の時のXがmaxであり、X<=10**6で回せば十分

A, B, W = map(int, input().split())
min_ans = 10**15
max_ans = 10**-15

for X in range(1, 10**6 + 1):
    if A * X <= W * 1000 <= B * X:
        min_ans = min(min_ans, X)
        max_ans = max(max_ans, X)

if min_ans == 10**15:
    print("UNSATISFIABLE")
else:
    print(min_ans, max_ans)
