#!/usr/bin/env python3
"""Reviewer-authored (f91) semantic audit of the pinned species-0 support CNF.

Independent of the author's encoder: parses the raw Wanless text itself,
rebuilds the five-net, derives A_x from the physical orthogonality argument,
assigns semantics to every pinned variable, and classifies each pinned clause
into one of the physically justified families (or flags it).  Also builds a
from-scratch CNF and checks clause-multiset equality after an explicit
auxiliary-variable bijection.  Standard library only.
"""
import collections, hashlib, itertools, json, pathlib, sys, time
ROOT = pathlib.Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/moqls8')
SRC = ROOT / 'frontier-20261028-source-wanless-max3-order8-v1.txt'
SRC_SHA = '95943777fc50075220569c53fca1382bd30e79ccf7c1fc29efbee55a30322a67'
CNF = ROOT / 'frontier-20261028-q1-support-species0-v1.cnf'
CNF_SHA = '0ddbe3818bba22fb3e040d669f0b81dcfe8f39f3b005db842a6c969db8f00f63'
V = range(8)

def sha(b): return hashlib.sha256(b).hexdigest()

# ---------- 1. source triple, parsed from raw bytes ----------
src = SRC.read_bytes(); assert sha(src) == SRC_SHA, 'source hash'
nonblank = [l.strip() for l in src.decode('ascii').splitlines() if l.strip()]
assert nonblank[0].split()[:3] == ['8', '8', '114'], nonblank[0]
assert len(nonblank) == 1 + 8 * 114
squares = [[[ord(ch) - 97 for ch in nonblank[1 + 8 * k + i]] for i in V] for k in range(114)]
T = squares[0:3]                       # zero-based species index 0 == first printed triple
for L in T:
    assert all(sorted(r) == list(V) for r in L), 'row Latin'
    assert all(sorted(L[i][j] for i in V) == list(V) for j in V), 'column Latin'
    assert L[0] == list(V), 'first row must be identity for e_t = Q(0,t) semantics'
for a, b in itertools.combinations(range(3), 2):
    assert len({(T[a][i][j], T[b][i][j]) for i in V for j in V}) == 64, 'MOLS'

# ---------- 2. five-net, OA(64,5,8,2) check, allowed sets ----------
pt = {8 * i + j: (i, j, T[0][i][j], T[1][i][j], T[2][i][j]) for i in V for j in V}
for k1, k2 in itertools.combinations(range(5), 2):
    assert len({(p[k1], p[k2]) for p in pt.values()}) == 64, 'five-net strength 2'
lines = {(k, v): frozenset(x for x in pt if pt[x][k] == v) for k in range(5) for v in V}
assert all(len(l) == 8 for l in lines.values())
def collinear(x, y): return any(pt[x][k] == pt[y][k] for k in range(5))
# physical: Q(x) for x=(i,j), i>0, is orthogonal to e_j (column line) and to
# e_{L_k(x)} (cell (0,L_k(x)) shares symbol line k), so support in complement.
A = {x: frozenset(V) - frozenset(pt[x][1:]) for x in range(8, 64)}
assert all(len(A[x]) == 4 for x in A), 'four distinct forbidden labels'

# ---------- 3. parse pinned CNF ----------
cb = CNF.read_bytes(); assert sha(cb) == CNF_SHA, 'cnf hash'
hdr = None; clauses = []
for line in cb.decode('ascii').splitlines():
    z = line.split()
    if not z or z[0] == 'c': continue
    if z[0] == 'p':
        assert hdr is None and z[1] == 'cnf' and len(z) == 4; hdr = (int(z[2]), int(z[3])); continue
    q = list(map(int, z)); assert q[-1] == 0 and 0 not in q[:-1] and all(abs(t) <= hdr[0] for t in q[:-1])
    clauses.append(tuple(q[:-1]))
nvars, m = hdr; assert m == len(clauses) == 7697 and nvars == 2176
assert all(len(set(map(abs, c))) == len(c) for c in clauses), 'no duplicate/tautological literals'

# ---------- 4. variable semantics ----------
# Hypothesis for support variables: x ascending 8..63, t ascending in A[x].
Pvar = {}; k = 0
for x in range(8, 64):
    for t in sorted(A[x]):
        k += 1; Pvar[(x, t)] = k
assert k == 224
Psem = {v: key for key, v in Pvar.items()}
# auxiliary semantics derived from the pinned clauses themselves
pos_bin = collections.defaultdict(list)     # aux -> list of P it implies via (-aux, P)
tern = collections.defaultdict(list)        # aux -> list of (P1,P2) via (aux, -P1, -P2)
for c in clauses:
    auxs = [l for l in c if abs(l) > 224]
    if len(c) == 2 and len(auxs) == 1 and auxs[0] < 0 and c[0] != c[1]:
        other = [l for l in c if abs(l) <= 224]
        if other and other[0] > 0: pos_bin[-auxs[0]].append(other[0])
    if len(c) == 3 and len(auxs) == 1 and auxs[0] > 0:
        other = [l for l in c if abs(l) <= 224]
        if len(other) == 2 and all(l < 0 for l in other): tern[auxs[0]].append(tuple(sorted(-l for l in other)))
