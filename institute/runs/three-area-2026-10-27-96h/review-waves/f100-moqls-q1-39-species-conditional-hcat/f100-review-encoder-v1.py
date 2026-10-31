#!/usr/bin/env python3
"""f100 review: independent re-derivation of the q1 support CNF from the physical definitions.

Physical setting (as reconstructed by the reviewer): Q is a quantum Latin square of order 8 whose
three mates are classical (ordinary MOLS L1,L2,L3 after rotating each mate into its own basis).
Pair-product orthogonality with a classical mate L_k forces Q to be an ONB along each symbol line of
L_k; rows and columns are ONBs by definition.  So Q is an ONB on every line of the 5-net
{rows, columns, L1, L2, L3}.  Fix an anchor line (the "first row"); its eight Q vectors are an ONB,
taken as coordinates e_0..e_7 (e_j at the anchor cell in column j).  For an off-anchor cell x, the
four anchor cells collinear with x (one per non-row class) carry coordinates that Q(x) must be
orthogonal to, so the support S_x of Q(x) lies in the complementary 4-set A_x.

Necessary support conditions encoded (variables P[x,t] = "t in S_x", t in A_x):
  (1) S_x nonempty;
  (2) for every line l and coordinate t with anchor cell (0,t) not on l: some off-anchor cell on l
      has t in its support (ONB completeness: sum over the line of |Q(x)_t|^2 = 1);
  (3) for collinear x,y: |S_x cap S_y| != 1 (an inner product with exactly one nonzero term is nonzero);
      encoded with auxiliaries B[x,y,t] <-> P[x,t] & P[y,t] when |A_x cap A_y| >= 2, binary clause when
      |A_x cap A_y| == 1;
  (4) for pairwise collinear x,y,z with A_x cap A_y = A_y cap A_z = A_x cap A_z = {t,u}: not all six of
      P[.,t],P[.,u] (projections onto span(e_t,e_u) would be three nonzero pairwise-orthogonal vectors
      in a 2-dimensional space);
  (5) nonclassicality: some |S_x| >= 2, via auxiliaries N[x,t,u] -> P[x,t], N[x,t,u] -> P[x,u], OR N.

This script does NOT import any author code.  It parses the two pinned Wanless snapshots itself,
builds the oriented net itself, derives forbidden sets from net collinearity (and cross-checks them
against the label-normalization description), generates the clause multiset with semantic names,
then parses the retained DIMACS file and compares the clause multisets under the producer's
declared variable order (P in cell/coordinate order, then B per sorted edge, then N per cell/pair).
Standard library only.
"""
import argparse, collections, hashlib, itertools, json, pathlib, sys, time

ROOT = pathlib.Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/moqls8')
SNAP = [('frontier-20261028-source-wanless-max3-order8-v1.txt',
         '95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67', 114),
        ('frontier-20261028-source-wanless-nonmax3-order8-v1.txt',
         'f8156dc17b3900e5d09796510acc630a3735d471ae08dcc248beebb9612be4b5', 3)]
V = range(8)


class ReviewError(Exception):
    pass


def parse_snapshot(name, sha, nsq):
    b = (ROOT / name).read_bytes()
    h = hashlib.sha256(b).hexdigest()
    if h != sha:
        raise ReviewError(f'snapshot hash mismatch {name}: {h}')
    lines = b.decode('ascii').split('\n')
    hdr = lines[0].split()
    if hdr[:3] != ['8', '8', str(nsq)]:
        raise ReviewError(f'header {lines[0]!r}')
    rows = [l for l in lines[1:] if l.strip() != '']
    if len(rows) != 8 * nsq:
        raise ReviewError(f'row count {len(rows)}')
    squares = []
    for k in range(nsq):
        sq = []
        for i in V:
            r = rows[8 * k + i]
            if len(r) != 8 or any(ch not in 'abcdefgh' for ch in r):
                raise ReviewError(f'row format {r!r}')
            sq.append([ord(ch) - 97 for ch in r])
        squares.append(sq)
    return squares


def is_latin(sq):
    return all(sorted(row) == list(V) for row in sq) and all(sorted(sq[i][j] for i in V) == list(V) for j in V)


