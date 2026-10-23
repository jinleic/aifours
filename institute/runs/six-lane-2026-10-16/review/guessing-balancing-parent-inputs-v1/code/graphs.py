"""Graphs R and R^- of Baber-Christofides-Dang-Riis-Vaughan (arXiv:1410.8349v2, Figure 1).

Edges were extracted from the original sources/tex/RGraph.ps path commands (endpoint coordinates) and
matched to node labels read from the rendered figure (sources/RGraph-from-ps-trim.png); see
verify_graph.py.  Vertices are 1..10; R^- = R minus edge {9,10}.
"""
NODE_XY = {  # PostScript user coordinates after the figure's y-flip (y grows downward)
    8: (200.0, 25.289), 2: (200.0, 110.219), 7: (168.555, 164.684), 3: (231.445, 164.684),
    1: (200.0, 182.84), 6: (137.109, 219.148), 5: (200.0, 219.148), 4: (262.891, 219.148),
    10: (63.559, 261.613), 9: (336.441, 261.613),
}
R_MINUS_EDGES = [(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (2, 3), (2, 7), (2, 9), (2, 10),
                 (3, 4), (3, 8), (3, 9), (4, 5), (4, 8), (4, 10), (5, 6), (5, 9), (5, 10),
                 (6, 7), (6, 8), (6, 9), (7, 8), (7, 10), (8, 9), (8, 10)]
R_EDGES = R_MINUS_EDGES + [(9, 10)]

def adjacency(edges, n=10):
    nb = {v: set() for v in range(1, n + 1)}
    for a, b in edges:
        nb[a].add(b); nb[b].add(a)
    return nb

# 0-based neighbor bitmasks
def nbmasks(edges, n=10):
    nb = adjacency(edges, n)
    return [sum(1 << (u - 1) for u in nb[v]) for v in range(1, n + 1)]