Bsem = {}; Nsem = {}
for a in range(225, nvars + 1):
    imp = sorted(pos_bin.get(a, [])); tt = tern.get(a, [])
    assert len(imp) == 2, ('aux without two implications', a, imp)
    (x1, t1), (x2, t2) = Psem[imp[0]], Psem[imp[1]]
    if tt:
        assert len(tt) == 1 and tt[0] == tuple(imp), ('aux definition', a)
        assert x1 != x2 and t1 == t2 and collinear(x1, x2), ('B semantics', a)
        Bsem[a] = (min(x1, x2), max(x1, x2), t1)
    else:
        assert x1 == x2 and t1 != t2, ('N semantics', a)
        Nsem[a] = (x1, frozenset((t1, t2)))
assert len(Bsem) + len(Nsem) == nvars - 224
assert len(set(Bsem.values())) == len(Bsem) and len(set(Nsem.values())) == len(Nsem), 'duplicate aux definitions'
Bvar = {v: a for a, v in Bsem.items()}

# ---------- 5. classify every pinned clause ----------
fam = collections.Counter(); bad = []
seen_bdef = collections.Counter(); seen_ndef = collections.Counter()
big_N = None
for c in clauses:
    S = frozenset(c)
    pos = [l for l in c if l > 0]; neg = [-l for l in c if l < 0]
    # (a) nonempty support
    if all(0 < l <= 224 for l in c) and len(c) == 4:
        xs = {Psem[l][0] for l in c}
        if len(xs) == 1 and {Psem[l][1] for l in c} == A[next(iter(xs))]:
            fam['a_nonempty'] += 1; continue
    # (b) axis on line: all off-row cells on a line not containing (0,t) that allow t
    if all(0 < l <= 224 for l in c) and len(c) == 4:
        ts = {Psem[l][1] for l in c}; xs = {Psem[l][0] for l in c}
        if len(ts) == 1:
            t = next(iter(ts)); hit = False
            for ln in lines.values():
                if t in ln: continue
                if xs == {x for x in ln if x >= 8 and t in A[x]}: hit = True; break
            if hit: fam['b_axis_on_line'] += 1; continue
    # (c) one-overlap
    if len(c) == 2 and all(l < 0 and -l <= 224 for l in c):
        (x, t), (y, u) = Psem[-c[0]], Psem[-c[1]]
        if t == u and x != y and collinear(x, y) and A[x] & A[y] == {t}:
            fam['c_one_overlap'] += 1; continue
    # (d) B definitions
    if len(c) == 2 and c[0] * c[1] < 0 and max(abs(l) for l in c) in Bsem:
        a = max(abs(l) for l in c); x, y, t = Bsem[a]; p = [l for l in c if abs(l) <= 224]
        if [l for l in c if abs(l) > 224][0] == -a and p and p[0] in (Pvar[(x, t)], Pvar[(y, t)]):
            seen_bdef[a] += 1; fam['d_B_def_bin'] += 1; continue
    if len(c) == 3 and any(abs(l) in Bsem for l in c):
        a = [l for l in c if abs(l) > 224]
        if len(a) == 1 and a[0] > 0 and a[0] in Bsem:
            x, y, t = Bsem[a[0]]
            if set(neg) == {Pvar[(x, t)], Pvar[(y, t)]}: seen_bdef[a[0]] += 1; fam['d_B_def_tern'] += 1; continue
    # (e) overlap size != 1 : (-B[x,y,t], B[x,y,u] for all other u in A[x]&A[y])
    if len(neg) == 1 and neg[0] in Bsem and all(l in Bsem for l in pos) and pos:
        x, y, t = Bsem[neg[0]]
        if all(Bsem[l][:2] == (x, y) for l in pos) and {Bsem[l][2] for l in pos} == (A[x] & A[y]) - {t}:
            fam['e_overlap_not_one'] += 1; continue
    # (f) triangles
    if len(c) == 6 and all(l < 0 and -l <= 224 for l in c):
        cells = collections.defaultdict(set)
        for l in c: x, t = Psem[-l]; cells[x].add(t)
        if len(cells) == 3 and len({frozenset(s) for s in cells.values()}) == 1:
            tu = next(iter(cells.values())); xs = sorted(cells)
            if len(tu) == 2 and all(collinear(p, q) and A[p] & A[q] == tu for p, q in itertools.combinations(xs, 2)):
                fam['f_triangle'] += 1; continue
    # (g) N definitions
    if len(c) == 2 and c[0] * c[1] < 0 and max(abs(l) for l in c) in Nsem:
        a = max(abs(l) for l in c); x, tu = Nsem[a]; p = [l for l in c if abs(l) <= 224]
        if [l for l in c if abs(l) > 224][0] == -a and p and p[0] in {Pvar[(x, t)] for t in tu}:
            seen_ndef[a] += 1; fam['g_N_def'] += 1; continue
    # (h) nonclassicality: OR over all N vars
    if all(l > 0 and l in Nsem for l in c):
        big_N = c; fam['h_nonclassical'] += 1; continue
    bad.append(c)
