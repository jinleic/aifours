"""Parent independent PARTIAL check of the Sun k6 (Core5(6)) engine-v3 certificate set.
Written by the parent from CERT-FORMAT-k6-v1.md (45f5d73c...) and rules-k6-v1..v3 / proof-k6-lemmas-v1 only;
no engine code was read.  Checks: (U) universe of T-consistent labelled leaves per type (count + sha256 of the
sorted code list), (O) orbit representatives cover the universe exactly once under the type stabiliser,
(K) every K witness, (R) every RLP witness (all admissible q, all 31 subsets, exact Fractions),
(N) every N26 witness with the SAFE condition (every admissible tau of every triple avoids primes >=5, and 3 if v=E3),
(P) every PB/Ppair witness, (L) every RPLP witness (exact integer arithmetic after common-denominator scaling).
FH5 witnesses are only counted here (checked by the separate-author checker).
Usage: python3 -B check_sun_k6_parent_v1.py ENGINE_DIR OUTDIR   (OUTDIR must not exist)
"""
import gzip
import hashlib
import itertools
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

BUDGET = 3000.0
T0 = time.monotonic()
EDGES = [(i, j) for j in range(6) for i in range(j)]          # sorted by (j, i)
EIDX = {e: k for k, e in enumerate(EDGES)}
TYPES = [(None, 0, None), (None, 0, 0), (0, 1, None), (0, 1, 0), (0, 1, 1), (0, 2, None), (0, 2, 0), (0, 2, 1)]


def eid(a, b):
    return EIDX[(a, b) if a < b else (b, a)]


def gtab(alpha, z, t):
    e2, c2, e3 = t
    if alpha == 2:
        return 2 if z == e2 else 1
    if alpha == 3:
        return 3 if z == e3 else 1
    if alpha == 4:
        if z == e2:
            return 4 if c2 == 2 else 2
        return 1
    return 1


def lcm(a, b):
    return a * b // math.gcd(a, b)


def tau_min(al, a, b, c, t):
    """triangle a,b,c with al(x,y) giving alpha."""
    x = al(a, b) // gtab(al(a, b), c, t)
    y = al(a, c) // gtab(al(a, c), b, t)
    z = al(b, c) // gtab(al(b, c), a, t)
    return lcm(lcm(x, y), z)


def tau_max(al, a, b, c):
    return min(al(a, b) * al(a, c), al(a, b) * al(b, c), al(a, c) * al(b, c))


def t_pass_table(a, b, c, t):
    """64-entry table indexed by 16*(alpha_ab-1)+4*(alpha_ac-1)+(alpha_bc-1)."""
    out = np.zeros(64, dtype=bool)
    for ab in range(1, 5):
        for ac in range(1, 5):
            for bc in range(1, 5):
                d = {(a, b): ab, (a, c): ac, (b, c): bc}
                al = lambda x, y: d[(x, y) if (x, y) in d else (y, x)]
                out[16 * (ab - 1) + 4 * (ac - 1) + (bc - 1)] = tau_min(al, a, b, c, t) <= tau_max(al, a, b, c)
    return out


def universe(t):
    """All labellings (rows of alpha-1 digits, edge order E) passing T on all 20 triangles."""
    cols = np.zeros((1, 0), dtype=np.int8)
    for j in range(1, 6):
        new = np.array(list(itertools.product(range(4), repeat=j)), dtype=np.int8)   # edges (0,j),...,(j-1,j)
        n1 = new.shape[0]
        tabs = [(a, b, t_pass_table(a, b, j, t)) for a in range(j) for b in range(a + 1, j)]
        parts = []
        for s in range(0, cols.shape[0], 2048):
            blk = cols[s:s + 2048]
            n0 = blk.shape[0]
            cand = np.concatenate([np.repeat(blk, n1, axis=0), np.tile(new, (n0, 1))], axis=1)
            for a, b, tab in tabs:
                idx = 16 * cand[:, eid(a, b)].astype(np.int32) + 4 * cand[:, eid(a, j)] + cand[:, eid(b, j)]
                cand = cand[tab[idx]]
            parts.append(cand)
        cols = np.concatenate(parts, axis=0)
    return cols


def codes_int(rows):
    w = (4 ** np.arange(14, -1, -1)).astype(np.int64)
    return rows.astype(np.int64) @ w


def code_str(x):
    s = []
    for _ in range(15):
        s.append(str(x % 4 + 1))
        x //= 4
    return ''.join(reversed(s))


