# 最小公倍数を求める問題
# A,Bをそれらの最大公約数gcd(A,B)で割った値をそれぞれa,bとするとき
# 最小公倍数lcm(A,B) = a*b*gcd(A,B) = A*B//gcd(A,B)である

import math


def lcm(A, B):
    return (A * B) // math.gcd(A, B)


A, B = map(int, input().split())
print(lcm(A, B))