def orthogonal(a, b):
    return len({(a[i][j], b[i][j]) for i in V for j in V}) == 64


def load_triples():
    squares = []
    for name, sha, n in SNAP:
        squares += parse_snapshot(name, sha, n)
    if len(squares) != 117:
        raise ReviewError('square count')
    triples = [squares[3 * k:3 * k + 3] for k in range(39)]
    for k, T in enumerate(triples):
        if not all(is_latin(L) for L in T):
            raise ReviewError(f'triple {k} not Latin')
        if not all(orthogonal(a, b) for a, b in itertools.combinations(T, 2)):
            raise ReviewError(f'triple {k} not MOLS')
    return triples


def oriented_net(T, r, c, s):
    """Return facts[(i,j)] = (i, j, l1, l2, l3) for the 5-net with class r as rows (anchor symbol s -> row 0),
    class c as columns, and the other three classes relabelled so the anchor cell in column j carries symbol j."""
    pts = [(i, j, T[0][i][j], T[1][i][j], T[2][i][j]) for i in V for j in V]
    order = [s] + [v for v in V if v != s]
    rel = {v: i for i, v in enumerate(order)}
    others = [k for k in range(5) if k not in (r, c)]
    cell = {}
    for p in pts:
        key = (rel[p[r]], p[c])
        if key in cell:
            raise ReviewError('classes r,c not orthogonal')
        cell[key] = p
    if len(cell) != 64:
        raise ReviewError('cell count')
    norm = []
    for k in others:
        m = {cell[(0, j)][k]: j for j in V}
        if len(m) != 8:
            raise ReviewError('anchor line is not a transversal of a label class')
        norm.append(m)
    facts = {}
    for (i, j), p in cell.items():
        facts[(i, j)] = (i, j) + tuple(norm[a][p[k]] for a, k in enumerate(others))
    return facts


def net_lines(facts):
    lines = {}
    for k in range(5):
        for v in V:
            cells = sorted(x for x in facts if facts[x][k] == v)
            if len(cells) != 8:
                raise ReviewError('line size')
            lines[(k, v)] = cells
    # net axiom check: two lines of different classes meet in exactly one cell; same class disjoint
    for (k1, v1), (k2, v2) in itertools.combinations(lines, 2):
        inter = len(set(lines[(k1, v1)]) & set(lines[(k2, v2)]))
        if (k1 == k2 and inter != 0) or (k1 != k2 and inter != 1):
            raise ReviewError('net axiom')
    return lines


def collinear_map(lines):
    col = collections.defaultdict(set)
    for cells in lines.values():
        for x, y in itertools.combinations(cells, 2):
            col[x].add(y)
            col[y].add(x)
    return col


