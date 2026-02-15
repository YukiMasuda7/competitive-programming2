N = int(input())
mountains = []
for i in range(N):
    S, T = map(str, input().split())
    mountains.append([int(T), S])
mountains.sort(reverse=True)
print(mountains[1][1])
