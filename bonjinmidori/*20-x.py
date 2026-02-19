# もじを直接入れ替えるとO(NQ)で間に合わない
# 要素の入れ替え x, y = y, x
# クエリ2の入れ替えがネック。クエリ2の通常状態と入れ替え状態でのクエリ1の挙動が変化することに着目する

N = int(input())
S = input()
Q = int(input())

S = "0" + S
S = list(S)
flip = False
for i in range(Q):
    T, A, B = map(int, input().split())
    if T == 1:
        if not flip:
            S[A], S[B] = S[B], S[A]
        else:
            if A <= N:
                A += N
            else:
                A -= N
            if B <= N:
                B += N
            else:
                B -= N
            S[A], S[B] = S[B], S[A]
    else:
        flip = not flip

if not flip:
    ans = S[1:]
else:
    ans = S[N + 1 :] + S[1 : N + 1]
print("".join(ans))
