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

# ----------------------------------


# 素因数分解
# O(√N)
def prime_factorize(N):
    if N == 1:
        return [1]
    prime_list = []
    i = 2
    while i * i <= N:
        if N % i == 0:
            prime_list.append(i)
            N //= i
        else:
            i += 1
    if N != 1:
        prime_list.append(N)
    return prime_list


# ---------------------------------

# 高速版 凡人49
# O(log(X))
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
