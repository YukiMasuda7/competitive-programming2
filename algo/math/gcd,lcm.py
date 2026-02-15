# 最小公倍数を求める問題
# A,Bをそれらの最大公約数gcd(A,B)で割った値をそれぞれa,bとするとき
# 最小公倍数lcm(A,B) = a*b*gcd(A,B) = A*B//gcd(A,B)である

# gcdはmathにある
# 0から√max(A,B)の範囲でA%i,B%i==0の判定でもいける
import math


def lcm(A, B):
    return (A * B) // math.gcd(A, B)
