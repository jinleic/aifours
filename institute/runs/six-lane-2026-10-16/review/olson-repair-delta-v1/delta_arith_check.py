#!/usr/bin/env python3
"""olson-repair-delta-v1 own arithmetic checks (delegated parent delta desk OlsonRepairDeltaDesk).
Own code only: no lane module is imported or executed; lane receipts are only parsed as JSON text.
Writes ONLY olson-repair-delta-v1/arith-check.json (exclusive create).  <=1 CPU, small memory.
"""
import json, hashlib, collections, time, pathlib, sys
HERE = pathlib.Path(__file__).resolve().parent
LANE = pathlib.Path('/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/olson/inverse-run-count/mixdef-high/c6')
t0 = time.time()
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def cdiv(a, b): return -((-a) // b)
def my_classes(p):
    """Own enumeration from the written setting of proof-SEEDG-r2.md Sec.0: k>=p+1, 1<=B<=kappa-1, k>=2kappa+3,
    E=R-k>=0 (even), R=2p-k+2kappa<=2p-3, B<=A=R-B<=2p-1."""
    out = []
    for k in range(p + 1, 3 * p):
        for kappa in range(2, k):
            R = 2 * p - k + 2 * kappa; E = R - k
            if E < 0 or k < 2 * kappa + 3 or R > 2 * p - 3: continue
            for B in range(1, kappa):
                if B <= R - B <= 2 * p - 1: out.append((k, kappa, B))
    return out
def A2(D, E, R, d):  # doubled eight L_A expressions, order of star r0/r1 definitions
    mn, mx = min(d, 0), max(d, 0)
    return [2*D+2*E+4, 2*D+E+2-2*mn, D+E+4, 2*D+E-2*mn, 2*D+2*E-2*d+2, D+E-d-mn+3, D+E+3-2*d+mx, R-d+2]
def B2(D, E, R, d):
    mn, mx = min(d, 0), max(d, 0)
    return [2*D+2*E+4, 2*D+E+2*mx, D+E+4, 2*D+E+2*mx+2, 2*D+2*E+2*d+2, D+E+mx+d+3, D+E+3+2*d-mn, R+d+2]
def sw(v): return [v[0], v[3], v[2], v[1]] + v[4:]
def lf_check(tuples):
    st = collections.Counter(); mins = {}
    for (D, E, kappa, B, d) in tuples:
        R = D + E + 2 * kappa
        a8, b8 = A2(D, E, R, d), B2(D, E, R, d); LA2, LB2 = min(a8), min(b8)
        st['tuples'] += 1
        if LA2 != D + E + 3 - max(d, -1) or LB2 != D + E + 3 + min(d, 1) or LB2 != min(A2(D, E, R, -d)): st['closed_form_mismatch'] += 1
        if d >= 1:
            u = d; C2 = D + E - u + 3; T2 = D + E + 4
            vA = [D+E+u+1, D+u-1, u+1, D+u-3, D+E-u-1, 0, 0, 2*kappa-1]
            vB = [D+E, D+2*u-4, 0, D+2*u-2, D+E+2*u-2, 2*u-1, 2*u-1, 2*kappa+u-2]
            if [x - C2 for x in a8] != vA or [x - T2 for x in b8] != vB or min(vA) < 0 or min(vB) < 0: st['vector_mismatch'] += 1
            if 2 * (D + E - u + 1) - C2 <= 0: st['r0_extra_term_attains'] += 1
        elif d == 0:
            vA0 = [D+E+1, D-1, 1, D-3, D+E-1, 0, 0, 2*kappa-1]
            if [x - (D+E+3) for x in a8] != vA0 or [x - (D+E+3) for x in b8] != sw(vA0): st['vector_mismatch'] += 1
        else:
            if a8 != sw(B2(D, E, R, -d)) or b8 != sw(A2(D, E, R, -d)): st['reflection_mismatch'] += 1
        gA2, gB2 = LA2 - (D - d), LB2 - (D + d)          # doubled real gaps
        mins['real_gap_doubled'] = min(mins.get('real_gap_doubled', 99), gA2, gB2)
        if min(gA2, gB2) < 3: st['real_gap_below_3_2'] += 1
        near2, far2 = E + 3, E - abs(d) + 4                # star-r1 LF 44 literal reading
        if d > 0: ok = (gA2, gB2) == (near2, far2)
        elif d < 0: ok = (gA2, gB2) == (far2, near2)
        else: ok = sorted([gA2, gB2]) == sorted([near2, far2])
        if not ok: st['lf44_near_far_literal_mismatch_d%s' % ('0' if d == 0 else '!=0')] += 1
        loQS, hiQS = cdiv(d - D, 2) + 1, (d + D) // 2 - 1
        lo_s, hi_s = 1 - cdiv(LA2, 2), cdiv(LB2, 2) - 1
        h, eps = E // 2, D % 2
        J = lambda uu: h + 2 - (uu - eps) // 2
        exp = (h + 2, J(d)) if d > 0 else ((h + 2, h + 2) if d == 0 else (J(-d), h + 2))
        got = (loQS - lo_s, hi_s - hiQS)
        if got != exp: st['integer_relaxation_formula_mismatch'] += 1
        mins['integer_gain'] = min(mins.get('integer_gain', 99), *got)
        if min(got) < 2: st['integer_gain_below_2'] += 1
    return dict(st), mins
res = {}
abstract = ((D, E, kap, B, d) for D in range(3, 41) for E in range(0, 41, 2) for kap in range(2, 16)
            for B in range(1, kap) for d in range(-min(B, E + 1), E + 2))
res['LF_abstract_domain'] = dict(zip(('counts', 'minima'), lf_check(abstract)),
                                 domain='D=Delta0 in 3..40, E even 0..40, kappa 2..15, 1<=B<=kappa-1, -min(B,E+1)<=d<=E+1')
PR61 = [q for q in range(5, 62) if isprime(q)]
CL = {p: my_classes(p) for p in PR61}
res['class_counts_p5_61'] = {p: len(CL[p]) for p in PR61}
def class_tuples():
    for p in PR61:
        for (k, kap, B) in CL[p]:
            R = 2*p - k + 2*kap; E = R - k; D = 2*p - R
            for d in range(-min(B, E + 1), E + 2): yield (D, E, kap, B, d)
res['LF_class_domain_p5_61'] = dict(zip(('counts', 'minima'), lf_check(class_tuples())))
p = 2**61 - 1; D = 2**60 + 200; kap = p - D; k = p + kap; R = 2*p - k + 2*kap; E = R - k
res['codex_large_case'] = {'E': E, 'Delta0_ok': D == 2*p - R, 'ceil_LA': str(cdiv(min(A2(D, E, R, 1)), 2)), 'ceil_LB': str(cdiv(min(B2(D, E, R, 1)), 2)),
                           'equals_2^59+101_and_+102': (cdiv(min(A2(D, E, R, 1)), 2), cdiv(min(B2(D, E, R, 1)), 2)) == (2**59 + 101, 2**59 + 102)}
def term_check(primes, slack):
    st = collections.Counter()
    for p in primes:
        for (k, kap, B) in CL[p]:
            R = 2*p - k + 2*kap; E = R - k; D = 2*p - R; A = R - B; kB = kap - B
            lam = lambda y, m: min(p - m + 1, y + m - kB, (y + B) // 2 + 1)
            lamc = lambda y, m: min(p - m + 1, A - kap - y + m, (A - y) // 2 + 1)
            for d in range(-min(B, E + 1) - slack, E + 2 + slack):
                indom = -min(B, E + 1) <= d <= E + 1
                mn, mx = min(d, 0), max(d, 0)
                bA = {(1,1): 2*D+2*E+4, (1,2): 2*D+E+2-2*mn, (1,3): D+E+4, (2,1): 2*D+E-2*mn, (2,2): 2*D+2*E-2*d+2,
                      (2,3): D+E-d-mn+3, (3,1): D+E+4, (3,2): D+E+3-2*d+mx, (3,3): R-d+2}
                bB = {(1,1): 2*D+2*E+4, (1,2): 2*D+E+2*mx, (1,3): D+E+4, (2,1): 2*D+E+2*mx+2, (2,2): 2*D+2*E+2*d+2,
                      (2,3): D+E+mx+d+3, (3,1): D+E+4, (3,2): D+E+3+2*d-mn, (3,3): R+d+2}
                LA2, LB2 = min(bA.values()), min(bB.values())
                for yp in range(-B - mn, A - mx + 1):
                    y = yp + d
                    if not (-B + mx <= y <= A + mn): continue           # (2.1)
                    for m in range(1, k // 2 + 1):                      # (F1): 2m <= k
                        for mp in (m - 1, m):                           # m-1 <= m' <= m, m' >= 1
                            if mp < 1: continue
                            U = (p - mp + 1, yp + mp - kB, (yp + B) // 2 + 1); T = (p - m + 1, A - kap - y + m, (A - y) // 2 + 1)
                            V = (p - m + 1, y + m - kB, (y + B) // 2 + 1); S = (p - mp + 1, A - kap - yp + mp, (A - yp) // 2 + 1)
                            st['domain_tuples' if indom else 'out_of_0.2prime_tuples'] += 1
                            if any(2 * (U[i-1] + T[j-1]) < bA[(i, j)] or 2 * (V[i-1] + S[j-1]) < bB[(i, j)] for i in (1, 2, 3) for j in (1, 2, 3)):
                                st['term_bound_fail_' + ('in' if indom else 'out')] += 1
                            if not indom: continue
                            sA, sB = lam(yp, mp) + lamc(y, m), lam(y, m) + lamc(yp, mp)
                            if sA != min(U) + min(T) or sB != min(V) + min(S): st['min_sum_identity_fail'] += 1
                            if 2 * sA < LA2 or 2 * sB < LB2: st['sum_below_L'] += 1
                            if any(2 * sA < v for v in bA.values()) or any(2 * sB < v for v in bB.values()): st['r0_each_wording_false'] += 1
    return dict(st)
res['term_bounds_p5_23_slack3'] = term_check([5, 7, 11, 13, 17, 19, 23], 3)
def qq_check(primes):
    st = collections.Counter()
    for p in primes:
        for (k, kap, B) in CL[p]:
            R = 2*p - k + 2*kap; E = R - k; D = 2*p - R; A = R - B; kB = kap - B
            lam = lambda y, m: min(p - m + 1, y + m - kB, (y + B) // 2 + 1)
            lamc = lambda y, m: min(p - m + 1, A - kap - y + m, (A - y) // 2 + 1)
            win = {}
            for d in range(-min(B, E + 1), E + 2):
                a = max(lam(d, 1), cdiv(d - D, 2) + 1); b = min(p - lamc(d, 1), (d + D) // 2 - 1)
                if a <= b: win[d] = (a, b)
            e = lambda d: abs(d) - 1 if d else 1
            ws = sorted(win)
            for i, d1 in enumerate(ws):
                for d2 in ws[i:]:
                    if e(d1) + e(d2) > E: continue
                    (a1, b1), (a2, b2) = win[d1], win[d2]; y = d1 + d2
                    for m in (1, 2):
                        st['pair_m_cases'] += 1
                        if d1 == d2: st['equal_weight_cases'] += 1
                        if y < -B: st['y_below_minus_B_cases'] += 1
                        if a1 + a2 < 1 - lamc(y, m) or b1 + b2 > p + lam(y, m) - 1: st['P2_fail'] += 1
    return dict(st)
res['extended_QQ_formal_pairs_p5_61'] = qq_check(PR61)
p0 = collections.Counter()
for p in PR61:
    for (k, kap, B) in CL[p]:
        R = 2*p - k + 2*kap; E = R - k; A = R - B; kB = kap - B
        for d in range(-min(B, E + 1), E + 2):
            p0['cases'] += 1
            if min(p, d + 1 - kB, (d + B) // 2 + 1) + min(p, A - kap - d + 1, (A - d) // 2 + 1) < 1: p0['fail'] += 1
res['P0_automatic_PIN_p5_61'] = dict(p0)
res['small_domain_weight_count_p11_43'] = sum(2*p - 2*k + 2*kap + 2 + min(B, 2*p - 2*k + 2*kap + 1)
                                             for p in PR61 if 11 <= p <= 43 for (k, kap, B) in CL[p])
res['max_E_p5_p7'] = {p: max(2*p - 2*k + 2*kap for (k, kap, B) in CL[p]) for p in (5, 7)}
sf = collections.Counter()
for B in range(1, 30):
    for kB in range(1, 30):
        for k in range(kB + 3*B, kB + 3*B + 6):
            for npr in range(0, B + 1):
                for nan in range(0, B - npr + 1):
                    sf['cases'] += 1
                    if not (2*(k - kB - 2*B) + npr > B + nan - 2): sf['violations'] += 1
res['C0WB_sufficient_family_algebra'] = dict(sf)
p, k, kap, B = 17, 21, 7, 4; kB = kap - B
runs = [2]*6 + [1]*11 + [-1]*4; x = [2]*6 + [1]*11 + [-2, -2, -1, -1]
Z = [i for i in range(len(runs)) if 2*x[i] - runs[i] <= 0]
res['codex_caseB_relaxed_example_17_21_7_4'] = {'legal_class': (k, kap, B) in CL[17], 'E': 2*p - 2*k + 2*kap, 'sum_x': sum(x),
    'singletons_ok': all(x[i] >= min(p, runs[i] + 1 - kB, (runs[i] + B)//2 + 1) for i in range(len(runs))),
    'Z': Z, 'Phi_Z': sum(runs[i] - x[i] for i in Z) + 1, 'kB': kB, 'n_ev_al': sum(1 for d in runs if d > 0 and d % 2 == 0),
    'note': 'relaxed singleton+sum data only; Phi(Z)<=kB is Case-B arithmetic; not a (0.2) solution or group counterexample'}
OUTD = LANE / 'out'
def parse(name):
    cls, cnt = {}, {}
    for line in (OUTD / name).read_text().split('\n'):
        if not line.startswith('{'): continue
        o = json.loads(line)
        if 'class' in o: cls[tuple(o['class'])] = o
        elif 'counts' in o: cnt[o['p']] = o['counts']
    return cls, cnt
X3, X3n = parse('revision_X3p23.txt'); S0, S0n = parse('revision_star3mode0.txt'); S1, S1n = parse('revision_star3mode1.txt')
S3, _ = parse('revision_star3mode3.txt'); T2, _ = parse('revision_star3tight2.txt'); T4, _ = parse('revision_star3tight4.txt')
_, H0 = parse('seedXstar2_mode0.txt'); _, HX = parse('seedX2_mode0.txt'); _, H1 = parse('seedXstar2_mode1.txt')
def changes(new, old):
    c = collections.Counter()
    for kk, v in new.items():
        if old[kk]['verdict'] != v['verdict']: c['%s:%s->%s' % (old[kk]['label'], old[kk]['verdict'], v['verdict'])] += 1
    return dict(c)
res['receipt_reconciliation'] = {
    'receipt_sha256': {n: hashlib.sha256((OUTD / n).read_bytes()).hexdigest() for n in ('revision_X3p23.txt', 'revision_star3mode0.txt',
        'revision_star3mode1.txt', 'revision_star3mode3.txt', 'revision_star3tight2.txt', 'revision_star3tight4.txt',
        'seedXstar2_mode0.txt', 'seedX2_mode0.txt', 'seedXstar2_mode1.txt')},
    'own_class_ids_equal_X3_ids_p11_23': {(q,) + c for q in (11, 13, 17, 19, 23) for c in CL[q]} == set(X3),
    'own_class_ids_equal_star3mode0_ids_p11_31': {(q,) + c for q in (11, 13, 17, 19, 23, 29, 31) for c in CL[q]} == set(S0),
    'mode1_vs_X3_classes': len(X3), 'mode1_vs_X3_verdict_or_label_mismatches': sum(1 for kk in X3 if kk not in S1 or S1[kk]['verdict'] != X3[kk]['verdict'] or S1[kk]['label'] != X3[kk]['label']),
    'star3mode0_counts_equal_seedXstar2_mode0': all(S0n[q] == H0[q] for q in H0),
    'X3_counts_equal_seedX2_mode0_p11_23': all(X3n[q] == HX[q] for q in X3n),
    'star3mode1_counts_equal_seedXstar2_mode1': all(S1n[q] == H1[q] for q in H1),
    'mode0_failures': len([v for v in S0.values() if v['verdict'] == 'fail']),
    'mode0_failure_stages': dict(collections.Counter(v['stage'] for v in S0.values() if v['verdict'] == 'fail')),
    'mode0_failure_labels': dict(collections.Counter(v['label'] for v in S0.values() if v['verdict'] == 'fail')),
    'mode0_OPENE_failure': [v for v in S0.values() if v['verdict'] == 'fail' and v['label'] == 'OPENE'],
    'mode3_failures': len([v for v in S3.values() if v['verdict'] == 'fail']),
    'mode3_failure_stages': dict(collections.Counter(v['stage'] for v in S3.values() if v['verdict'] == 'fail')),
    'mode3_changes_vs_mode0': changes(S3, S0), 'tight2_changes_vs_mode0': changes(T2, S0), 'tight4_changes_vs_mode0': changes(T4, S0),
    'OPEN0_pass_classes_mode0': [list(kk) + [('RA2' if (kk[3] == 2 and kk[2] - kk[3] == kk[0] - 5) else 'other')] for kk, v in sorted(S0.items()) if v['label'] == 'OPEN0' and v['verdict'] == 'pass'],
}
rp = {}
for n in ('replayW_mut0', 'replayW_mut1', 'replayW_mut2', 'replayW_mut3', 'replayW2_mut0', 'replayW2_mut1'):
    for line in (OUTD / (n + '.txt')).read_text().split('\n'):
        if line.startswith('{'): rp[n] = json.loads(line)
res['replay_receipts'] = rp
res['seconds'] = round(time.time() - t0, 1)
res['python'] = sys.version.split()[0]
res['script_sha256'] = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
with open(HERE / 'arith-check.json', 'x') as f:
    json.dump(res, f, indent=1, default=str); f.write('\n')
print(json.dumps({'seconds': res['seconds'], 'wrote': str(HERE / 'arith-check.json')}))
