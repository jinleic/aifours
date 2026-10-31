#!/opt/homebrew/bin/python3
"""Exact search of the rank-four even half with E=0 for one block configuration.

Configuration (beta,N6,N8): numbers of type-12, type-6, type-8 C0 blocks; alpha=10-beta type-10
blocks; the rest are zero blocks.  Steps:
  1. all type-10 edge-set coverings (Lemma 4 of the structure paper) and type-12 triple choices;
  2. type-8 pairs; row-shape feasibility of (#|y|=1,#|y|=2,#|y|=4) per quadric fibre;
  3. injective placements of the non-zero blocks in F_2^4 up to AGL(4,2) (first two non-zero blocks
     fixed at 0 and 1), pruned by: every NZ edge covered by type-10 blocks sits on an affine 2-flat;
  4. for each placement, a small CNF over codeword variants: exactly one variant per block, every
     type-10 edge flat has U-sign product -1, every quadric row lies in the explicit valid-row table
     (y=Walsh(w)/4, w ternary, entries in {0,1,2,4} in absolute value), and the s=0 row sums to 0.
     The CNF is solved by kissat; every SAT model is decoded and re-verified by a direct 256-point
     Walsh transform.
Output: JSON receipt with counts and all verified solutions found (up to the symmetry breaking).
"""
import argparse, collections, itertools, json, pathlib, subprocess, tempfile, time
import numpy as np

KISSAT = '/opt/homebrew/bin/kissat'


def chi(a, b):
    return 1 - 2 * (bin(a & b).count('1') & 1)


def Q4(s):
    s1, s2, s3, s4 = s & 1, (s >> 1) & 1, (s >> 2) & 1, (s >> 3) & 1
    return (s1 * s2 + s3 * s4 + s3 + s4) % 2


Z0 = [s for s in range(16) if Q4(s) == 0]
NZ = [s for s in range(16) if Q4(s) == 1]
V5 = [1, 2, 7, 11, 15]
EDGES = [(i, j) for i in range(5) for j in range(i + 1, 5)]
NZOF = [V5[i] ^ V5[j] for (i, j) in EDGES]


def walsh16(x):
    return [sum(x[z] * chi(s, z) for z in range(16)) for s in range(16)]


def c0_words():
    words = set()
    for coef in itertools.product(range(3), repeat=6):
        words.add(tuple(sum(cf * chi(s, z) for cf, s in zip(coef, Z0)) % 3 for z in range(16)))
    out = []
    for w in words:
        x = [0 if t == 0 else (1 if t == 1 else -1) for t in w]
        out.append((tuple(x), walsh16(x), sum(abs(t) for t in x)))
    return out


