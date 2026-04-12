N = int(input())
S = input()
if S[0] != "o":
    print(S)
    exit()
else:
    end = 0
    for i in range(1, N):
        if S[i] == "o":
            end += 1
        else:
            if end == N - 1:
                print("")
                exit()
            else:
                print(S[end + 1 :])
                exit()
