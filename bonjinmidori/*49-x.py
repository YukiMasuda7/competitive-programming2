# 高速因数分解の問題(エラトステネスの篩も似たことをしていたような...)
# 普通の因数分解(1から√Xまで割れるかチェック)は
# O(√X)
# 今回の方法だと
# O(logX)

# 以下で求めるD(X)を使って素因数分解する
# (1)Xの素因数のうち最小のものD(X)をX=2~Nまで格納
#    -> D(2*1)=2, D(2*2)=2, D(2*3)=2
#       D(3*1)=3, D(3*2)=3, D(3*3)=3
#       ...
# 4**1 = 2**2 だが2**2の時点で最小の素因数2を書き込んでいるので更新しない

# a*i (2<= a <=N)がNを超えるまで求めていく。
# よって計算量は
#   N/2 + N/3 + ... + N/N
# < N/1 + N/2 + ... + N/N
# < ∮N/k(区分求積法)
# = NlnN ≒ NlogN
# (ln = logN / loge = 2.3logN、オーダー記法では定数倍は意味をなさない)
# ↑logの底、10である

# 素因数分解の方法
# X=1となるまで1,2を繰り返す
# (1)D(X)を素因数として記録
# (2)XをD(X)で割る

# ----------------------------------------------------------------

# 1. 要素内の任意のペアのgcd=1 -> pairwise coprime
# 2. 要素内の任意のペアのgcd!=1 かつ 全ての要素のgcd=1
#    ->setwise coprim
# 3. それ以外

# math.gcd(a,b)の計算量はユークリッド互除法に基づき
# O(log(min(a,b)))
# a,b<10**6
# なので、高々20程度

# a,bの全探索じゃあ間に合わない

# 全ての要素のgcdはO(N)で求まる

# Aiの約数列挙(O(N√N))をして -> 10**9で間に合わない

# 今回は素因数の種類が分かればいい(指数部分はいらない)ので
# setでよい
# a,bの二重for文では間に合わないので
# その素因数がすでに使われているかどうかをbool値で管理する

import math

N = int(input())
A = list(map(int, input().split()))
# 全ての要素のgcdをチェック
all_gcd = A[0]
for i in range(1, N):
    all_gcd = math.gcd(A[i], all_gcd)

# 任意のペアのgcdが1かチェックする(1ならflag==False)
flag = False
# 2<=X<=NのD(X)を作っておく
D = [0] * (10**6 + 1)
for i in range(2, 10**6 + 1):
    if D[i] != 0:
        continue
    for j in range(1, 10**6 + 1):
        if i * j < 10**6 + 1:
            if D[i * j] == 0:
                D[i * j] = i
        else:
            break


def fast_prime_fact(x):
    prime = []
    while 1 < x:
        prime.append(D[x])
        x //= D[x]
    return prime


prime_used = [False] * (10**6 + 1)
# A[i]を素因数分解していく
for i in range(N):
    prime_list = fast_prime_fact(A[i])
    prime_set = set(prime_list)
    for p in prime_set:
        if not prime_used[p]:
            prime_used[p] = True
        else:
            flag = True

if not flag:
    print("pairwise coprime")
else:
    if all_gcd == 1:
        print("setwise coprime")
    else:
        print("not coprime")
