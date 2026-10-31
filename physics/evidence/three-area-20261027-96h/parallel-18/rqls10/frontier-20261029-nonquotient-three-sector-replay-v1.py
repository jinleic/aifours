#!/usr/bin/env python3
"""Independent exact replay of the Weisner three-sector certificate.

Does not import or execute the author checker. Enumerates transversals by all
10! column permutations and counts triangle-free triples with membership
bitsets, then independently checks every reported equality proof step.
"""
import ast
import hashlib
import itertools
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'frontier-20261028-ols10-switch-v1.py'
CERT = ROOT / 'frontier-20261029-nonquotient-three-sector-certificate-v1.json'
OUT = ROOT / 'frontier-20261029-nonquotient-three-sector-replay-v1.json'
EXPECTED_SOURCE = '394c59221d0526ca623d46925d4d82e68d13ddb55b6c45f5bdada1ee622ff172'
EXPECTED_CERT = '975e381fff5745f687bbe5e0a25d84a21239e0c7dcbf02cf023eac80f74a1900'
if OUT.exists():
    raise FileExistsError(OUT)
sraw, craw = SOURCE.read_bytes(), CERT.read_bytes()
assert hashlib.sha256(sraw).hexdigest() == EXPECTED_SOURCE
assert hashlib.sha256(craw).hexdigest() == EXPECTED_CERT
cert = json.loads(craw)
module = ast.parse(sraw.decode('utf-8'))
expr = next(node.value for node in module.body if isinstance(node, ast.Assign)
            and any(isinstance(t, ast.Name) and t.id == 'ROWS' for t in node.targets))
table = [[tuple(int(ch) for ch in word) for word in row.split()] for row in ast.literal_eval(expr)]
rawL = tuple(table[r][c][1] for r in range(10) for c in range(10))
renaming = {value: i for i, value in enumerate(rawL[:10])}
L = tuple(renaming[x] for x in rawL)
assert [list(L[10*r:10*r+10]) for r in range(10)] == cert['labels_normalized_first_row']
assert all(set(L[10*r:10*r+10]) == set(range(10)) for r in range(10))
assert all({L[10*r+c] for r in range(10)} == set(range(10)) for c in range(10))

# Different traversal from the original row DFS: enumerate all 10! permutations.
T = [p for p in itertools.permutations(range(10))
     if len({L[10*r+c] for r, c in enumerate(p)}) == 10]
assert [list(p) for p in T] == cert['transversal_catalogue']
N = len(T)
assert N == 728
masks = [sum(1 << (10*r+c) for r, c in enumerate(t)) for t in T]
members = [0]*100
for i, t in enumerate(T):
    for r, c in enumerate(t):
        members[10*r+c] |= 1 << i
universe = (1 << N)-1
higher = [universe ^ ((1 << (i+1))-1) for i in range(N)]
compatible = []
for i, t in enumerate(T):
    conflicts = 0
    for r, c in enumerate(t):
        conflicts |= members[10*r+c]
    compatible.append(universe & ~conflicts)

# Pair-to-transversal bad masks, rather than the author's pair-to-cell masks.
col_symbol_row = [[0]*10 for _ in range(10)]
for r in range(10):
    for c in range(10):
        col_symbol_row[c][L[10*r+c]] = r
bad = {}
for i in range(N):
    later = compatible[i] & higher[i]
    while later:
        bit = later & -later
        j = bit.bit_length()-1
        later -= bit
        forbidden_transversals = 0
        for r in range(10):
            x, y = T[i][r], T[j][r]
            cell1 = 10*col_symbol_row[x][L[10*r+y]]+x
            cell2 = 10*col_symbol_row[y][L[10*r+x]]+y
            forbidden_transversals |= members[cell1] | members[cell2]
        bad[(i, j)] = forbidden_transversals

triples = 0
safe_supports = set()
for i in range(N):
    later = compatible[i] & higher[i]
    while later:
        bit = later & -later
        j = bit.bit_length()-1
        later -= bit
        possible = compatible[i] & compatible[j] & higher[j]
        triples += possible.bit_count()
        possible &= ~bad[(i, j)]
        while possible:
            bk = possible & -possible
            k = bk.bit_length()-1
            possible -= bk
            if not (bad[(i, k)] >> j & 1) and not (bad[(j, k)] >> i & 1):
                safe_supports.add(masks[i] | masks[j] | masks[k])
assert triples == 3365592
cert_safe = {int(record['mask_hex'], 16) for record in cert['triangle_free_sector_supports']}
assert safe_supports == cert_safe and len(safe_supports) == 1968

# Exact-cover alternative: pick the least-supported uncovered CELL rather than
# anchoring the remaining mate colors to cells in the first row.
by_cell = [[i for i, m in enumerate(masks) if m >> c & 1] for c in range(100)]
mate_sets = set()

def extend(used, picked):
    if used.bit_count() == 100:
        mate_sets.add(tuple(sorted(picked)))
        return
    best = None
    for cell in range(100):
        if used >> cell & 1:
            continue
        options = [i for i in by_cell[cell] if not (masks[i] & used)]
        if not options:
            return
        if best is None or len(options) < len(best):
            best = options
    for i in best:
        extend(used | masks[i], picked + [i])

