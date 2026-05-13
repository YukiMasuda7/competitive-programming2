# 明らかにdpっぽい
# dp[i]: i段目への到達方法の数

N,L=map(int,input().split())
dp=[0]*(L+1)
dp[0]=1
for i in range(1, L+1):
    