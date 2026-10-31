#!/usr/bin/env python3
"""Exact three-sector constraints for the literal Weisner order-10 square.

Read, but never execute, a pinned literal source of the two classical Latin
squares. Recompute every transversal of the resolution square, every disjoint
triple of them, and every classical mate. On sector supports coming from full
mates, emit replayable ray-equality proofs derived solely from orthogonal triads
in a three-dimensional Hilbert space. No floats, Gram-matrix search or solver.
"""
import ast
import collections
import hashlib
import itertools
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'frontier-20261028-ols10-switch-v1.py'
OUT = ROOT / 'frontier-20261029-nonquotient-three-sector-certificate-v1.json'
SOURCE_SHA = '394c59221d0526ca623d46925d4d82e68d13ddb55b6c45f5bdada1ee622ff172'
if OUT.exists():
    raise FileExistsError(OUT)
raw = SOURCE.read_bytes()
assert hashlib.sha256(raw).hexdigest() == SOURCE_SHA
module = ast.parse(raw.decode('utf-8'))
assignment = next(node.value for node in module.body if isinstance(node, ast.Assign)
                  and any(isinstance(target, ast.Name) and target.id == 'ROWS'
                          for target in node.targets))
rows = ast.literal_eval(assignment)
pairs = [[tuple(map(int, word)) for word in row.split()] for row in rows]
assert len(pairs) == 10 and all(len(row) == 10 for row in pairs)

def normalize(square):
    mapping = {symbol: i for i, symbol in enumerate(square[:10])}
    assert len(mapping) == 10
    return tuple(mapping[value] for value in square)

seed_a = normalize(tuple(pairs[r][c][0] for r in range(10) for c in range(10)))
L = normalize(tuple(pairs[r][c][1] for r in range(10) for c in range(10)))

def latin(square):
    return (all(set(square[10*r:10*r+10]) == set(range(10)) for r in range(10))
            and all({square[10*r+c] for r in range(10)} == set(range(10)) for c in range(10)))

assert latin(seed_a) and latin(L) and len(set(zip(seed_a, L))) == 100

# Enumerate every transversal by depth-first search on rows, with used-column
# and used-label bitsets. The resulting permutations are in lexical order.
transversals = []
dfs_nodes = 0

def trans_dfs(r, columns, labels, path):
    global dfs_nodes
    dfs_nodes += 1
    if r == 10:
        transversals.append(tuple(path))
        return
    for c in range(10):
        t = L[10*r+c]
        if not (columns >> c & 1) and not (labels >> t & 1):
            path.append(c)
            trans_dfs(r+1, columns | (1 << c), labels | (1 << t), path)
            path.pop()

trans_dfs(0, 0, 0, [])
assert transversals == sorted(set(transversals))
N = len(transversals)
assert N == 728
masks = [sum(1 << (10*r+c) for r, c in enumerate(t)) for t in transversals]
for t in transversals:
    assert len(set(t)) == 10 and len({L[10*r+c] for r, c in enumerate(t)}) == 10

# Each future adjacent bit represents a disjoint pair of transversals.
adj = [0] * N
for i in range(N):
    for j in range(i+1, N):
        if not (masks[i] & masks[j]):
            adj[i] |= 1 << j

# For disjoint transversals i,j, forbidden[i,j] contains, for each row r,
# the two cells completing the possible R-C-T triangles with the two selected
# row cells. Their row is unique because L is Latin in every column.
col_inverse = [[0]*10 for _ in range(10)]
for r in range(10):
    for c in range(10):
        col_inverse[c][L[10*r+c]] = r
forbidden = {}
for i in range(N):
    for j in range(i+1, N):
        if not (adj[i] >> j & 1):
            continue
        bits = 0
        for r in range(10):
            a, b = transversals[i][r], transversals[j][r]
            ra = col_inverse[a][L[10*r+b]]
            rb = col_inverse[b][L[10*r+a]]
            bits |= (1 << (10*ra+a)) | (1 << (10*rb+b))
        forbidden[(i, j)] = bits

