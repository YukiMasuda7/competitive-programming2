import itertools

S, K = map(str, input().split())
K = int(K)
P = itertools.permutations(S, len(S))
PP = [p for p in P]
PP = list(set(PP))
PP.sort()
print("".join(PP[K - 1]))
