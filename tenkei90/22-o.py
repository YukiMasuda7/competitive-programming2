# 1辺が最大公約数の長さの立方体になる？
import math

A, B, C = map(int, input().split())
l = math.gcd(A, B)
l = math.gcd(l, C)
ans = A // l + B // l + C // l - 3
print(ans)
