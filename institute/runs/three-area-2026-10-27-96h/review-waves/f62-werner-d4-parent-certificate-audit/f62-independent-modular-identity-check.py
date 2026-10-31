#!/usr/bin/env python3
"""f62 reviewer: implementation-independent modular re-evaluation of the corrected d=4
three-copy certificate orbit identity (all 4675 orbit sums, all 1237 blocks, all 329
equality coefficients, objective), written from the mathematical definitions only.

Differences from the author's ep3core/verify_perd and from the first reviewer's global checker:
  * numpy int64 modular arithmetic (several 20-bit primes); no FLINT, no big-int tensor engine;
  * per-type aggregation with tensordot mode contractions; no (family,kpos,lpos,cut) grouping,
    no hstack/offset layout;
  * dense explicit diagram basis vectors D, K = D C, local map K^T E K by integer matmul
    (no loop counting, no Counter summation);
  * own entry rule with LAST-available factor assignment (the others use first-available),
    which is only valid if the orbit sums really carry the two-sided stabilizer symmetry;
  * objective from cycle counts (author uses cycle counts; first reviewer uses fixed-point
    counts) -- checked here against the explicit 2-replica swap operator trace as well;
  * own orbit labels by min-label propagation over explicitly listed generators, plus a
    Burnside orbit count over the full 432/192-element symmetry group, plus a bijection
    comparison against the first reviewer's union-find labels.
Zero residues modulo every tested prime for every orbit is strong implementation-independent
evidence, not by itself an exact proof (no height bound here). In-memory fault controls follow.
Reads only pinned public/owner bytes; writes only into this review directory.
"""
import hashlib, importlib.util, io, itertools, json, lzma, math, pickle, sys, tarfile, time
from pathlib import Path
import numpy as np
sys.dont_write_bytecode = True

OWN = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart')
OUTDIR = Path(__file__).resolve().parent
ARCHIVE = OWN / 'frontier-20261028-tomar-release-ep3-v3.tar.gz'
CORRECTED = OWN / 'frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz'
GLOBAL_CHECKER = OWN / 'frontier-20261028-independent-d4-global-identity-check.py'
OUT = OUTDIR / 'f62-independent-modular-identity-check-results.json'
EXPECTED = {
    'archive': '2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3',
    'member': '0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f',
    'corrected': 'c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94',
    'global_checker': 'b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d',
}
PERMS = list(itertools.permutations(range(4)))
PIDX = {p: i for i, p in enumerate(PERMS)}
LETTERS = {'31': 'aaab', '22': 'aabb', '13': 'bbba'}
SWAP03 = (3, 1, 2, 0)
NWORDS = 24 ** 4


def sha256(b): return hashlib.sha256(b).hexdigest()


class DataOnlyUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        raise pickle.UnpicklingError('global/class loading forbidden: %s.%s' % (module, name))


def compose(a, b): return tuple(a[b[i]] for i in range(4))


def inverse(a):
    r = [0] * 4
    for i, j in enumerate(a): r[j] = i
    return tuple(r)


def ncycles(p):
    seen, c = set(), 0
    for i in range(len(p)):
        if i in seen: continue
        c += 1; j = i
        while j not in seen: seen.add(j); j = p[j]
    return c


def basis(n, m): return np.array(list(itertools.product(range(n), repeat=m)), dtype=np.int64)


B4 = basis(4, 4); B43 = basis(4, 3); B2 = basis(2, 4); B23 = basis(2, 3)


def perm_matrix(B, p):
    """V_p[x, y] = [x[p[j]] == y[j] for all j]  (so V_p V_q = V_{p o q})."""
    return np.all(B[:, None, list(p)] == B[None, :, :], axis=2).astype(np.int64)


def entry_matrix(B, p, kpos, lpos):
    """E[i, j] = V_p[k(i,j), l(i,j)] with k_m = (i|j)[slot] from kpos[m], l likewise from lpos."""
    N = B.shape[0]
    def gather(pos):
        cols = [np.broadcast_to(B[:, None, s] if w == 'i' else B[None, :, s], (N, N)) for w, s in pos]
        return np.stack(cols, axis=2)
    K, L = gather(kpos), gather(lpos)
    return np.all(K[:, :, list(p)] == L, axis=2).astype(np.int8)


