# 最大フロー問題:
# 容量付き有向グラフにおいて、
# 始点 s から 終点 t へ流せる「流量」の最大値

# 残余グラフ:
# 辺に対して
# f流すとするとき
# 順方向に流すと +f
# 逆方向に流すと -f
# になるようなグラフ。
# 先に間違った経路で流してしまった場合、
# 逆辺がないと「戻して別ルートに流す」ができない。

# Ford-Fulkerson法:
# 1. 残余グラフ上の(残り容量0の辺を通らない)スタートかゴールまでのパスを見つける
# 2. パス上の辺のうち最小流量の辺と同じ流量Fだけパスに流す。
#    (逆方向の流量は -F であることに注意)
# 3. 1のパスが見つからなくなるまで1, 2を繰り返す

# 最小カット定理: 最小カットのコストが最大フローと一致する。
# 最小カット: 始点 s と終点 t を「分断する」辺の集合のうち、
# その容量の合計が最小になるもの


# 最大フロー用の辺の構造体
class maxflow_edge:
    def __init__(self, to, cap, rev):
        self.to = to      # 行き先ノード
        self.cap = cap    # 残余容量
        self.rev = rev    # 逆辺（戻り）のインデックス


# 深さ優先探索
def dfs(pos, goal, F, edges, used):
    if pos == goal:
        return F  # ゴールに到着：フローを流せる！
    # 探索する
    used[pos] = True
    for e in edges[pos]:
        # 容量が 1 以上でかつ、まだ訪問していない頂点にのみ行く
        if e.cap > 0 and not used[e.to]:
            flow = dfs(e.to, goal, min(F, e.cap), edges, used)
            # フローを流せる場合、åç残余グラフの容量を flow だけ増減させる
            if flow >= 1:
                e.cap -= flow
                edges[e.to][e.rev].cap += flow
                return flow
    # すべての辺を探索しても見つからなかった…
    return 0


#  頂点 s から頂点 t までの最大フローの総流量を返す（頂点数 N、辺のリスト edges）
def maxflow(N, s, t, edges):
    # 初期状態の残余グラフを構築
    # （ここは書籍とは少し異なる実装をしているため、8 行目は edges[a] に追加された後なので len(edges[a]) - 1 となっていることに注意）
    edges = [list() for i in range(N + 1)]
    for a, b, c in edges:
        # 逆辺（b→a）がedges[b]に追加される予定なので、そのインデックスは「edges[b]の長さ（=追加前の末尾）」
        edges[a].append(maxflow_edge(b, c, len(edges[b])))
        # 逆辺（a→b）は直前にedges[a]に追加されたばかりなので、そのインデックスは「edges[a]の末尾（=len(edges[a])-1）」
        edges[b].append(maxflow_edge(a, 0, len(edges[a]) - 1))
    INF = 10**10
    total_flow = 0
    while True:
        used = [False] * (N + 1)
        F = dfs(s, t, INF, edges, used)
        if F > 0:
            total_flow += F
        else:
            break  # フローを流せなくなったら、操作終了
    return total_flow


# 入力
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(M)]

# 答えを求めて出力
answer = maxflow(N, 1, N, edges)
print(answer)
