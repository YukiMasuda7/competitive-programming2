X = input()
Y = [0] * 4
for i in range(4):
    Y[i] = int(X[i])

if len(set(Y)) == 1:
    print("Weak")
    exit()

for i in range(3):
    if Y[i + 1] != (Y[i] + 1) % 10:
        print("Strong")
        exit()
print("Weak")