def build(T, r, c, s):
    facts = oriented_net(T, r, c, s)
    lines = net_lines(facts)
    col = collinear_map(lines)
    anchor = [(0, j) for j in V]
    coord = {(0, j): j for j in V}          # anchor cell (0,j) carries e_j
    off = [(i, j) for i in range(1, 8) for j in V]   # off-anchor cells in the producer's cell order
    # forbidden sets from collinearity with anchor cells (geometric derivation)
    A = {}
    for x in off:
        forb = {coord[y] for y in anchor if y in col[x]}
        if len(forb) != 4:
            raise ReviewError('anchor partners not four distinct')
        # cross-check with the label-normalisation description (column, l1, l2, l3 of x)
        if forb != set(facts[x][1:]):
            raise ReviewError('normalisation mismatch')
        A[x] = tuple(sorted(set(V) - forb))
    # semantic clause generation
    clauses = []   # list of tuples of (name, sign) ; sign +1/-1
    def P(x, t):
        return ('P', x, t)
    def add(*lits):
        clauses.append(tuple(lits))
    # (1) nonempty support
    for x in off:
        add(*((P(x, t), 1) for t in A[x]))
    # (2) coverage
    n_cov = 0
    for key in sorted(lines):
        cells = lines[key]
        for t in V:
            if (0, t) in cells:
                continue
            elig = [x for x in cells if x[0] != 0 and t in A[x]]
            if not elig:
                raise ReviewError('coverage clause would be empty -> formula trivially UNSAT by a bug')
            add(*((P(x, t), 1) for x in elig))
            n_cov += 1
    # (3) pair clauses; edge order = sorted pairs of off-anchor cells
    edges = sorted({tuple(sorted((x, y))) for x in off for y in col[x] if y[0] != 0})
    n_bin = n_edge_aux = 0
    Bnames = []
    for x, y in edges:
        common = sorted(set(A[x]) & set(A[y]))
        if len(common) == 1:
            t = common[0]
            add((P(x, t), -1), (P(y, t), -1)); n_bin += 1
            continue
        if len(common) < 2:
            continue
        n_edge_aux += 1
        B = {t: ('B', x, y, t) for t in common}
        Bnames += [B[t] for t in common]
        for t in common:
            add((B[t], -1), (P(x, t), 1))
            add((B[t], -1), (P(y, t), 1))
            add((B[t], 1), (P(x, t), -1), (P(y, t), -1))
        for t in common:
            add((B[t], -1), *((B[u], 1) for u in common if u != t))
    # (4) triangles, generated from all triples of pairwise collinear off-anchor cells
    tri = []
    offset = set(off)
    for x, y, z in itertools.combinations(off, 3):
        if y not in col[x] or z not in col[x] or z not in col[y]:
            continue
        axy = set(A[x]) & set(A[y]); ayz = set(A[y]) & set(A[z]); axz = set(A[x]) & set(A[z])
        if len(axy) == 2 and axy == ayz == axz:
            t, u = sorted(axy)
            tri.append((t, u, x, y, z))
    # producer emits triangles grouped by (t,u) then x<y<z; replicate that order for the ordered comparison
    tri.sort()
    for t, u, x, y, z in tri:
        add((P(x, t), -1), (P(x, u), -1), (P(y, t), -1), (P(y, u), -1), (P(z, t), -1), (P(z, u), -1))
    # (5) nonclassicality
    Nnames = []
    for x in off:
        for t, u in itertools.combinations(A[x], 2):
            n = ('N', x, t, u); Nnames.append(n)
            add((n, -1), (P(x, t), 1))
            add((n, -1), (P(x, u), 1))
    add(*((n, 1) for n in Nnames))
    # producer-declared numbering: P (cell order, sorted coords), then B per sorted edge/sorted coord, then N
    numbering = {}
    for x in off:
        for t in A[x]:
            numbering[P(x, t)] = len(numbering) + 1
    for b in Bnames:
        numbering[b] = len(numbering) + 1
    for n in Nnames:
        numbering[n] = len(numbering) + 1
    stats = {'off_cells': len(off), 'support_vars': 8 * 7 * 4, 'coverage_clauses': n_cov, 'edges': len(edges),
             'binary_pair_clauses': n_bin, 'aux_pair_edges': n_edge_aux, 'B_vars': len(Bnames),
             'triangles': len(tri), 'N_vars': len(Nnames), 'variables': len(numbering), 'clauses': len(clauses)}
    return clauses, numbering, stats, A, lines


