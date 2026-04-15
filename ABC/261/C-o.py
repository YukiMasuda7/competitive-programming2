N = int(input())
d = dict()
for i in range(N):
    S = input()
    if S not in d:
        print(S)
        d[S] = 0
    else:
        d[S] += 1
        print(S + "(" + str(d[S]) + ")")
