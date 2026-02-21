# 尺取り法っぽい -> l,rを動かすごとにその区間のmax,minを更新していけばいい？
# セグ木は -> それぞれのノードに[min, max]を持たせる
# ↑セグ木だと結局l,rの全探索をするしかないので間に合わない

N, D = map(int, input().split())
A = list(map(int, input().split()))