assert not bad, ('unclassified clauses', bad[:5], len(bad))
assert all(seen_bdef[a] == 3 for a in Bsem), 'every B has exactly 3 defining clauses'
assert all(seen_ndef[a] == 2 for a in Nsem), 'every N has exactly 2 defining clauses'
assert fam['h_nonclassical'] == 1
cover = {Nsem[l] for l in big_N}
need = {(x, frozenset(p)) for x in A for p in itertools.combinations(sorted(A[x]), 2)}
assert cover == need and len(big_N) == 336, 'nonclassicality clause must cover all 336 cell/pair options'

# ---------- 6. from-scratch rebuild and multiset comparison ----------
edges = sorted({tuple(sorted(e)) for ln in lines.values() for e in itertools.combinations(sorted(x for x in ln if x >= 8), 2)})
assert len(edges) == 868
my = []
for x in range(8, 64): my.append(tuple(Pvar[(x, t)] for t in sorted(A[x])))
for ln in lines.values():
    for t in V:
        if t in ln: continue
        el = [x for x in sorted(ln) if x >= 8 and t in A[x]]; assert len(el) == 4
        my.append(tuple(Pvar[(x, t)] for x in el))
my_B = {}
for x, y in edges:
    com = sorted(A[x] & A[y])
    if len(com) == 1: my.append((-Pvar[(x, com[0])], -Pvar[(y, com[0])]))
    elif len(com) >= 2:
        for t in com:
            b = Bvar[(x, y, t)]; my_B[(x, y, t)] = b
            my += [(-b, Pvar[(x, t)]), (-b, Pvar[(y, t)]), (b, -Pvar[(x, t)], -Pvar[(y, t)])]
        for t in com: my.append((-Bvar[(x, y, t)],) + tuple(Bvar[(x, y, u)] for u in com if u != t))
assert set(my_B) == set(Bsem.values()), 'B variable set equals pinned aux set'
tri = 0
for x, y, z in itertools.combinations(range(8, 64), 3):
    if collinear(x, y) and collinear(y, z) and collinear(x, z):
        c1 = A[x] & A[y]
        if len(c1) == 2 and c1 == A[y] & A[z] == A[x] & A[z]:
            tri += 1; t, u = sorted(c1)
            my.append(tuple(-Pvar[(w, s)] for w in (x, y, z) for s in (t, u)))
Nvar = {v: a for a, v in Nsem.items()}
for x in range(8, 64):
    for t, u in itertools.combinations(sorted(A[x]), 2):
        n = Nvar[(x, frozenset((t, u)))]; my += [(-n, Pvar[(x, t)]), (-n, Pvar[(x, u)])]
my.append(tuple(sorted(Nvar.values())))
cm = collections.Counter(frozenset(c) for c in my); cp = collections.Counter(frozenset(c) for c in clauses)
assert cm == cp, ('clause multiset mismatch', len(cm - cp), len(cp - cm))
assert all(v == 1 for v in cp.values()), 'no duplicate clauses'

out = {'result': 'PASS_EVERY_PINNED_CLAUSE_IS_A_NECESSARY_SUPPORT_CONDITION',
       'reviewer': 'f91 same-harness reviewer (not external family)',
       'source_sha256': SRC_SHA, 'cnf_sha256': CNF_SHA, 'cnf_bytes': len(cb),
       'variables': nvars, 'clauses': m, 'support_vars': 224, 'B_vars': len(Bsem), 'N_vars': len(Nsem),
       'five_net_edges': len(edges), 'triangles_direct_enum': tri,
       'clause_families': dict(sorted(fam.items())),
       'one_overlap_edges': fam['c_one_overlap'],
       'multi_overlap_edges': sum(1 for x, y in edges if len(A[x] & A[y]) >= 2),
       'zero_overlap_edges': sum(1 for x, y in edges if len(A[x] & A[y]) == 0),
       'from_scratch_multiset_equal': True,
       'script_sha256': sha(pathlib.Path(__file__).read_bytes())}
print(json.dumps(out, indent=1))