def traced_perm(B, n, p, slot, order):
    """(Tr_slot V_p)[row, col] on the survivors placed at replica positions `order`."""
    N = B.shape[0]
    out = np.zeros((N, N), dtype=np.int64)
    for v in range(n):
        a = np.empty((N, 4), dtype=np.int64); a[:, slot] = v
        for i, s in enumerate(order): a[:, s] = B[:, i]
        out += np.all(a[:, None, list(p)] == a[None, :, :], axis=2)
    return out


def diagram_vectors(keys, n, m):
    """Explicit D (n^m x #keys): key = (pairs, top, bottom); x[a]=x[b]=v on pairs, x[s]=t on top,
    x[s]=n+r (r<0) on bottom; every slot covered exactly once."""
    D = np.zeros((n ** m, len(keys)), dtype=np.int64)
    for c, (pairs, top, bottom) in enumerate(keys):
        slots = [s for a, b in pairs for s in (a, b)] + [s for s, _ in top] + [s for s, _ in bottom]
        if sorted(slots) != list(range(m)): raise ValueError('diagram key does not cover slots once: %r' % ((pairs, top, bottom),))
        for vals in itertools.product(range(n), repeat=len(pairs)):
            x = [None] * m
            for (a, b), v in zip(pairs, vals): x[a] = x[b] = v
            for s, t in top: x[s] = t
            for s, r in bottom: x[s] = n + r
            if any(not 0 <= v < n for v in x): raise ValueError('diagram value out of range')
            idx = 0
            for v in x: idx = idx * n + v
            D[idx, c] += 1
    return D


def parse_label(lab):
    f, l, r = lab.split('_')
    part = lambda s: () if s == 'e' else tuple(int(c) for c in s)
    return int(f[1:]), part(l), part(r)


def entry_rule(row_u, row_v):
    """Gram entry |u><v|[i,j] = u(i) conj(v(j)) as Y_fam[k;l]; LAST-available assignment."""
    tu, tv = row_u.split(), row_v.split()
    if len(tu) != 4 or len(tv) != 4: raise ValueError('row length')
    unc, con = [], []
    for m, (x, y) in enumerate(zip(tu, tv)):
        cx, cy = x.endswith('*'), y.endswith('*')
        if cx != cy or x[0] not in 'ab' or y[0] not in 'ab': raise ValueError('row tokens %r %r' % (x, y))
        if cx: unc.append((y[0], ('j', m))); con.append((x[0], ('i', m)))
        else: unc.append((x[0], ('i', m))); con.append((y[0], ('j', m)))
    fams = [f for f, L in LETTERS.items() if sorted(L) == sorted(v[0] for v in unc)]
    if len(fams) != 1 or sorted(v[0] for v in unc) != sorted(v[0] for v in con): raise ValueError('family')
    fam = fams[0]
    def assign(pool):
        pool = list(pool); out = []
        for letter in LETTERS[fam]:
            idx = max(i for i, v in enumerate(pool) if v[0] == letter)
            out.append(pool.pop(idx)[1])
        return tuple(out)
    return fam, assign(unc), assign(con)


def load():
    raw = ARCHIVE.read_bytes()
    if sha256(raw) != EXPECTED['archive']: raise ValueError('archive hash')
    with tarfile.open(fileobj=io.BytesIO(raw), mode='r:gz') as tf:
        cert = tf.extractfile('release_ep3/certs/ep3_perd_d4.pkl.xz').read()
    if sha256(cert) != EXPECTED['member']: raise ValueError('member hash')
    pkg = DataOnlyUnpickler(io.BytesIO(lzma.decompress(cert, memlimit=256 * 1024 * 1024))).load()
    if (pkg['format'], pkg['k'], pkg['d'], pkg['nrow']) != ('ep3-perd-v1', 3, 4, 4675): raise ValueError('metadata')
    cb = CORRECTED.read_bytes()
    if sha256(cb) != EXPECTED['corrected']: raise ValueError('corrected hash')
    corr = json.loads(lzma.decompress(cb, memlimit=256 * 1024 * 1024))
    if corr['source_member_sha256'] != EXPECTED['member'] or corr['source_archive_sha256'] != EXPECTED['archive']: raise ValueError('corrected provenance')
    if corr['dimension'] != 4 or corr['copies'] != 3 or len(corr['matrices']) != len(pkg['types']): raise ValueError('corrected shape')
    return pkg, corr


