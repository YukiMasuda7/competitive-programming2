# 角から詰めて配置していくのが最大？
# 幅1の時は制限がないことに注意
H, W = map(int, input().split())
cnt = 0
if H == 1 or W == 1:
    cnt = H * W
else:
    for i in range(H):
        for j in range(W):
            if i % 2 == 0 and j % 2 == 0:
                cnt += 1
print(cnt)
