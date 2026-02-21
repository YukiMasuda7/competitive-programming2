# 割り算のmod計算(nCk % modなど)は計算がネック

# 今回もネックはnCaとnCb
# math.comb(n, a) などの「階乗を直接計算する方法」は
# nが大きすぎてTLEやメモリエラーになります。

# 1. 逆元とは？
# mod m に対して a ✖︎ b ≡ 1 となるbを「aの逆元」という
# つまり、「aで割る」ということは「aの逆元を掛ける」ことと同じ

# 2. なぜ必要？
# (a+b)%mod = a%mod + b%mod（引き算、掛け算も同じ）
# しかし割り算にはこれができない (そもそもa/bがintとは限らない)
# よって(a/b)%modの代わりにa*B%mod(Bはbの逆元)を用いる


# 3. どうやって求める？
# m が素数なら「フェルマーの小定理」で
# a**(mod - 2) % mod
# がaの逆元
# python では　pow(a, m-2, m)　で書ける


def comb_large_n(n, k, mod):
    res = 1
    for i in range(k):
        res = res * (n - i) % mod
        res = res * pow(i + 1, mod - 2, mod) % mod  # 逆元で割る
    return res