class Evaluator:
    def __init__(self, pkg):
        self.pkg = pkg
        self.types = pkg['types']
        self.Kcache, self.Ecache, self.localcache, self.eqcache = {}, {}, {}, {}
        for mod in sorted({m for t in self.types for m in t['modules'][:3]}):
            side, cut, lab = mod.split('|')
            if side != 'S': raise ValueError(mod)
            cut = tuple(int(x) for x in cut.split(',')) if cut else ()
            keys, C = pkg['diagrams'][(4, cut)][parse_label(lab)]
            C = np.array(C, dtype=np.int64)
            self.Kcache[mod] = diagram_vectors(keys, 4, 4) @ C          # (256, dim)
        self.aux = {k: np.array(v, dtype=np.int64) for k, v in pkg['aux'].items()}
        self.dims = []
        for t in self.types:
            d = [self.Kcache[m].shape[1] for m in t['modules'][:3]] + [self.aux[t['modules'][3]].shape[1]]
            n = math.prod(d)
            if len(t['W']) != len(t['rows']) * n or any(len(r) != t['r'] for r in t['W']): raise ValueError('W shape')
            self.dims.append(d)

    def E(self, kpos, lpos, aux):
        key = (kpos, lpos, aux)
        if key not in self.Ecache:
            B = B2 if aux else B4
            self.Ecache[key] = [entry_matrix(B, p, kpos, lpos) for p in PERMS]
        return self.Ecache[key]

    def local(self, mod, aux, kpos, lpos, rule_swap=False):
        key = (mod, aux, kpos, lpos)
        if key not in self.localcache:
            K = self.aux[mod] if aux else self.Kcache[mod]
            Es = self.E(kpos, lpos, aux)
            self.localcache[key] = np.stack([K.T @ E @ K for E in Es])   # (24, dim, dim)
        return self.localcache[key]

    def block_tensor(self, ti, r, s, Zp, p, rule=None):
        """Word tensor (p1,p2,p3,pQ) of <W_r Z W_s^T, M_rs(V_w)> modulo p; rule overrides (fam,kpos,lpos)."""
        t = self.types[ti]; d = self.dims[ti]; n = math.prod(d)
        fam, kpos, lpos = rule if rule else entry_rule(t['rows'][r], t['rows'][s])
        A = [self.local(t['modules'][l], l == 3, kpos, lpos) for l in range(4)]
        W = np.array(t['W'], dtype=np.int64)
        G = ((W[r * n:(r + 1) * n] @ Zp) % p @ W[s * n:(s + 1) * n].T) % p
        X = G.reshape(d + d)
        X = np.tensordot(A[0], X, axes=([1, 2], [0, 4])) % p   # (p1, a2,a3,a4, b2,b3,b4)
        X = np.tensordot(A[1], X, axes=([1, 2], [1, 4])) % p   # (p2, p1, a3,a4, b3,b4)
        X = np.tensordot(A[2], X, axes=([1, 2], [2, 4])) % p   # (p3, p2, p1, a4, b4)
        X = np.tensordot(A[3], X, axes=([1, 2], [3, 4])) % p   # (pQ, p3, p2, p1)
        return fam, X.transpose(3, 2, 1, 0)

    def eq_rows(self, spec, override_order=None):
        side, slot, order, kind, mkeys = spec
        order = tuple(override_order) if override_order else tuple(order)
        key = (side, slot, order, kind, tuple(mkeys))
        if key in self.eqcache: return self.eqcache[key]
        blocks = []
        for mk in mkeys:
            if side == 'S':
                keys, C = self.pkg['diagrams'][(3, ())][parse_label(mk.split('|')[-1])]
                J = diagram_vectors(keys, 4, 3) @ np.array(C, dtype=np.int64)       # (64, dim)
                ops = [traced_perm(B43, 4, p, slot, order) for p in PERMS]
            elif kind == 'del':
                J = self.aux[mk]
                if J.shape[0] != 8: raise ValueError('aux del compression rows')
                ops = [traced_perm(B23, 2, p, slot, order) for p in PERMS]
            elif kind == 'stiefel_aux':
                J = self.aux[mk]
                if J.shape[0] != 16: raise ValueError('aux stiefel compression rows')
                nat = tuple(i for i in range(4) if i != slot)
                rest = np.array([[row[i] for i in nat] for row in B2])
                ridx = rest @ np.array([4, 2, 1])
                ops = []
                for p in PERMS:
                    tr = traced_perm(B23, 2, p, slot, nat)
                    same = (B2[:, None, slot] == B2[None, :, slot]).astype(np.int64)
                    ops.append(2 * perm_matrix(B2, p) - same * tr[np.ix_(ridx, ridx)])
            else:
                raise ValueError(kind)
            blocks.append(np.stack([(J.T @ O @ J).ravel() for O in ops], axis=1))   # (dim^2, 24)
        self.eqcache[key] = np.concatenate(blocks, axis=0)
        return self.eqcache[key]

    def eq_tensor(self, part, coeffs, p, override_order=None):
        Es = [self.eq_rows(spec, override_order) for spec in part['local']]
        Lt = np.zeros([E.shape[0] for E in Es], dtype=np.int64)
        for index, value in coeffs:
            if len(index) != 4 or any(not 0 <= i < Es[l].shape[0] for l, i in enumerate(index)): raise ValueError('equality index')
            Lt[tuple(index)] = (Lt[tuple(index)] + value) % p
        T = Lt
        for l in range(4): T = np.tensordot(T, Es[l], axes=([0], [0])) % p
        return T  # (p1,p2,p3,pQ)