def sha_sorted(ints):
    hsh = hashlib.sha256()
    for x in np.sort(ints):
        hsh.update((code_str(int(x)) + '\n').encode())
    return hsh.hexdigest()


def stabiliser(t):
    e2, _, e3 = t
    return [p for p in itertools.permutations(range(6))
            if (e2 is None or p[e2] == e2) and (e3 is None or p[e3] == e3)]


def perm_edge_maps(perms):
    maps = []
    for p in perms:
        m = np.empty(15, dtype=np.int64)
        for k, (i, j) in enumerate(EDGES):
            m[eid(p[i], p[j])] = k        # new[eid(p i, p j)] = old[k]
        maps.append(m)
    return maps


class Pat:
    def __init__(self, rep, t):
        self.t = t
        self.e2, self.c2, self.e3 = t
        self.a = [[0] * 6 for _ in range(6)]
        for k, (i, j) in enumerate(EDGES):
            self.a[i][j] = self.a[j][i] = int(rep[k])

    def al(self, x, y):
        return self.a[x][y]


def check_K(P, w):
    v, S = w[0], list(w[1])
    if len(set(S)) != len(S) or v in S or any(not (0 <= s < 6) for s in S):
        return False
    if sum(P.al(i, v) for i in S) < 5:
        return False
    for i, j in itertools.combinations(S, 2):
        if tau_min(P.al, i, v, j, P.t) != P.al(i, v) * P.al(v, j):
            return False
    return True


def neigh_stats(P, v):
    N = [j for j in range(6) if j != v]
    st = []
    for j in N:
        d = P.c2 if j == P.e2 else 0
        f = 1 if j == P.e3 else 0
        st.append((d, f))
    return N, st


def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def v3(n):
    c = 0
    while n % 3 == 0:
        n //= 3
        c += 1
    return c


SAT = 30


def allowed_sets(q, st):
    e2 = [v2(q[x]) + (0 if st[x][0] == 0 else (1 if st[x][0] == 1 else SAT)) for x in range(5)]
    e3 = [v3(q[x]) + (SAT if st[x][1] == 1 else 0) for x in range(5)]
    mg = {}
    for x, y in itertools.combinations(range(5), 2):
        mg[(x, y)] = 2 ** min(e2[x], e2[y]) * 3 ** min(e3[x], e3[y])
    out = []
    for r in range(1, 6):
        for S in itertools.combinations(range(5), r):
            ok = True
            if r >= 2:
                for tsz in range(2, r + 1):
                    for T in itertools.combinations(S, tsz):
                        if not any(mg[(x, y)] >= tsz for x, y in itertools.combinations(T, 2)):
                            ok = False
                            break
                    if not ok:
                        break
            if ok:
                out.append(S)
    return out


_rlp_cache = {}


def rlp_key_ok(key, duals, q, st):
    if key in _rlp_cache:
        return _rlp_cache[key]
    ok = False
    ent = duals.get(key)
    if ent is not None:
        y = ent['y'] if isinstance(ent, dict) else ent
        y = [Fraction(s) for s in y]
        if len(y) == 5 and all(x >= 0 for x in y):
            if all(sum(y[x] for x in S) <= 1 for S in allowed_sets(q, st)):
                ok = sum(Fraction(q[x], 5) * y[x] for x in range(5)) >= 1
    _rlp_cache[key] = ok
    return ok


def rlp_key(q, st):
    return ','.join(str(x) for x in q) + '|' + ';'.join('%d%d' % s for s in st)


def admissible_qs(P, v, N):
    return list(itertools.product(*[range(1, 5 - P.al(v, j) + 1) for j in N]))


def check_RLP(P, w, duals):
    v = w[0]
    N, st = neigh_stats(P, v)
    for q in admissible_qs(P, v, N):
        if not rlp_key_ok(rlp_key(q, st), duals, q, st):
            return False
    return True


def admissible_taus(tmin, tmax):
    return [x for x in range(tmin, tmax + 1) if x % tmin == 0]


def check_N26(P, w):
    v = w[0]
    if v == P.e2:
        return False
    N = [j for j in range(6) if j != v]
    if any(P.al(v, j) != 2 for j in N):
        return False
    if any(P.al(j, k) not in (2, 4) for j, k in itertools.combinations(N, 2)):
        return False
    for j, k, l in itertools.combinations(N, 3):
        tmin, tmax = tau_min(P.al, j, k, l, P.t), tau_max(P.al, j, k, l)
        if tmin > tmax:
            return False      # T-inconsistent rep would be an error anyway
        for tau in admissible_taus(tmin, tmax):
            m = tau
            for pr in (2, 3):
                while m % pr == 0:
                    m //= pr
            if m != 1:
                return False
            if v == P.e3 and tau % 3 == 0:
                return False
    return True


