# N,M<=10なので全探索でいい
# しかしforの回数は可変なので再帰？
# combinationsで行ける
import itertools

N, M = map(int, input().split())
nums = [i for i in range(1, M + 1)]
ans = itertools.combinations(nums, N)
for a in ans:
    print(*a)