def objective(complement=False):
    cyc = np.array([ncycles(p) for p in PERMS]); cycs = np.array([ncycles(compose(SWAP03, p)) for p in PERMS])
    vs = 2 * 4 ** cyc - 4 ** cycs if not complement else 2 * 4 ** cycs - 4 ** cyc
    vq = 2 ** cycs if not complement else 2 ** cyc
    return np.einsum('a,b,c,d->abcd', vs, vs, vs, vq).astype(np.int64)


def objective_from_operators():
    """Direct check of the cycle-count objective on every word via explicit 2-replica operators:
    Tr[(F_Q prod_i (I - F_i/2))_{03} (x) I_{12} V_w] computed from 4-replica traces Tr V_p and Tr F_03 V_p."""
    trV4 = np.array([np.trace(perm_matrix(B4, p)) for p in PERMS])
    F = perm_matrix(B4, SWAP03)
    trFV4 = np.array([np.trace(F @ perm_matrix(B4, p)) for p in PERMS])
    trV2 = np.array([np.trace(perm_matrix(B2, p)) for p in PERMS])
    F2 = perm_matrix(B2, SWAP03)
    trFV2 = np.array([np.trace(F2 @ perm_matrix(B2, p)) for p in PERMS])
    vs = 2 * trV4 - trFV4
    return np.einsum('a,b,c,d->abcd', vs, vs, vs, trFV2).astype(np.int64)