def lohi(P, v, j, k):
    """lo, hi for |X_j cap X_k| in units |G| (Fractions), per CERT-FORMAT PB."""
    xj, xk = Fraction(P.al(v, j), 5), Fraction(P.al(v, k), 5)
    ajk = P.al(j, k)
    u = Fraction(1, 5 * gtab(ajk, v, P.t))
    lo0 = max(Fraction(tau_min(P.al, v, j, k, P.t), 5 * ajk), xj + xk - 1, Fraction(0))
    lo = math.ceil(lo0 / u) * u
    m = min(xj, xk)
    hi = math.floor(m / u) * u
    if hi == m:
        avj, avk = P.al(v, j), P.al(v, k)
        akj = ajk
        if xj < xk:
            barred = not (avj + akj <= 4)
        elif xk < xj:
            barred = not (avk + ajk <= 4)
        else:
            barred = not ((avj + akj <= 4) and (avk + ajk <= 4))
        if barred:
            hi -= u
    return lo, hi


def check_P(P, w, rule):
    v = w[0]
    if rule == 'Ppair':
        j, k = w[1]
        lo, hi = lohi(P, v, j, k)
        return lo > hi
    S = list(w[1])
    N = [j for j in range(6) if j != v]
    for j, k in itertools.combinations(N, 2):
        lo, hi = lohi(P, v, j, k)
        if lo > hi:
            return False
    tot = sum(1 - Fraction(P.al(v, j), 5) for j in S)
    for j, k in itertools.combinations(sorted(S), 2):
        lo, hi = lohi(P, v, j, k)
        tot -= 1 - Fraction(P.al(v, j), 5) - Fraction(P.al(v, k), 5) + hi
    return tot >= 1


def check_RPLP(P, w, duals):
    v, certs = w[0], w[1]
    N, st = neigh_stats(P, v)
    qs = admissible_qs(P, v, N)
    if len(certs) != len(qs):
        return False
    pairs = list(itertools.combinations(range(5), 2))
    forced = []
    for wi, ji in itertools.permutations(range(5), 2):
        ww, jj = N[wi], N[ji]
        if tau_min(P.al, v, ww, jj, P.t) >= P.al(v, ww) * P.al(ww, jj):
            forced.append((wi, ji))
    LH = {}
    for (x, y) in pairs:
        LH[(x, y)] = lohi(P, v, N[x], N[y])
    for q, cert in zip(qs, certs):
        if cert[0] == 'R':
            if cert[1] != rlp_key(q, st) or not rlp_key_ok(cert[1], duals, q, st):
                return False
            continue
        if cert[0] != 'P' or len(cert[1]) != 30:
            return False
        vec = [Fraction(s) for s in cert[1]]
        a, b, uu, ll = vec[0:5], vec[5:10], vec[10:20], vec[20:30]
        if any(x < 0 for x in uu) or any(x < 0 for x in ll):
            return False
        allowed = set(allowed_sets(q, st))
        for r in range(1, 6):
            for A in itertools.combinations(range(5), r):
                As = set(A)
                if any((ji in As) and (wi not in As) for wi, ji in forced):
                    continue
                base = sum(b[x] for x in A) - sum(uu[pi] for pi, (x, y) in enumerate(pairs) if x in As and y in As) \
                    + sum(ll[pi] for pi, (x, y) in enumerate(pairs) if x in As and y in As)
                for sr in range(0, r + 1):
                    for S in itertools.combinations(A, sr):
                        if sr >= 2 and S not in allowed:
                            continue
                        if base + sum(a[x] for x in S) > 1:
                            return False
        obj = sum(a[x] * Fraction(q[x], 5) for x in range(5)) + sum(b[x] * Fraction(5 - P.al(v, N[x]), 5) for x in range(5))
        for pi, (x, y) in enumerate(pairs):
            lo, hi = LH[(x, y)]
            base = 1 - Fraction(P.al(v, N[x]) + P.al(v, N[y]), 5)
            obj += -uu[pi] * (base + hi) + ll[pi] * (base + lo)
        if obj < 1:
            return False
    return True


