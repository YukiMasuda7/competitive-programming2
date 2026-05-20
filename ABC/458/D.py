# 毎回ソートしてたら間に合わない

# 一回全てを格納してから２つずつ消していく？(答えを逆から求める)
# 中央値より大きいのが2つなら中央値のindは-1

X = int(input())
Q = int(input())
mean = [-(10**10), -(10**10), X, 10**10, 10**10]
for i in range(Q):
    A, B = map(int, input().split())
    mean.append(A)
    mean.append(B)
    mean.sort()
    mean = mean[1:6]
    print(mean[2])
