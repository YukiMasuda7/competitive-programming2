# 実際に消すのではなく、元の文字列の先頭が変わっていくだけ
N, Q = map(int, input().split())
S = input()
head = 0
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        head = (head + q[1]) % N
    else:
        q[1] -= 1
        print(S[(q[1] - head) % N])
