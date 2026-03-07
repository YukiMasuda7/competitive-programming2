# Bの左にあるAの数、右にあるCの数を管理する必要がある？
# ↑違う

# 今回は先頭からSを見ていき、ABCを作れるなら作る(貪欲法)

# A,B,Cの数をcntA, cntB, cntCとする
# Sを先頭から見ていく
# Aは全て数える
# cntBはそこまでのBの累積数とそこまでのcntAの小さいほう↓
# cntA>=cntBならcntB個のAB、cntA<cntBならcntA個のABを作れる

# ABとCについても同様
# 答えはCの採用数になる

S = input()
A = 0
B = 0
C = 0
for s in S:
    if s == "A":
        A += 1
    elif s == "B":
        B = min(A, B + 1)
    else:
        C = min(B, C + 1)
print(C)