extend(0, [])
assert mate_sets == {tuple(row) for row in cert['mate_transversal_indices']}
assert len(mate_sets) == 10
support_origins = {}
for mate in mate_sets:
    for subset in itertools.combinations(mate, 3):
        mask = masks[subset[0]] | masks[subset[1]] | masks[subset[2]]
        support_origins.setdefault(mask, []).append(subset)
assert len(support_origins) == 1197

class ProofError(Exception):
    pass

def require(value, code):
    if not value:
        raise ProofError(code)

def replay(mask, proof):
    cells = [c for c in range(100) if mask >> c & 1]
    require(len(cells) == 30, 'sector_size')
    contexts = []
    for f in range(3):
        for value in range(10):
            block = [c for c in cells if (c//10 if f == 0 else c%10 if f == 1 else L[c]) == value]
            require(len(block) == 3, 'context_size')
            contexts.append(block)
    parent = {c: c for c in cells}
    def root(x):
        while parent[x] != x:
            x = parent[x]
        return x
    for event in proof:
        basis, x, y, z, w, e1, e2 = event
        require(all(v in parent for v in (x, y, z, w)), 'cell_outside_sector')
        require(all(0 <= v < 30 for v in (basis, e1, e2)), 'invalid_context')
        require(set((x, y, z)) == set(contexts[basis]), 'wrong_basis_cells')
        a, b, d = root(x), root(y), root(w)
        require(len({a, b, d}) == 3, 'witness_not_three_distinct_rays')
        require({a, d} <= {root(c) for c in contexts[e1]}, 'missing_xw_orthogonality')
        require({b, d} <= {root(c) for c in contexts[e2]}, 'missing_yw_orthogonality')
        u, v = root(z), d
        require(u != v, 'redundant_equality')
        parent[max(u, v)] = min(u, v)
        require(all(len({root(c) for c in block}) == 3 for block in contexts), 'collapsed_basis')
    return sorted(sorted(c for c in cells if root(c) == u) for u in {root(c) for c in cells})

records = cert['full_mate_sector_proof_records']
assert {int(record['sector_mask_hex'], 16) for record in records} == set(support_origins)
class_counts = []
steps = 0
for record in records:
    mask = int(record['sector_mask_hex'], 16)
    proof = record['three_dimensional_equality_proof']
    classes = replay(mask, proof)
    assert classes == record['forced_ray_classes']
    class_counts.append(len(classes))
    steps += len(proof)
assert class_counts.count(3) == 1194 and class_counts.count(30) == 3

# Intended-reason mutation controls, applied in memory only.
example = next(record for record in records if record['three_dimensional_equality_proof'])
mask = int(example['sector_mask_hex'], 16)
original = example['three_dimensional_equality_proof']
mutations = []
for kind in ('outside', 'basis', 'orthogonality'):
    modified = [list(e) for e in original]
    if kind == 'outside':
        modified[0][4] = next(c for c in range(100) if not (mask >> c & 1))
        expected = 'cell_outside_sector'
    elif kind == 'basis':
        modified[0][0] = 30
        expected = 'invalid_context'
    else:
        basis, x, y, z, w, e1, e2 = modified[0]
        cells = [c for c in range(100) if mask >> c & 1]
        blocks = [[c for c in cells if (c//10 if f == 0 else c%10 if f == 1 else L[c]) == value]
                  for f in range(3) for value in range(10)]
        modified[0][5] = next(i for i, block in enumerate(blocks) if x not in block or w not in block)
        expected = 'missing_xw_orthogonality'
    try:
        replay(mask, modified)
    except ProofError as exc:
        require(str(exc) == expected, 'mutation_wrong_reason')
        mutations.append({'mutation': kind, 'rejected_as': str(exc)})
    else:
        raise ProofError('mutation_not_rejected')

out = {
    'status': 'INDEPENDENT_EXACT_REPLAY_PASS_UNREVIEWED',
    'native_clock': subprocess.check_output(['/bin/date'], text=True).rstrip('\n'),
    'source_sha256': EXPECTED_SOURCE,
    'certificate_sha256': EXPECTED_CERT,
    'replay_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'transversals': N,
    'disjoint_transversal_triples': triples,
    'triangle_free_sector_supports': len(safe_supports),
    'normalized_classical_mates': len(mate_sets),
    'mate_sector_supports': len(support_origins),
    'mate_sector_supports_with_three_forced_rays': class_counts.count(3),
    'mate_sector_supports_without_forced_equalities': class_counts.count(30),
    'replayed_equality_steps': steps,
    'intended_reason_mutations': mutations,
    'limitations': 'Same-harness author replay; does not establish novelty or a full 1-RQLS(10) no-go.',
}
with OUT.open('x', encoding='utf-8') as f:
    json.dump(out, f, indent=2)
    f.write('\n')
print(json.dumps(out, indent=2))
