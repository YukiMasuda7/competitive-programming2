H, W, X, Y = map(int, input().split())
G = [list(input()) for _ in range(H)]
X -= 1
Y -= 1
ans = 1
u = d = l = r = 1
while Y + r < W and G[X][Y + r] == ".":
    ans += 1
    r += 1
while 0 <= Y - l and G[X][Y - l] == ".":
    ans += 1
    l += 1
while X + d < H and G[X + d][Y] == ".":
    ans += 1
    d += 1
while 0 <= X - u and G[X - u][Y] == ".":
    ans += 1
    u += 1
print(ans)
