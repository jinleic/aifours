#!/usr/bin/env python3
"""Independent sparse exact-arithmetic controls for the frozen f216 review."""
from fractions import Fraction as F
import json
import random


def z(x=0, y=0):
    return (F(x), F(y))

ZERO, ONE, MI = z(), z(1), z(-1)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def conj(x):
    return (x[0], -x[1])


def put(a, key, value):
    value = add(a.get(key, ZERO), value)
    if value == ZERO:
        a.pop(key, None)
    else:
        a[key] = value


def accum(a, b, coefficient=ONE):
    for ij, value in b.items():
        put(a, ij, mul(coefficient, value))
    return a


def ident(n):
    return {(i, i): ONE for i in range(n)}


def outer(v):
    a = {}
    for i, x in v.items():
        for j, y in v.items():
            put(a, (i, j), mul(x, conj(y)))
    return a


def adj(a):
    return {(j, i): conj(x) for (i, j), x in a.items()}


def trans(a):
    return {(j, i): x for (i, j), x in a.items()}


def mm(a, b):
    brows = {}
    for (i, j), v in b.items():
        brows.setdefault(i, []).append((j, v))
    result = {}
    for (i, k), x in a.items():
        for j, y in brows.get(k, ()):
            put(result, (i, j), mul(x, y))
    return result


def swap(d):
    return {(i*d+j, j*d+i): ONE for i in range(d) for j in range(d)}


def pt(a, d, side):
    result = {}
    for (row, col), value in a.items():
        i, j = divmod(row, d)
        h, l = divmod(col, d)
        key = (h*d+j, i*d+l) if side == 'A' else (i*d+l, h*d+j)
        put(result, key, value)
    return result


def vectorize(a, d):
    return {i*d+j: value for (i, j), value in a.items()}


def qform(v, a):
    out = ZERO
    for (i, j), value in a.items():
        if i in v and j in v:
            out = add(out, mul(mul(conj(v[i]), value), v[j]))
    return out


def trace(a):
    out = ZERO
    for (i, j), x in a.items():
        if i == j:
            out = add(out, x)
    return out


def traceprod(a, b):
    out = ZERO
    for (i, j), x in a.items():
        out = add(out, mul(x, b.get((j, i), ZERO)))
    return out


def expected(a, b, label):
    if a != b:
        raise AssertionError(label)


def differing(a, b):
    delta = accum(accum({}, a), b, MI)
    first = min(delta) if delta else None
    return {'nonzero_entries': len(delta), 'first_index': first,
            'first_value_re_im': None if first is None else [str(x) for x in delta[first]]}


def skewput(j, a, b, x):
    if x:
        put(j, (a, b), z(x))
        put(j, (b, a), z(-x))


def canonical_j(d, weights):
    k = len(weights)
    m = 2*k
    j = {}
    defect = []
    for i, (lam, s) in enumerate(weights):
        assert lam*lam+s*s == 1
        skewput(j, 2*i, 2*i+1, lam)
        if s:
            p = m+2*len(defect)
            q = p+1
            assert q < d
            skewput(j, 2*i, p, s)
            skewput(j, 2*i+1, q, -s)
            skewput(j, p, q, lam)
            defect.append((i, p, q))
    for p in range(m+2*len(defect), d, 2):
        skewput(j, p, p+1, 1)
    return j, defect


def build_pair(j, d, k):
    jj = outer(vectorize(j, d))
    f = swap(d)
    r = accum(accum(ident(d*d), f), jj)
    w = accum(accum(accum({}, ident(d*d), z(k)), f, z(-k)), jj, MI)
    return r, w


def verify_source(j, d, k):
    expected(mm(j, adj(j)), ident(d), 'J unitary')
    expected(trans(j), accum({}, j, MI), 'J skew')
    r, w = build_pair(j, d, k)
    f = swap(d)
    sym = {}
    for i in range(d):
        accum(sym, outer({i*d+i: ONE}), z(2))
        for h in range(i+1, d):
            accum(sym, outer({i*d+h: ONE, h*d+i: ONE}))
    expected(sym, accum(ident(d*d), f), 'symmetric PSD sum')
    expected(r, accum(dict(sym), outer(vectorize(j, d))), 'R PSD sum')
    bj = {(i, h): conj(v) for (i, h), v in j.items()}
    v = {}
    for i in range(d):
        for (b, c), x in bj.items():
            put(v, (i*d+b, i*d+c), x)
    expected(mm(v, adj(v)), ident(d*d), 'twist unitary')
    omega = {i*d+i: ONE for i in range(d)}
    rhs = accum(accum(ident(d*d), outer(omega)), mm(mm(v, f), adj(v)))
    expected(pt(r, d, 'B'), rhs, 'Bob PPT orientation')
    expected(pt(r, d, 'B'), accum(mm(mm(v, sym), adj(v)), outer(omega)), 'PPT PSD sum')
    expected(pt(r, d, 'A'), trans(pt(r, d, 'B')), 'both PPT orientations')
    expected(trace(r), z(d*(d+2)), 'trace R')
    expected(traceprod(w, r), z(d*(2*k-d)), 'negative pairing')
    return r, w


