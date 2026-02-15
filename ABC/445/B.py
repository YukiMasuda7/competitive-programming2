N = int(input())
A = []
m = -1
for i in range(N):
    s = input()
    A.append(s)
    m = max(m, len(s))

for a in A:
    x = (m - len(a)) // 2
    print("." * x + a + "." * x)
