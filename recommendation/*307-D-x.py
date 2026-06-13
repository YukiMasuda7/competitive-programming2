# よく見る"("と")"の問題
# 括弧列はスタックと相性がよい
# "("と英小文字はpush、")"が来たら"("までをpop->内側から消えていく
# しかし"("が0この状態では消せないので注意
from collections import deque

N = int(input())
S = input()
stack = deque([])
cnt = 0
for i in range(N):
    if S[i] != ")":
        stack.append(S[i])
        if S[i] == "(":
            cnt += 1
    else:
        if cnt != 0:
            while stack[-1] != "(":
                stack.pop()
            stack.pop()
            cnt -= 1
        else:
            stack.append(")")

print("".join(stack))