def parse_dimacs(path):
    b = path.read_bytes()
    text = b.decode('ascii')
    lines = text.split('\n')
    if lines[-1] != '':
        raise ReviewError('no trailing newline')
    hdr = lines[0].split()
    if len(hdr) != 4 or hdr[:2] != ['p', 'cnf']:
        raise ReviewError('header')
    nv, nc = int(hdr[2]), int(hdr[3])
    clauses = []
    for l in lines[1:-1]:
        toks = l.split()
        if not toks or toks[-1] != '0':
            raise ReviewError(f'clause line {l!r}')
        lits = [int(t) for t in toks[:-1]]
        if any(v == 0 or abs(v) > nv for v in lits):
            raise ReviewError('literal range')
        clauses.append(tuple(lits))
    if len(clauses) != nc:
        raise ReviewError(f'clause count header {nc} actual {len(clauses)}')
    return nv, nc, clauses, hashlib.sha256(b).hexdigest(), len(b)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--manifest', default=str(ROOT / 'frontier-20261028-q1-39-species-local-proof-manifest-v1.json'))
    ap.add_argument('--species', type=int, nargs='*', default=None)
    ap.add_argument('--output', required=True)
    a = ap.parse_args()
    out_path = pathlib.Path(a.output)
    if out_path.exists():
        raise SystemExit('refusing to overwrite ' + str(out_path))
    man = json.loads(pathlib.Path(a.manifest).read_text())
    triples = load_triples()
    records = []
    t0 = time.monotonic()
    for rec in man['records']:
        sp = rec['species']
        if a.species is not None and sp not in a.species:
            continue
        r, c, s = rec['orientation']
        clauses, numbering, stats, A, lines = build(triples[sp], r, c, s)
        inv = {v: k for k, v in numbering.items()}
        fpath = ROOT / rec['formula']
        nv, nc, fcl, fsha, fbytes = parse_dimacs(fpath)
        # semantic multiset of file clauses under the declared numbering
        unknown = sorted({abs(v) for cl in fcl for v in cl if abs(v) not in inv})
        mine = collections.Counter(frozenset(lits) for lits in clauses)
        theirs = collections.Counter(frozenset((inv[abs(v)], 1 if v > 0 else -1) for v in cl) for cl in fcl if all(abs(v) in inv for v in cl))
        only_mine = sum((mine - theirs).values()); only_theirs = sum((theirs - mine).values())
        # ordered equality and byte equality of a re-rendering in the producer's format
        rendered = ('p cnf %d %d\n' % (len(numbering), len(clauses)) +
                    ''.join(' '.join(str(numbering[n] * sg) for n, sg in cl) + ' 0\n' for cl in clauses)).encode('ascii')
        records.append({
            'species': sp, 'orientation': [r, c, s], 'formula': rec['formula'], 'formula_sha256_observed': fsha,
            'formula_sha256_manifest': rec['formula_sha256'], 'formula_hash_match': fsha == rec['formula_sha256'],
            'file_vars': nv, 'file_clauses': nc, 'mine': stats,
            'file_vars_outside_my_numbering': unknown,
            'multiset_equal': (only_mine == 0 and only_theirs == 0 and not unknown),
            'clauses_only_mine': only_mine, 'clauses_only_file': only_theirs,
            'file_subset_of_mine': (only_theirs == 0 and not unknown),
            'ordered_equal': [frozenset(l) for l in clauses] == [frozenset((inv[abs(v)], 1 if v > 0 else -1) for v in cl) for cl in fcl] if not unknown else False,
            'rerender_sha256': hashlib.sha256(rendered).hexdigest(), 'rerender_bytes_equal_file': rendered == fpath.read_bytes(),
        })
        print(json.dumps({k: records[-1][k] for k in ('species', 'orientation', 'file_vars', 'file_clauses', 'multiset_equal', 'ordered_equal', 'rerender_bytes_equal_file')}), flush=True)
    receipt = {
        'kind': 'F100_REVIEW_INDEPENDENT_ENCODER_COMPARISON', 'script_sha256': hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        'manifest_sha256': hashlib.sha256(pathlib.Path(a.manifest).read_bytes()).hexdigest(),
        'snapshots': {n: s for n, s, _ in SNAP}, 'species_checked': len(records),
        'all_multiset_equal': all(x['multiset_equal'] for x in records),
        'all_file_subset_of_sound_set': all(x['file_subset_of_mine'] for x in records),
        'all_rerender_bytes_equal': all(x['rerender_bytes_equal_file'] for x in records),
        'elapsed_seconds': time.monotonic() - t0, 'records': records,
        'limits': 'Clause-content equality under the producer-declared numbering; soundness of the clause shapes is argued in review-v1.md; Hcat not addressed here.'}
    with out_path.open('x', encoding='utf-8') as h:
        json.dump(receipt, h, indent=1); h.write('\n')
    print('ALL_MULTISET_EQUAL', receipt['all_multiset_equal'], 'ALL_SUBSET', receipt['all_file_subset_of_sound_set'], 'ALL_BYTES', receipt['all_rerender_bytes_equal'])


if __name__ == '__main__':
    main()
