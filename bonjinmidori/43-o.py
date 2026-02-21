# 77=70+7なので77%Kは
# (7%K +(7*10)%K)%K = (7%K + (7%K)*(10%K))%Kである
# 777=770+7なので777%Kは
# (7%K +(77*10)%K)%K = (7%K + (77%K)*(10%K))%Kである

# これで　O(N)でmodKの値が出せる
K = int(input())
modK = [0] * 10**6
modK[1] = 7 % K
for i in range(2, 10**6):
    modK[i] = (7 % K + (modK[i - 1]) * (10 % K)) % K
for i in range(1, 10**6):
    if modK[i] == 0:
        print(i)
        exit()
print(-1)