def valid_rows():
    lo = ((np.arange(3 ** 12)[:, None] // (3 ** np.arange(12))) % 3).astype(np.int16) - 1
    H = np.array([[chi(s, z) for z in range(16)] for s in range(16)], dtype=np.int16)
    rows = set()
    for hi in range(3 ** 4):
        top = np.array([(hi // 3 ** i) % 3 - 1 for i in range(4)], dtype=np.int16)
        X = np.concatenate([lo, np.broadcast_to(top, (lo.shape[0], 4))], axis=1)
        W = X @ H.T
        keep = (W % 4 == 0).all(1)
        Y = W[keep] // 4
        ab = np.abs(Y)
        Y = Y[((ab == 0) | (ab == 1) | (ab == 2) | (ab == 4)).all(1)]
        rows.update(map(tuple, Y.tolist()))
    return rows


def affine_flat(pts):
    pts = list(pts)
    if len(pts) != 4 or len(set(pts)) != 4:
        return False
    return (pts[0] ^ pts[1] ^ pts[2] ^ pts[3]) == 0


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--beta', type=int, required=True); p.add_argument('--n6', type=int, required=True)
    p.add_argument('--n8', type=int, required=True); p.add_argument('--max-solutions', type=int, default=20)
    p.add_argument('--output', type=pathlib.Path, required=True); a = p.parse_args()
    if a.output.exists():
        raise FileExistsError(a.output)
    t0 = time.time()
    beta, N6, N8 = a.beta, a.n6, a.n8; alpha = 10 - beta; N0 = 16 - alpha - beta - N6 - N8
    assert N0 >= 0
    words = c0_words(); VR = valid_rows()
    # edge sets of type-10 words and their pairs
    t10 = collections.defaultdict(list); t12 = collections.defaultdict(list)
    t6 = [w for w in words if w[2] == 6]; t8 = collections.defaultdict(list)
    for x, U, n in words:
        if n == 10:
            t10[frozenset(k for k in range(10) if U[NZOF[k]] != 0)].append((x, U))
        elif n == 12:
            t12[frozenset(t for t in Z0 if U[t] != 0)].append((x, U))
        elif n == 8:
            t8[frozenset(t for t in Z0 if U[t] != 0)].append((x, U))
    esl = sorted(t10, key=lambda e: sorted(e))
    triples_of_edge = collections.defaultdict(list)
    for A in t12:
        s = 0
        for t in A:
            s ^= t
        triples_of_edge[NZOF.index(s)].append(A)
    # 1. coverings
    covers = []
    for E12 in itertools.combinations(range(10), beta):
        E12s = set(E12); avail = [e for e in esl if not (e & E12s)]
        def rec(i, left, cov, chosen):
            if left == 0:
                if all(cov[k] == (0 if k in E12s else 4) for k in range(10)):
                    covers.append((E12, tuple(chosen)))
                return
            if i == len(avail):
                return
            es = avail[i]; mx = min([left] + [4 - cov[k] for k in es])
            for mult in range(mx, -1, -1):
                for k in es:
                    cov[k] += mult
                rec(i + 1, left - mult, cov, chosen + [es] * mult)
                for k in es:
                    cov[k] -= mult
        rec(0, alpha, [0] * 10, [])
    allowed = set(); VSUP = set(); VRIDX = collections.defaultdict(list)
    for row in VR:
        allowed.add((sum(abs(t) == 1 for t in row), sum(abs(t) == 2 for t in row), sum(abs(t) == 4 for t in row)))
        VSUP.add((frozenset(c for c in range(16) if abs(row[c]) == 1), frozenset(c for c in range(16) if abs(row[c]) == 2),
                  frozenset(c for c in range(16) if abs(row[c]) == 4)))
        VRIDX[tuple(c for c in range(16) if row[c] != 0)].append(row)
    stats = collections.Counter(); solutions = []
    for E12, chosen in covers:
        for tri in itertools.product(*[triples_of_edge[e] for e in E12]):
            for pairs in itertools.combinations(sorted(t8, key=lambda q: sorted(q)), N8) if N8 else [()]:
                # block objects: (kind, key)
                objs = [('10', es) for es in chosen] + [('12', A) for A in tri] + [('6', None)] * N6 + [('8', P) for P in pairs]
                def zsupp(o):
                    if o[0] == '10':
                        return set(t for t in Z0 if t10[o[1]][0][1][t] != 0)
                    if o[0] == '12':
                        return set(o[1])
                    if o[0] == '6':
                        return set(Z0)
                    return set(o[1])
                mag = {'10': 1, '12': 2, '6': 2, '8': 4}
                ok = True
                for t in Z0:
                    cnt = collections.Counter(mag[o[0]] for o in objs if t in zsupp(o))
                    if (cnt[1], cnt[2], cnt[4]) not in allowed:
                        ok = False; break
                stats['row_shape_feasible' if ok else 'row_shape_infeasible'] += 1
                if not ok:
                    continue
                # 3. placements: assign objects to distinct positions; prune by NZ flats and full-row supports
                n_obj = len(objs)
                edge_members = {k: [i for i, o in enumerate(objs) if o[0] == '10' and k in o[1]] for k in range(10)}
                row_members = {t: [(i, mag[o[0]]) for i, o in enumerate(objs) if t in zsupp(o)] for t in Z0}
                pos = [None] * n_obj; used = set(); placements = []
                def prune(i_new):
                    for k, mem in edge_members.items():
                        if i_new in mem and all(pos[i] is not None for i in mem):
                            if not affine_flat([pos[i] for i in mem]):
                                return False
                    for t, mem in row_members.items():
                        if any(i == i_new for i, _ in mem) and all(pos[i] is not None for i, _ in mem):
                            key = (frozenset(pos[i] for i, g in mem if g == 1), frozenset(pos[i] for i, g in mem if g == 2),
                                   frozenset(pos[i] for i, g in mem if g == 4))
                            if key not in VSUP:
                                return False
                    return True
                def rec_p(i):
                    if i == n_obj:
                        placements.append(tuple(pos)); return
                    choices = [0] if i == 0 else ([1] if i == 1 else range(16))
                    for c in choices:
                        if c in used:
                            continue
                        pos[i] = c; used.add(c)
                        if prune(i):
                            rec_p(i + 1)
                        used.discard(c); pos[i] = None
                rec_p(0)
                stats['placements'] += len(placements)
                for pl in placements:
                    res = solve_signs(objs, pl, t10, t12, t6, t8, VRIDX)
                    stats['sign_systems'] += 1
                    if res is not None:
                        stats['solutions'] += 1
                        if len(solutions) < a.max_solutions:
                            solutions.append(res)
    out = {'config': {'beta': beta, 'N6': N6, 'N8': N8, 'alpha': alpha, 'N0': N0}, 'coverings': len(covers),
           'stats': dict(stats), 'solutions': solutions, 'elapsed_seconds': time.time() - t0,
           'scope': 'exact E=0 rank-four even-half search for one configuration, placements up to AGL(4,2) via fixing two block positions; not a Boolean witness'}
    with a.output.open('x', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True); fh.write('\n')
    print(json.dumps({'config': out['config'], 'coverings': len(covers), 'stats': dict(stats), 'elapsed': round(out['elapsed_seconds'], 1)}))


def solve_signs(objs, pl, t10, t12, t6, t8, VRIDX):
    # variants per object
    var = []
    for o in objs:
        if o[0] == '10':
            var.append(t10[o[1]])
        elif o[0] == '12':
            var.append(t12[o[1]])
        elif o[0] == '6':
            var.append(t6)
        else:
            var.append(t8[o[1]])
    n = 0; cl = []
    def nv():
        nonlocal n; n += 1; return n
    X = [[nv() for _ in v] for v in var]
    for xs in X:
        cl.append(list(xs))
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                cl.append([-xs[i], -xs[j]])
    # NZ edge sign products for type-10 edges: XOR of 'negative' bits must be 1
    for k in range(10):
        mem = [i for i, o in enumerate(objs) if o[0] == '10' and k in o[1]]
        if not mem:
            continue
        s = NZOF[k]; bits = []
        for i in mem:
            b = nv(); bits.append(b)
            for vi, v in enumerate(var[i]):
                cl.append([-X[i][vi], b if v[1][s] < 0 else -b])
        for patt in itertools.product((0, 1), repeat=len(bits)):
            if sum(patt) % 2 == 0:
                cl.append([(-b if q else b) for b, q in zip(bits, patt)])
    # quadric rows: explicit valid vectors with the fixed support, bidirectional channelling
    for t in Z0:
        contrib = [i for i in range(len(objs)) if any(v[1][t] != 0 for v in var[i])]
        supp = tuple(sorted(pl[i] for i in contrib))
        cand = [r for r in VRIDX.get(supp, []) if (t != 0 or sum(r) == 0)]
        if not cand:
            return None
        R = [nv() for _ in cand]
        cl.append(list(R))
        for j, r in enumerate(cand):
            for i in contrib:
                c = pl[i]
                cl.append([-R[j]] + [X[i][vi] for vi, v in enumerate(var[i]) if v[1][t] // 2 == r[c]])
    with tempfile.NamedTemporaryFile('w', suffix='.cnf', delete=False) as fh:
        fh.write(f'p cnf {n} {len(cl)}\n')
        for c in cl:
            fh.write(' '.join(map(str, c)) + ' 0\n')
        path = fh.name
    r = subprocess.run([KISSAT, '-q', path], capture_output=True, text=True)
    pathlib.Path(path).unlink()
    if r.returncode == 20:
        return None
    assert r.returncode == 10, r.returncode
    true = set()
    for line in r.stdout.splitlines():
        if line.startswith('v '):
            true.update(int(t) for t in line[2:].split() if int(t) > 0)
    u = [0] * 256
    blocks = {}
    for i, xs in enumerate(X):
        vi = [j for j, x in enumerate(xs) if x in true]; assert len(vi) == 1
        x = var[i][vi[0]][0]; c = pl[i]; blocks[c] = list(x)
        for z in range(16):
            u[c + 16 * z] = x[z]
    # direct verification
    for A in range(256):
        r_, s_ = A & 15, A >> 4
        w = sum(u[y] * chi(A, y) for y in range(256))
        if Q4(s_) == 0:
            assert w in (0, 8, -8) and (A != 0 or w == 0)
        else:
            assert w in (12, -12)
    return {'u': u, 'm': sum(abs(t) for t in u), 'Z': sum(1 for A in range(256) if sum(u[y] * chi(A, y) for y in range(256)) == 0)}


if __name__ == '__main__':
    main()
