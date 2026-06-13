# N<=10**3なのでO(N**2)でも間に合う
# 6連続作れるかの判定はqueが良さそう
# 斜めの探索がムズイから却下

# 各マスを6連続の端として右、下、右下, 左下のそれぞれ6マスを参照する

N = int(input())
S = [input() for _ in range(N)]

dir = [[0, 1], [1, 0], [1, 1], [1, -1]]


def six_combo(pos, dir):
    ny = pos[0]
    nx = pos[1]
    for dy, dx in dir:
        cnt = 0
        flag = True
        for i in range(6):
            y = ny + dy * i
            x = nx + dx * i

            if not (0 <= y < N and 0 <= x < N):
                flag = False
                break

            if S[y][x] == "#":
                cnt += 1

        if flag and cnt >= 4:
            return True

    return False


for i in range(N):
    for j in range(N):
        if six_combo([i, j], dir):
            print("Yes")
            exit()

print("No")