def compression_decomposition(j, d, weights, defect):
    k, m = len(weights), 2*len(weights)
    r, wfull = build_pair(j, d, k)
    del r
    w = {(a, b): v for (a, b), v in wfull.items() if a < m*d and b < m*d}
    je = {a*d+b: v for (a, b), v in j.items() if a < m}
    fe = {(a*d+b, b*d+a): ONE for a in range(m) for b in range(m)}
    direct = accum(accum(accum({}, ident(m*d), z(k)), fe, z(-k)), outer(je), MI)
    expected(w, direct, 'actual compressed swap/vector')
    u, weights_u = [], []
    for i, (lam, _) in enumerate(weights):
        u.append({(2*i)*d+2*i+1: ONE, (2*i+1)*d+2*i: MI})
        weights_u.append(lam)
    for i, p, q in defect:
        u.append({(2*i)*d+p: ONE, (2*i+1)*d+q: MI})
        weights_u.append(weights[i][1])
    assert sum(x*x for x in weights_u) == k
    pmat, qmat = {}, {}
    pair_vectors = []
    for a in range(len(u)):
        for b in range(a+1, len(u)):
            x = {}
            for index, val in u[b].items():
                put(x, index, mul(z(weights_u[a]), val))
            for index, val in u[a].items():
                put(x, index, mul(z(-weights_u[b]), val))
            pair_vectors.append(x)
            accum(pmat, outer(x))
    for a in range(m):
        for b in range(a+1, m):
            if a % 2 == 0 and b == a+1:
                continue
            accum(pmat, outer({a*d+b: ONE, b*d+a: MI}), z(k))
    for a in range(m):
        for o in range(m, d):
            if any(a in (2*i, 2*i+1) and o in (p, q) for i, p, q in defect):
                continue
            accum(pmat, outer({a*d+o: ONE}), z(k))
    for i, p, q in defect:
        h = {(2*i)*d+q: ONE, (2*i+1)*d+p: ONE}
        accum(qmat, outer(h), z(k))
    expected(accum(dict(pmat), pt(qmat, d, 'A')), w, 'compressed P+Q^Gamma_A')
    return w, pmat, qmat, pair_vectors


def phases_matrix(a, rowphases):
    return {(i, h): mul(mul(rowphases[i], value), conj(rowphases[h]))
            for (i, h), value in a.items()}


def complex_congruence(j, phases):
    return {(i, h): mul(mul(phases[i], value), phases[h]) for (i, h), value in j.items()}


def show(q):
    return [str(q[0]), str(q[1])]


