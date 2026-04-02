# いい整数は9桁までなのでNの範囲は小さくて済むはず
# 2**10が1024
# 2**0から2**30までの数を組み合わせればいい
# 選び方はbit全探索？
nums=set()

for mask in range(1<<20):
    num=""
    for shift in range(20):
        if mask >> shift & 1:
            num+=str(2**shift)