def orbit_labels(letters, left=True, right=True, inv=True, sites=True):
    codes = np.arange(NWORDS, dtype=np.int64)
    d = [(codes // 24 ** (3 - l)) % 24 for l in range(4)]
    mul = np.array([[PIDX[compose(p, q)] for q in PERMS] for p in PERMS])
    invm = np.array([PIDX[inverse(p)] for p in PERMS])
    stab = [g for g in PERMS if all(letters[g[i]] == letters[i] for i in range(4))]
    enc = lambda ds: ((ds[0] * 24 + ds[1]) * 24 + ds[2]) * 24 + ds[3]
    maps = []
    for g in stab:
        gi = PIDX[g]
        if left: maps.append(enc([mul[gi][x] for x in d]))
        if right: maps.append(enc([mul[x, gi] for x in d]))
    if inv: maps.append(enc([invm[x] for x in d]))
    if sites: maps += [enc([d[1], d[0], d[2], d[3]]), enc([d[0], d[2], d[1], d[3]])]
    lab = codes.copy()
    while True:
        new = lab.copy()
        for m in maps: np.minimum(new, lab[m], out=new)
        if np.array_equal(new, lab): break
        lab = new
    uniq, oid = np.unique(lab, return_inverse=True)
    return oid.astype(np.int64), len(uniq), len(stab)


def burnside_count(letters):
    codes = np.arange(NWORDS, dtype=np.int64)
    d = [(codes // 24 ** (3 - l)) % 24 for l in range(4)]
    mul = np.array([[PIDX[compose(p, q)] for q in PERMS] for p in PERMS])
    invm = np.array([PIDX[inverse(p)] for p in PERMS])
    stab = [g for g in PERMS if all(letters[g[i]] == letters[i] for i in range(4))]
    enc = lambda ds: ((ds[0] * 24 + ds[1]) * 24 + ds[2]) * 24 + ds[3]
    total, count = 0, 0
    for s in stab:
        for t in stab:
            base = [mul[PIDX[s]][mul[x, PIDX[t]]] for x in d]
            for e in (0, 1):
                ds = [invm[x] for x in base] if e else base
                for pi in itertools.permutations(range(3)):
                    img = [None] * 4
                    for i in range(3): img[pi[i]] = ds[i]
                    img[3] = ds[3]
                    total += int(np.count_nonzero(enc(img) == codes)); count += 1
    if total % count: raise ValueError('Burnside sum not divisible by group order')
    return total // count, count


def is_prime(n):
    if n < 2: return False
    for q in range(2, math.isqrt(n) + 1):
        if n % q == 0: return False
    return True


def main():
    t0 = time.monotonic()
    pkg, corr = load()
    ev = Evaluator(pkg)
    if sha256(GLOBAL_CHECKER.read_bytes()) != EXPECTED['global_checker']: raise ValueError('global checker hash')
    report = {'kind': 'f62_independent_modular_d4_certificate_orbit_identity', 'inputs_sha256': dict(EXPECTED)}
    # orbits: own labels, Burnside counts, bijection with the first reviewer's union-find
    spec = importlib.util.spec_from_file_location('first_reviewer_global_checker', GLOBAL_CHECKER)
    gc = importlib.util.module_from_spec(spec); spec.loader.exec_module(gc)
    orbits, orbit_report = {}, {}
    for f, letters in LETTERS.items():
        oid, norb, nstab = orbit_labels(letters)
        theirs, ntheirs = gc.generate_orbits(letters)
        pairs = set(zip(oid.tolist(), theirs.tolist()))
        bij = len(pairs) == norb == ntheirs
        bcount, gorder = burnside_count(letters)
        orbits[f] = (oid, norb)
        orbit_report[f] = {'own_orbits': norb, 'first_reviewer_orbits': int(ntheirs), 'label_bijection': bij,
                           'burnside_orbits': bcount, 'symmetry_group_order': gorder, 'stabilizer_order': nstab,
                           'orbit_size_min': int(np.bincount(oid).min()), 'orbit_size_max': int(np.bincount(oid).max())}
    report['orbits'] = orbit_report
    report['all_orbit_count'] = sum(v[1] for v in orbits.values())
    # objective cross-check
    obj = objective()
    report['objective_cycle_vs_operator_trace_mismatches'] = int(np.count_nonzero(obj != objective_from_operators()))
    report['objective_denominator'] = 8 * (2 * 4 ** 3) ** 4
    # rational data
    Zq = [[(int(a), int(b)) for a, b in m['values']] for m in corr['matrices']]
    for m, t in zip(corr['matrices'], pkg['types']):
        if m['r'] != t['r'] or len(m['values']) != t['r'] ** 2: raise ValueError('matrix shape')
    eqc = [(e['group'], tuple(e['index']), int(e['numerator']), int(e['denominator'])) for e in corr['equality_coefficients']]
    if any(g not in pkg['eq_groups'] for g, *_ in eqc): raise ValueError('unknown equality group')
    maxbits = max(b.bit_length() for M in Zq for _, b in M)
    report['corrected_matrix_count'] = len(Zq); report['corrected_equality_count'] = len(eqc)
    report['max_matrix_denominator_bits'] = maxbits
    report['max_equality_denominator_bits'] = max(d.bit_length() for *_, d in eqc)
    # symmetric check of the rationals (exact)
    asym = [i for i, (M, t) in enumerate(zip(Zq, pkg['types'])) if any(M[a * t['r'] + b] != M[b * t['r'] + a] for a in range(t['r']) for b in range(t['r']))]
    report['nonsymmetric_corrected_matrices'] = asym
    # primes
    primes, q = [], 2 ** 20
    while len(primes) < 5:
        q -= 1
        if is_prime(q): primes.append(q)
    report['primes'] = primes
    per_prime = []
    baseline = None
    for p in primes:
        tp = time.monotonic()
        try:
            Zmod = [np.array([a % p * pow(b, -1, p) % p for a, b in M], dtype=np.int64).reshape(t['r'], t['r']) for M, t in zip(Zq, pkg['types'])]
            lam = [(g, idx, a % p * pow(b, -1, p) % p) for g, idx, a, b in eqc]
            inv_den = pow(report['objective_denominator'], -1, p)
        except ValueError:
            per_prime.append({'prime': p, 'skipped': 'denominator not invertible'}); continue
        acc = {f: np.zeros((24,) * 4, dtype=np.int64) for f in LETTERS}
        nblocks = 0
        for ti, t in enumerate(pkg['types']):
            for r in range(len(t['rows'])):
                for s in range(len(t['rows'])):
                    fam, X = ev.block_tensor(ti, r, s, Zmod[ti], p)
                    acc[fam] -= X; nblocks += 1
            if ti % 100 == 0:
                for f in acc: np.mod(acc[f], p, out=acc[f])
        acc['31'] += (obj % p) * inv_den % p
        for name, group in pkg['eq_groups'].items():
            coeffs = [(idx, v) for g, idx, v in lam if g == name]
            for part in group['parts']:
                acc[part['family']] -= int(part['sign']) * ev.eq_tensor(part, coeffs, p)
        for f in acc: np.mod(acc[f], p, out=acc[f])
        res = {}
        for f, (oid, norb) in orbits.items():
            osum = np.zeros(norb, dtype=np.int64); np.add.at(osum, oid, acc[f].ravel()); osum %= p
            res[f] = {'nonzero_orbit_residues': int(np.count_nonzero(osum)), 'orbits': norb,
                      'nonzero_word_level_residues': int(np.count_nonzero(acc[f]))}
        per_prime.append({'prime': p, 'blocks_evaluated': nblocks, 'residues': res, 'seconds': round(time.monotonic() - tp, 3)})
        print('prime', p, res, round(time.monotonic() - tp, 1), 's', flush=True)
        if baseline is None: baseline = (p, {f: acc[f].copy() for f in acc}, Zmod, lam, inv_den)
    report['per_prime'] = per_prime
    ok = all('residues' in x and all(v['nonzero_orbit_residues'] == 0 for v in x['residues'].values()) for x in per_prime) and any('residues' in x for x in per_prime)
    # ---- in-memory fault controls on the baseline prime (linearity: add the delta of the mutated term)
    p, acc0, Zmod, lam, inv_den = baseline
    def orbit_nonzero(f, tensor):
        oid, norb = orbits[f]; osum = np.zeros(norb, dtype=np.int64); np.add.at(osum, oid, (tensor % p).ravel()); return int(np.count_nonzero(osum % p))
    controls = {}
    # (a) single 1x1 multiplier +1
    ti = next(i for i, t in enumerate(pkg['types']) if t['r'] == 1 and len(t['rows']) == 1)
    fam, X = ev.block_tensor(ti, 0, 0, np.array([[1]], dtype=np.int64), p)
    controls['single_row_1x1_multiplier_plus_1'] = {'type_index': ti, 'family': fam, 'nonzero_orbit_residues': orbit_nonzero(fam, acc0[fam] - X)}
    # (b) coupled Gram diagonal +1 at (0,0)
    gi = next(i for i, t in enumerate(pkg['types']) if len(t['rows']) == 2)
    Zunit = np.zeros((pkg['types'][gi]['r'],) * 2, dtype=np.int64); Zunit[0, 0] = 1
    delta = {f: np.zeros((24,) * 4, dtype=np.int64) for f in LETTERS}
    for r in range(2):
        for s in range(2):
            fam, X = ev.block_tensor(gi, r, s, Zunit, p); delta[fam] -= X
    controls['coupled_gram_diagonal_plus_1'] = {'type_index': gi, 'nonzero_orbit_residues': {f: orbit_nonzero(f, acc0[f] + delta[f]) for f in LETTERS}}
    # (c) one aab equality coefficient +1
    aab = pkg['eq_groups']['aab']; idx0 = next(idx for g, idx, v in lam if g == 'aab')
    dl = {f: np.zeros((24,) * 4, dtype=np.int64) for f in LETTERS}
    for part in aab['parts']: dl[part['family']] -= int(part['sign']) * ev.eq_tensor(part, [(idx0, 1)], p)
    controls['aab_equality_coefficient_plus_1'] = {'index': list(idx0), 'nonzero_orbit_residues': {f: orbit_nonzero(f, acc0[f] + dl[f]) for f in LETTERS}}
    # (d) objective trace/swap complement convention
    objc = objective(complement=True)
    controls['objective_complement_convention'] = {'nonzero_orbit_residues_31': orbit_nonzero('31', acc0['31'] - (obj % p) * inv_den % p + (objc % p) * inv_den % p)}
    # (e) abb: replace the 13-part survivor order (3,0,2) by (0,2,3)
    abb = pkg['eq_groups']['abb']; coeffs = [(idx, v) for g, idx, v in lam if g == 'abb']
    part13 = next(pt for pt in abb['parts'] if pt['family'] == '13')
    Told = ev.eq_tensor(part13, coeffs, p)
    Tnew = ev.eq_tensor({'local': [(s[0], s[1], (0, 2, 3), s[3], s[4]) for s in part13['local']], 'family': '13', 'sign': part13['sign']}, coeffs, p)
    controls['abb_13_part_order_302_replaced_by_023'] = {'nonzero_orbit_residues_13': orbit_nonzero('13', acc0['13'] + int(part13['sign']) * Told - int(part13['sign']) * Tnew)}
    # (f) coupled Gram off-diagonal index rule transposed (use the (s,r) rule for the (r,s) block)
    dg = {f: np.zeros((24,) * 4, dtype=np.int64) for f in LETTERS}
    for ti, t in enumerate(pkg['types']):
        if len(t['rows']) != 2: continue
        for r, s in ((0, 1), (1, 0)):
            fam, Xold = ev.block_tensor(ti, r, s, Zmod[ti], p)
            fam2, Xnew = ev.block_tensor(ti, r, s, Zmod[ti], p, rule=entry_rule(t['rows'][s], t['rows'][r]))
            dg[fam] += Xold; dg[fam2] -= Xnew
    controls['coupled_offdiagonal_rule_transposed_all_111_types'] = {f: orbit_nonzero(f, acc0[f] + dg[f]) for f in LETTERS}
    # (g) which symmetries are load-bearing: residues summed over FINER partitions
    finer = {}
    for label, kw in {'no_inversion': dict(inv=False), 'no_site_permutations': dict(sites=False),
                      'left_stabilizer_only': dict(right=False), 'no_stabilizer': dict(left=False, right=False)}.items():
        finer[label] = {}
        for f, letters in LETTERS.items():
            oid, norb, _ = orbit_labels(letters, **kw)
            osum = np.zeros(norb, dtype=np.int64); np.add.at(osum, oid, acc0[f].ravel())
            finer[label][f] = {'classes': norb, 'nonzero_class_residues': int(np.count_nonzero(osum % p))}
    controls['finer_partition_residues'] = finer
    report['fault_controls_prime'] = p
    report['fault_controls'] = controls
    report['numpy_version'] = np.__version__; report['python_version'] = sys.version.split()[0]
    report['elapsed_seconds'] = round(time.monotonic() - t0, 3)
    report['scope'] = ('All 4675 orbit sums of the corrected d4 certificate identity re-evaluated modulo 20-bit primes with an '
                       'independent implementation (numpy int64; no FLINT; per-type aggregation; explicit basis vectors; own '
                       'entry rule/orbits/objective). Zero residues mod every prime is implementation-independent evidence for the '
                       'exact identity, not a height-bounded proof. No PSD, physical-bridge, novelty or general-d claim.')
    report['verdict'] = 'PASS' if ok else 'FAIL'
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