def main():
    results = []
    cases = [
        (4, [(F(0), F(1))]),
        (6, [(F(3,5), F(4,5)), (F(1), F(0))]),
        (6, [(F(1), F(0)), (F(1), F(0))]),
        (8, [(F(3,5), F(4,5)), (F(5,13), F(12,13))]),
        (8, [(F(1), F(0)), (F(0), F(1)), (F(1), F(0))]),
        (10, [(F(3,5), F(4,5)), (F(5,13), F(12,13)), (F(1), F(0))]),
        (12, [(F(3,5), F(4,5)), (F(5,13), F(12,13)), (F(8,17), F(15,17))]),
    ]
    complex_negative = None
    missing_negative = None
    for d, weights in cases:
        k, m = len(weights), 2*len(weights)
        j, defect = canonical_j(d, weights)
        verify_source(j, d, k)
        c, pmat, qmat, pair_vectors = compression_decomposition(j, d, weights, defect)
        phases = [ONE]*d
        phases[1] = z(0, 1)
        j_complex = complex_congruence(j, phases)
        verify_source(j_complex, d, k)
        _, w_complex = build_pair(j_complex, d, k)
        compressed_complex = {(a,b): v for (a,b), v in w_complex.items() if a < m*d and b < m*d}
        phase_p = [mul(phases[a], phases[b]) for a in range(m) for b in range(d)]
        phase_q = [mul(conj(phases[a]), phases[b]) for a in range(m) for b in range(d)]
        pc, qc = phases_matrix(pmat, phase_p), phases_matrix(qmat, phase_q)
        expected(phases_matrix(c, phase_p), compressed_complex, 'complex compressed covariance')
        expected(accum(dict(pc), pt(qc, d, 'A')), compressed_complex, 'complex decomposition')
        if d == 6 and len(defect) == 1:
            wrong_pt = accum(dict(pc), pt(qc, d, 'B'))
            wrong_pt_diff = differing(wrong_pt, compressed_complex)
            assert wrong_pt_diff['nonzero_entries']
            badp = accum(dict(pmat), outer(pair_vectors[0]), MI)
            missing_negative = differing(accum(badp, pt(qmat, d, 'A')), c)
            assert missing_negative['nonzero_entries']
            f = swap(d)
            vbad = {}
            for a in range(d):
                for (b, h), value in j_complex.items():
                    put(vbad, (a*d+b, a*d+h), value)
            omega = {a*d+a: ONE for a in range(d)}
            rcomplex, _ = build_pair(j_complex, d, k)
            wrong_source = accum(accum(ident(d*d), outer(omega)), mm(mm(vbad, f), adj(vbad)))
            wrong_source_diff = differing(wrong_source, pt(rcomplex, d, 'B'))
            assert wrong_source_diff['nonzero_entries']
            complex_negative = {'wrong_compressed_PT_side': wrong_pt_diff,
                                'wrong_twist_J_instead_of_conjugate_J': wrong_source_diff}
        results.append({'d': d, 'k': k, 'defect_pairs': len(defect),
                        'lambda_s': [[str(a), str(b)] for a,b in weights],
                        'real_and_complex_exact_equalities': 'PASS'})

    # Original d=6 choice J0 = [[0,I],[-I,0]], including a rational 4-plane.
    d, k = 6, 2
    j0 = {}
    for a in range(3):
        skewput(j0, a, a+3, 1)
    r0, w0 = verify_source(j0, d, k)
    e0 = [(0, ONE)]
    columns = [e0, [(3,z(F(3,5))), (1,z(F(4,5)))], [(2,ONE)], [(5,ONE)],
               [(3,z(F(4,5))), (1,z(F(-3,5)))], [(4,MI)]]
    o = {}
    for col, entries in enumerate(columns):
        for row, value in entries:
            put(o, (row, col), value)
    expected(mm(adj(o), o), ident(d), 'rational full basis orthogonal')
    jrot = mm(mm(trans(o), j0), o)
    jc, _ = canonical_j(6, cases[1][1])
    expected(jrot, jc, 'actual J0 rational compressed canonical form')
    y2 = {0*d+3: ONE, 1*d+4: ONE}
    y3 = dict(y2)
    y3[2*d+5] = ONE
    expected(qform(y2, w0), ZERO, 'rank-two saturation')
    expected(qform(y3, w0), z(-3), 'rank-three negative')
    rng = random.Random(216)
    values = []
    for _ in range(40):
        left = [[rng.randrange(-3,4) for _ in range(d)] for _ in range(2)]
        right = [[rng.randrange(-3,4) for _ in range(d)] for _ in range(2)]
        y = {}
        for a in range(d):
            for b in range(d):
                val = sum(left[t][a]*right[t][b] for t in range(2))
                if val:
                    y[a*d+b] = z(val)
        q = qform(y, w0)
        assert q[1] == 0 and q[0] >= 0
        values.append(q[0])
    rho_bad = outer(y3)
    vneg = {0*d+4: ONE, 1*d+3: MI}
    expected(qform(vneg, pt(rho_bad, d, 'B')), z(-2), 'non-PPT source negative direction')
    filtered_w = {(a,b): v for (a,b), v in w0.items() if a//d < 4 and b//d < 4}
    expected(qform(y3, filtered_w), z(-3), 'rank-four filter with non-PPT source')
    print(json.dumps({'cases': results,
                      'original_d6': {'trace_R': show(trace(r0)),
                                      'trace_WR': show(traceprod(w0,r0)),
                                      'rank2_saturation': show(qform(y2,w0)),
                                      'rank3_negative': show(qform(y3,w0)),
                                      'rank2_random_samples': len(values),
                                      'rank2_sample_min': str(min(values)),
                                      'rational_4plane_canonical_congruence': 'PASS'},
                      'intended_reason_negatives': {
                          'dropped_SOS_pair': missing_negative,
                          **complex_negative,
                          'nonPPT_rank4_filter_pairing': show(qform(y3, filtered_w)),
                          'nonPPT_partial_transpose_direction': show(qform(vneg, pt(rho_bad,d,'B')))
                      }}, indent=2))


if __name__ == '__main__':
    main()
