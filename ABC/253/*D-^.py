# 包除原理
# AとBの倍数はlcm(A, B)の倍数
import math

N, A, B = map(int, input().split())
AB = math.lcm(A, B)
# それぞれ何個あるかを計算
a = N // A
b = N // B
ab = N // AB
# 等比級数の和を計算 x + 2x + ... jx =(1/2)*(項数)*(初項+末項)
aa = (1 + a) * a * A // 2
bb = (1 + b) * b * B // 2
aabb = (1 + ab) * ab * AB // 2
s = (1 + N) * N // 2
ans = s - (aa + bb - aabb)
print(ans)