def direct_corner(mask):
    row_labels = [0]*10
    col_labels = [0]*10
    for cell in range(100):
        if mask >> cell & 1:
            r, c = divmod(cell, 10)
            bit = 1 << L[cell]
            row_labels[r] |= bit
            col_labels[c] |= bit
    return any((mask >> (10*r+c) & 1)
               and ((row_labels[r] & col_labels[c]) & ~(1 << L[10*r+c]))
               for r in range(10) for c in range(10))

all_triples = 0
corner_triples = 0
safe = {}
unsafe_controls = 0
for i in range(N):
    js = adj[i]
    while js:
        jb = js & -js
        j = jb.bit_length()-1
        js -= jb
        ks = adj[i] & adj[j]
        fij = forbidden[(i, j)]
        while ks:
            kb = ks & -ks
            k = kb.bit_length()-1
            ks -= kb
            all_triples += 1
            mask = masks[i] | masks[j] | masks[k]
            corner = bool((fij & masks[k]) or (forbidden[(i, k)] & masks[j])
                          or (forbidden[(j, k)] & masks[i]))
            if corner:
                corner_triples += 1
                if unsafe_controls < 2000:
                    assert direct_corner(mask)
                    unsafe_controls += 1
            else:
                assert not direct_corner(mask)
                safe.setdefault(mask, []).append((i, j, k))

assert all_triples == 3365592 and corner_triples == 3363624
assert sum(map(len, safe.values())) == 1968 and len(safe) == 1968

# Independent exact-cover census of classical mates. Each transversal is
# anchored by its row-zero column, which is its normalized mate symbol.
groups = [[i for i, t in enumerate(transversals) if t[0] == c] for c in range(10)]
mate_sets = []
mate_nodes = 0

def cover_dfs(rem, used, chosen):
    global mate_nodes
    mate_nodes += 1
    if not rem:
        mate_sets.append(tuple(sorted(chosen)))
        return
    c = min(rem, key=lambda q: (sum(not (masks[i] & used) for i in groups[q]), q))
    for i in groups[c]:
        if not (masks[i] & used):
            cover_dfs(rem - {c}, used | masks[i], chosen + [i])

cover_dfs(set(range(10)), 0, [])
assert len(mate_sets) == len(set(mate_sets)) == 10
for chosen in mate_sets:
    m = 0
    for idx in chosen:
        assert not (m & masks[idx])
        m |= masks[idx]
    assert m == (1 << 100)-1