def main():
    eng, out = sys.argv[1], sys.argv[2]
    os.mkdir(out)
    inputs = {f: hashlib.sha256(open(os.path.join(eng, f), 'rb').read()).hexdigest()
              for f in ('run.json', 'orbits.jsonl.gz', 'rlp_duals.json', 'survivors.json')}
    run = json.load(open(os.path.join(eng, 'run.json')))
    duals = json.load(open(os.path.join(eng, 'rlp_duals.json')))
    survivors = json.load(open(os.path.join(eng, 'survivors.json')))
    lines = [json.loads(l) for l in gzip.open(os.path.join(eng, 'orbits.jsonl.gz'), 'rt')]
    res = {'inputs_sha256': inputs, 'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
           'survivors_json_empty': survivors == [], 'n_lines': len(lines), 'types': {}, 'rules': {}, 'failures': []}
    bytype = {}
    for ln in lines:
        bytype.setdefault(tuple(ln['type']), []).append(ln)
    rule_ok = {}
    for t in TYPES:
        key = str(t)
        s = run['summary'][key]
        rows = universe(t)
        ints = np.sort(codes_int(rows))
        tr = {'leaves': int(len(ints)), 'leaves_run': s['leaves_labelled'], 'sha_match': None,
              'orbits_lines': len(bytype.get(t, [])), 'orbits_run': s['orbits']}
        tr['sha_match'] = sha_sorted(ints) == s['leafcodes_sha256']
        # orbit coverage
        maps = perm_edge_maps(stabiliser(t))
        reps = bytype.get(t, [])
        R = np.array([[int(ch) - 1 for ch in ln['rep']] for ln in reps], dtype=np.int8)
        imgs = []
        for m in maps:
            img = np.empty_like(R)
            img[:, m] = R
            imgs.append(codes_int(img))
        imgs = np.stack(imgs, axis=1)                      # reps x |stab|
        orbit_sets = [np.unique(row) for row in imgs]
        total = sum(len(o) for o in orbit_sets)
        allimg = np.unique(np.concatenate(orbit_sets)) if orbit_sets else np.array([], dtype=np.int64)
        tr['orbit_images_total'] = int(total)
        tr['orbit_images_distinct'] = int(len(allimg))
        tr['orbits_disjoint'] = bool(total == len(allimg))
        tr['union_equals_universe'] = bool(len(allimg) == len(ints) and np.array_equal(allimg, ints))
        reps_in = np.isin(codes_int(R), ints)
        tr['reps_T_consistent'] = bool(reps_in.all())
        res['types'][key] = tr
        # rule checks
        for ln in reps:
            if time.monotonic() - T0 > BUDGET:
                res['incomplete'] = True
                break
            P = Pat(ln['rep'], t)
            r = ln['rule']
            w = ln.get('witness')
            if r == 'K':
                ok = check_K(P, w)
            elif r == 'RLP':
                ok = check_RLP(P, w, duals)
            elif r == 'N26':
                ok = check_N26(P, w)
            elif r in ('PB', 'Ppair'):
                ok = check_P(P, w, r)
            elif r == 'RPLP':
                ok = check_RPLP(P, w, duals)
            elif r == 'FH5':
                ok = None
            else:
                ok = False
            c = rule_ok.setdefault(r, {'verified': 0, 'failed': 0, 'not_checked_here': 0})
            if ok is None:
                c['not_checked_here'] += 1
            elif ok:
                c['verified'] += 1
            else:
                c['failed'] += 1
                if len(res['failures']) < 50:
                    res['failures'].append({'type': key, 'rep': ln['rep'], 'rule': r, 'witness': w})
        print(json.dumps({key: tr}), flush=True)
    res['rules'] = rule_ok
    res['elapsed_s'] = round(time.monotonic() - T0, 1)
    res['all_types_ok'] = all(v['leaves'] == v['leaves_run'] and v['sha_match'] and v['orbits_disjoint']
                              and v['union_equals_universe'] and v['reps_T_consistent']
                              and v['orbits_lines'] == v['orbits_run'] for v in res['types'].values())
    res['no_survive'] = 'SURVIVE' not in rule_ok and res['survivors_json_empty']
    res['all_checked_rules_ok'] = all(v['failed'] == 0 for v in rule_ok.values())
    with open(os.path.join(out, 'RESULT-v1.json'), 'x') as f:
        json.dump(res, f, indent=1)
        f.write('\n')
    print(json.dumps({k: res[k] for k in ('all_types_ok', 'no_survive', 'all_checked_rules_ok', 'rules', 'elapsed_s')}))


if __name__ == '__main__':
    main()
