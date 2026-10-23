"""Re-derive R's edge list from the original PostScript of Figure 1 (sources/tex/RGraph.ps).

Each stroked path 'x0 y0 m ... (l|c) S' is one edge; its first and last points are node centres.
Node labels: NODE_XY in graphs.py (read from the rendered figure). Checks: 27 strokes, all endpoints
are node centres, the set equals R_EDGES, the BCDRV fractional clique cover uses only cliques of R^-,
and R^- = R - {9,10}.
"""
import re, sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import NODE_XY, R_EDGES, R_MINUS_EDGES, adjacency

ps = open(os.path.join(os.path.dirname(__file__), "..", "sources", "tex", "RGraph.ps")).read()
body = ps.split("%%EndPageSetup", 1)[1]
strokes = re.findall(r"cm\s+([-\d.]+)\s+([-\d.]+)\s+m\s+(.*?)\s+S\s+Q", body, re.S)
def node_at(x, y):
    for v, (a, b) in NODE_XY.items():
        if abs(a - x) < 0.01 and abs(b - y) < 0.01:
            return v
    return None
edges = set(); bad = []
for x0, y0, rest in strokes:
    nums = re.findall(r"[-\d.]+", rest)
    x1, y1 = float(nums[-2]), float(nums[-1])
    a, b = node_at(float(x0), float(y0)), node_at(x1, y1)
    if a is None or b is None: bad.append((x0, y0, x1, y1)); continue
    edges.add(tuple(sorted((a, b))))
ok = (len(edges) == 27 and len(strokes) - len(bad) == 27 and edges == set(tuple(sorted(e)) for e in R_EDGES))
# any stroke not joining two node centres must be a degenerate (zero-length) glyph artefact, not an edge
degenerate_only = all(abs(float(a) - c) < 1e-6 and abs(float(b) - d) < 1e-6 for a, b, c, d in bad)
nbm = adjacency(R_MINUS_EDGES)
cover = [(1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8)]
cliques_ok = all(all(b in nbm[a] for a in K for b in K if a != b) for K in cover)
each_vertex_thrice = all(sum(v in K for K in cover) == 3 for v in range(1, 11))
out = dict(strokes=len(strokes), node_to_node_strokes=len(strokes) - len(bad), non_edge_strokes=bad,
           non_edge_strokes_degenerate=degenerate_only, edges_match_R=ok,
           R_minus_is_R_minus_9_10=(set(R_EDGES) - set(R_MINUS_EDGES) == {(9, 10)}),
           bcdrv_cover_cliques_in_R_minus=cliques_ok, cover_each_vertex_weight_1=each_vertex_thrice)
print(json.dumps(out))
if not (ok and degenerate_only and cliques_ok and each_vertex_thrice): sys.exit(1)