# Each sector support below is a union of three mate transversals. For any
# three-sector support, contexts() returns its 10 rows, 10 columns and 10
# resolution classes as actual cell IDs (0..99).
def contexts(mask):
    cell_list = [i for i in range(100) if mask >> i & 1]
    assert len(cell_list) == 30
    out = []
    for family in range(3):
        for value in range(10):
            block = tuple(i for i in cell_list
                          if (i//10 if family == 0 else i%10 if family == 1 else L[i]) == value)
            assert len(block) == 3
            out.append(block)
    return cell_list, out

class DSU:
    def __init__(self, cells):
        self.parent = {x: x for x in cells}

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def join(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b:
            return False
        lo, hi = sorted((a, b))
        self.parent[hi] = lo
        return True

def sector_closure(mask):
    cells, blocks = contexts(mask)
    dsu = DSU(cells)
    proof = []
    while True:
        graph = collections.defaultdict(set)
        edge_context = {}
        for ci, block in enumerate(blocks):
            roots = tuple(dsu.find(x) for x in block)
            assert len(set(roots)) == 3
            for a, b in itertools.combinations(roots, 2):
                graph[a].add(b)
                graph[b].add(a)
                edge_context.setdefault(tuple(sorted((a, b))), ci)
        event = None
        for ci, block in enumerate(blocks):
            for k in range(3):
                x, y, z = block[(k+1)%3], block[(k+2)%3], block[k]
                a, b, old = dsu.find(x), dsu.find(y), dsu.find(z)
                for witness in sorted(graph[a] & graph[b]):
                    if witness != old:
                        w = next(v for v in cells if dsu.find(v) == witness)
                        event = [ci, x, y, z, w,
                                 edge_context[tuple(sorted((a, witness)))],
                                 edge_context[tuple(sorted((b, witness)))]]
                        break
                if event:
                    break
            if event:
                break
        if event is None:
            break
        proof.append(event)
        assert dsu.join(event[3], event[4])
    classes = collections.defaultdict(list)
    for cell in cells:
        classes[dsu.find(cell)].append(cell)
    return blocks, proof, sorted(classes.values())

def replay_proof(mask, proof):
    cells, blocks = contexts(mask)
    dsu = DSU(cells)
    for basis, x, y, z, w, edge_xw, edge_yw in proof:
        assert set((x, y, z)) == set(blocks[basis])
        assert all(len({dsu.find(c) for c in block}) == 3 for block in blocks)
        a, b, d = dsu.find(x), dsu.find(y), dsu.find(w)
        assert len({a, b, d}) == 3
        assert {a, d} <= {dsu.find(c) for c in blocks[edge_xw]}
        assert {b, d} <= {dsu.find(c) for c in blocks[edge_yw]}
        assert dsu.find(z) != d
        assert dsu.join(z, w)
    assert all(len({dsu.find(c) for c in block}) == 3 for block in blocks)
    return sorted(sorted(c for c in cells if dsu.find(c) == root)
                  for root in {dsu.find(c) for c in cells})

mate_supports = {}
for mi, chosen in enumerate(mate_sets):
    for triple in itertools.combinations(chosen, 3):
        mask = masks[triple[0]] | masks[triple[1]] | masks[triple[2]]
        mate_supports.setdefault(mask, [mi, list(triple)])
assert len(mate_supports) == 1197
records = []
for mask, origin in sorted(mate_supports.items()):
    blocks, proof, classes = sector_closure(mask)
    assert replay_proof(mask, proof) == classes
    assert len(classes) in (3, 30)
    assert (len(classes) == 30) == (mask in safe)
    records.append({'sector_mask_hex': format(mask, '025x'), 'origin_mate_and_transversals': origin,
                    'forced_ray_classes': classes, 'three_dimensional_equality_proof': proof})
counts = collections.Counter(len(record['forced_ray_classes']) for record in records)
assert counts == {3: 1194, 30: 3}

summary = {
    'status': 'EXACT_ENUMERATION_AND_EQUALITY_PROOFS_PASS_UNREVIEWED',
    'native_clock': subprocess.check_output(['/bin/date'], text=True).rstrip('\n'),
    'source_sha256': SOURCE_SHA,
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'transversals': N,
    'transversal_DFS_nodes': dfs_nodes,
    'disjoint_transversal_pairs': sum(bits.bit_count() for bits in adj),
    'disjoint_transversal_triples': all_triples,
    'triples_with_extra_context_triangle': corner_triples,
    'triangle_free_triples': all_triples-corner_triples,
    'distinct_triangle_free_sector_supports': len(safe),
    'unsafe_direct_test_controls': unsafe_controls,
    'normalized_classical_mates': len(mate_sets),
    'classical_mate_exact_cover_nodes': mate_nodes,
    'distinct_supports_from_full_mates': len(mate_supports),
    'mate_supports_forced_to_three_rays': counts[3],
    'mate_supports_without_a_forced_equality': counts[30],
    'scope': 'Literal Weisner resolution L; 3D sectors that are unions of three transversals. No general RQLS(10) no-go.',
}
output = {
    **summary,
    'labels_normalized_first_row': [list(L[10*r:10*r+10]) for r in range(10)],
    'transversal_catalogue': [list(t) for t in transversals],
    'mate_transversal_indices': [list(chosen) for chosen in mate_sets],
    'triangle_free_sector_supports': [{'mask_hex': format(mask, '025x'), 'transversal_triples': triples}
                                      for mask, triples in sorted(safe.items())],
    'full_mate_sector_proof_records': records,
}
with OUT.open('x', encoding='utf-8') as f:
    json.dump(output, f, separators=(',', ':'))
    f.write('\n')
print(json.dumps(summary, indent=2))
