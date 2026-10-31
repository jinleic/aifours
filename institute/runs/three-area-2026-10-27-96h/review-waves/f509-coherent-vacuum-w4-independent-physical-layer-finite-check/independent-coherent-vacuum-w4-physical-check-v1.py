from fractions import Fraction as F
from itertools import combinations
import math
import time

START = time.monotonic()
LIMIT = 50.0
TOL = 2e-10

class CheckFailure(Exception):
    pass

class Deadline(Exception):
    pass

def tick():
    if time.monotonic() - START >= LIMIT:
        raise Deadline("cooperative 50-second deadline")

def must(condition, reason):
    if not condition:
        raise CheckFailure(reason)

def G(a=0, b=0):
    return (F(a), F(b))

Z, O = G(), G(1)

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def neg(a):
    return (-a[0], -a[1])

def sub(a, b):
    return add(a, neg(b))

def cj(a):
    return (a[0], -a[1])

def scale(a, c):
    return (a[0] * c, a[1] * c)

def mul(a, b):
    if not a[1] and not b[1]:
        return (a[0] * b[0], F(0))
    return (a[0]*b[0] - a[1]*b[1],
            a[0]*b[1] + a[1]*b[0])

def inv(a):
    d = a[0]*a[0] + a[1]*a[1]
    must(bool(d), "division by zero")
    return (a[0]/d, -a[1]/d)

def zero(n, m=None):
    return [[Z for _ in range(n if m is None else m)] for _ in range(n)]

def eye(n):
    a = zero(n)
    for i in range(n):
        a[i][i] = O
    return a

def adj(a):
    return [[cj(a[i][j]) for i in range(len(a))]
            for j in range(len(a[0]))]

def trans(a):
    return [list(row) for row in zip(*a)]

def mm(a, b):
    must(len(a[0]) == len(b), "matrix dimensions")
    out = zero(len(a), len(b[0]))
    for i, row in enumerate(a):
        tick()
        for k, x in enumerate(row):
            if x == Z:
                continue
            for j, y in enumerate(b[k]):
                if y != Z:
                    out[i][j] = add(out[i][j], mul(x, y))
    return out

def lin(terms):
    n = len(terms[0][1])
    out = zero(n, len(terms[0][1][0]))
    for c, a in terms:
        if not c:
            continue
        for i in range(n):
            tick()
            for j in range(len(a[0])):
                out[i][j] = add(out[i][j], scale(a[i][j], c))
    return out

def tr(a):
    value = Z
    for i in range(len(a)):
        value = add(value, a[i][i])
    must(value[1] == 0, "nonreal trace")
    return value[0]

def trprod(a, b):
    value = Z
    for i in range(len(a)):
        for j in range(len(a)):
            value = add(value, mul(a[i][j], b[j][i]))
    must(value[1] == 0, "nonreal Hermitian pairing")
    return value[0]

def outer(v):
    return [[mul(x, cj(y)) for y in v] for x in v]

def rank(a):
    a = [row[:] for row in a]
    row = 0
    for col in range(len(a[0])):
        tick()
        pivot = next((i for i in range(row, len(a))
                      if a[i][col] != Z), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        divisor = inv(a[row][col])
        a[row] = [mul(x, divisor) for x in a[row]]
        for i in range(row + 1, len(a)):
            c = a[i][col]
            if c != Z:
                a[i] = [sub(x, mul(c, y))
                        for x, y in zip(a[i], a[row])]
        row += 1
        if row == len(a):
            break
    return row

def psd(a):
    must(a == adj(a), "Hermiticity")
    a = [row[:] for row in a]
    for i in range(len(a)):
        tick()
        d = a[i][i]
        must(d[1] == 0 and d[0] >= 0, "PSD negative pivot")
        if not d[0]:
            must(all(a[i][j] == Z for j in range(i + 1, len(a))),
                 "PSD zero-pivot row")
            continue
        for j in range(i + 1, len(a)):
            for k in range(j, len(a)):
                correction = scale(mul(a[j][i], a[i][k]), 1/d[0])
                a[j][k] = sub(a[j][k], correction)
                a[k][j] = cj(a[j][k])

def pack(index, sites):
    value = 0
    for site in sites:
        value = 2*value + ((index >> (3-site)) & 1)
    return value

def partial(rho, sites):
    other = tuple(i for i in range(4) if i not in sites)
    out = zero(1 << len(sites))
    for a in range(16):
        tick()
        for b in range(16):
            if pack(a, other) == pack(b, other):
                i, j = pack(a, sites), pack(b, sites)
                out[i][j] = add(out[i][j], rho[a][b])
    return out

def embed(marginal, sites):
    other = tuple(i for i in range(4) if i not in sites)
    out = zero(16)
    for a in range(16):
        for b in range(16):
            if pack(a, other) == pack(b, other):
                out[a][b] = marginal[pack(a, sites)][pack(b, sites)]
    return out

def layers(rho):
    return {m: lin([(F(1), embed(partial(rho, s), s))
                    for s in combinations(range(4), m)])
            for m in (1, 2, 3)}

def kron(a, b):
    out = zero(len(a)*len(b), len(a[0])*len(b[0]))
    for i in range(len(a)):
        for j in range(len(a[0])):
            for k in range(len(b)):
                for l in range(len(b[0])):
                    out[i*len(b)+k][j*len(b[0])+l] = mul(a[i][j], b[k][l])
    return out

def tensor(factors):
    out = [[O]]
    for a in factors:
        out = kron(out, a)
    return out

def local_unitary():
    c, s = F(3, 5), F(4, 5)
    return tensor([
        [[G(c), G(0, s)], [G(0, s), G(c)]],
        [[O, Z], [Z, G(0, 1)]],
        [[G(c), G(-s)], [G(s), G(c)]],
        [[Z, O], [G(0, 1), Z]],
    ])

def conjugate(u, a):
    return mm(mm(u, a), adj(u))

def erasure(rho, h, p):
    s, b = 1-p, p/2
    return lin([(s**4, rho), (s**3*b, h[3]),
                (s**2*b**2, h[2]), (s*b**3, h[1]),
                (b**4, eye(16))])

def pauli_channel(rho, p):
    out = [row[:] for row in rho]
    weights = [1-3*p/4, p/4, p/4, p/4]
    must(all(w >= 0 for w in weights), "physical Pauli weights")
    for site in range(4):
        tick()
        mask = 1 << (3-site)
        nxt = zero(16)
        for kind, weight in enumerate(weights):
            if not weight:
                continue
            for a in range(16):
                ba = bool(a & mask)
                ia = a ^ mask if kind in (1, 2) else a
                phase_a = G(0, -1 if ba else 1) if kind == 2 else (
                    G(-1 if ba else 1) if kind == 3 else O)
                for b in range(16):
                    if out[a][b] == Z:
                        continue
                    bb = bool(b & mask)
                    ib = b ^ mask if kind in (1, 2) else b
                    phase_b = G(0, -1 if bb else 1) if kind == 2 else (
                        G(-1 if bb else 1) if kind == 3 else O)
                    value = mul(mul(phase_a, out[a][b]), cj(phase_b))
                    nxt[ia][ib] = add(nxt[ia][ib], scale(value, weight))
        out = nxt
    return out

def conjugate_w(a):
    return [[scale(a[15-i][15-j],
                   -1 if (i.bit_count()+j.bit_count()) % 2 else 1)
             for j in range(16)] for i in range(16)]

def spin(a):
    return conjugate_w(trans(a))

def partial_transpose(a, site):
    mask = 1 << (3-site)
    out = zero(16)
    for i in range(16):
        for j in range(16):
            ii = (i & ~mask) | (j & mask)
            jj = (j & ~mask) | (i & mask)
            out[ii][jj] = a[i][j]
    return out

def padd(a, b):
    out = [F(0)] * max(len(a), len(b))
    for i, c in enumerate(a):
        out[i] += c
    for i, c in enumerate(b):
        out[i] += c
    return out

def pmul(a, b):
    out = [F(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out

def product_polys(polys):
    out = [F(1)]
    for p in polys:
        out = pmul(out, p)
    return out

def tri_poly(diagonal, adjacent_products):
    previous, current = [F(1)], [-diagonal[0], F(1)]
    for i in range(1, len(diagonal)):
        nxt = padd(pmul([-diagonal[i], F(1)], current),
                   [-adjacent_products[i-1]*c for c in previous])
        previous, current = current, nxt
    return current

def leading_dets(diagonal, adjacent_products):
    before, current = F(1), diagonal[0]
    out = [current]
    for i in range(1, len(diagonal)):
        nxt = diagonal[i]*current-adjacent_products[i-1]*before
        before, current = current, nxt
        out.append(current)
    return out

def blocks(matrices):
    n = sum(len(a) for a in matrices)
    out, offset = zero(n), 0
    for a in matrices:
        for i in range(len(a)):
            for j in range(len(a)):
                out[offset+i][offset+j] = a[i][j]
        offset += len(a)
    return out

def extend(a, n):
    out = zero(n)
    for i in range(len(a)):
        for j in range(len(a)):
            out[i][j] = G(a[i][j])
    return out

def invariant_basis():
    columns = []
    for weight in range(5):
        columns.append([G(int(i.bit_count() == weight)) for i in range(16)])
    for f in ((1,-1,0,0), (1,0,-1,0), (1,0,0,-1)):
        for weight in (1,2,3):
            v = [Z]*16
            for sites in combinations(range(4), weight):
                index = sum(1 << (3-i) for i in sites)
                v[index] = G(sum(f[i] for i in sites))
            columns.append(v)
    pairs = list(combinations(range(4), 2))
    for coefficients in ((1,0,-1,-1,0,1), (0,1,-1,-1,1,0)):
        v = [Z]*16
        for sites, c in zip(pairs, coefficients):
            v[sum(1 << (3-i) for i in sites)] = G(c)
        columns.append(v)
    out = [list(row) for row in zip(*columns)]
    must(rank(out) == 16, "invariant basis rank")
    return out

def representations(r, u):
    a3 = [[4-3*r, 6*u, 0],
          [3*u/2, 1+3*r/2, 3*u/2],
          [0, u, 3*r/2]]
    b2 = [[1-r/2, u], [u/2, r/2]]
    a4 = [[6-3*r, 6*u, 0, 0],
          [3*u/2, 3, 3*u, 0],
          [0, 2*u, 1+3*r/2, u],
          [0, 0, 3*u/2, 3*r/2]]
    b3 = [[3-r, 2*u, 0],
          [u, 1+r/2, u/2],
          [0, u, r/2]]
    r3 = blocks([extend(a3, 5)] + [extend(b2, 3) for _ in range(3)]
                + [zero(2)])
    r2 = blocks([extend(a4, 5)] + [extend(b3, 3) for _ in range(3)]
                + [eye(2)])
    aa3 = [4-3*r, 1+3*r/2, 3*r/2]
    oo3 = [9*u*u, F(3,2)*u*u]
    aa4 = [6-3*r, F(3), 1+3*r/2, 3*r/2]
    oo4 = [9*u*u, 6*u*u, F(3,2)*u*u]
    bb2 = [1-r/2, r/2]
    ob2 = [u*u/2]
    bb3 = [3-r, 1+r/2, r/2]
    ob3 = [2*u*u, u*u/2]
    p3 = [-F(3,4)*r*r*(2+3*r), 4+F(15,4)*r*r, F(-5), F(1)]
    pb2 = [r*r/4, F(-1), F(1)]
    p4 = [F(27,4)*r*r*(2+2*r+r*r),
          -(18+F(135,4)*r*r+F(27,4)*r**3),
          27+F(39,4)*r*r, F(-10), F(1)]
    pb3 = [-r*r*(5+r)/4, 3+F(7,4)*r*r, F(-4), F(1)]
    for d, o, expected in ((aa3,oo3,p3), (bb2,ob2,pb2),
                           (aa4,oo4,p4), (bb3,ob3,pb3)):
        must(tri_poly(d, o) == expected, "characteristic factor")
    must(leading_dets([3-x for x in bb3], ob3) ==
         [r, F(3,2)*r*r, r*r*(16-r)/4], "B3 shifted determinants")
    must(leading_dets([x-1 for x in aa4], oo4) ==
         [5-3*r, 10-15*r+9*r*r,
          F(3,2)*r*(3*r-2)*(5-r),
          F(3,4)*r*r*(9*r*r+9*r-14)], "A4 shifted determinants")
    chi3 = product_polys([[F(0)]*7+[F(1)], p3, pb2, pb2, pb2])
    chi2 = product_polys([[F(0),F(1)], [F(-1),F(1)],
                          [F(-1),F(1)], p4, pb3, pb3, pb3])
    missing = product_polys([[F(0),F(1)], [F(-1),F(1)],
                             [F(-1),F(1)], p4, pb3, pb3])
    return r2, r3, chi2, chi3, missing

def prefix(values):
    out, total = [], F(0)
    for value in values:
        total += value
        out.append(total)
    return out

def reference(p):
    t = abs(1-p)
    a, b = (1+t)/2, (1-t)/2
    values = [a**(4-i.bit_count()) * b**i.bit_count()
              for i in range(16)]
    return prefix(sorted(values, reverse=True))

def projectors(u):
    order = [0,5,10,15] + [i for i in range(16) if i not in (0,5,10,15)]
    current, out = zero(16), []
    for col in order:
        v = [row[col] for row in u]
        current = lin([(F(1), current), (F(1), outer(v))])
        out.append(current)
    for k, q in enumerate(out, 1):
        must(mm(q, q) == q and q == adj(q) and tr(q) == k,
             "complex consuming projector")
    return out

def numerical_eigenvalues(a):
    n = len(a)
    real = [[float(x[0]) for x in row] for row in a]
    imag = [[float(x[1]) for x in row] for row in a]
    m = [real[i] + [-x for x in imag[i]] for i in range(n)]
    m += [imag[i] + real[i] for i in range(n)]
    size = 2*n
    for sweep in range(70):
        tick()
        off = max(abs(m[i][j]) for i in range(size) for j in range(i))
        if off < 2e-14:
            break
        for p in range(size-1):
            for q in range(p+1, size):
                x = m[p][q]
                if abs(x) < 1e-16:
                    continue
                tau = (m[q][q]-m[p][p])/(2*x)
                tangent = (1.0 if tau >= 0 else -1.0) / (
                    abs(tau) + math.sqrt(1+tau*tau))
                c = 1/math.sqrt(1+tangent*tangent)
                s = tangent*c
                m[p][p] -= tangent*x
                m[q][q] += tangent*x
                m[p][q] = m[q][p] = 0.0
                for k in range(size):
                    if k in (p,q):
                        continue
                    kp, kq = m[k][p], m[k][q]
                    m[k][p] = m[p][k] = c*kp-s*kq
                    m[k][q] = m[q][k] = s*kp+c*kq
    residual = max(sum(abs(m[i][j]) for j in range(size) if i != j)
                   for i in range(size))
    must(residual < 1e-11, "numerical Jacobi convergence")
    doubled = sorted((m[i][i] for i in range(size)), reverse=True)
    must(max(abs(doubled[2*i]-doubled[2*i+1]) for i in range(n)) < 1e-10,
         "realification paired eigenvalues")
    return [(doubled[2*i]+doubled[2*i+1])/2 for i in range(n)], residual

def reject(reason, operation):
    try:
        operation()
    except CheckFailure as error:
        must(str(error) == reason, "mutation wrong rejection reason")
        return
    raise CheckFailure("mutation survived: " + reason)

def family_vector(a, b):
    v = [Z]*16
    v[0] = G(a)
    for site in range(4):
        v[1 << (3-site)] = G(b/2)
    return v

def schmidt_matrix(v, sites):
    other = tuple(i for i in range(4) if i not in sites)
    a = zero(1 << len(sites), 1 << len(other))
    for i, value in enumerate(v):
        a[pack(i, sites)][pack(i, other)] = value
    return a

def run():
    u = local_unitary()
    must(mm(u, adj(u)) == eye(16), "physical local unitarity")
    qs = projectors(u)
    v_basis = invariant_basis()
    ref_layers = {
        1: prefix([4]+[3]*4+[2]*6+[1]*4+[0]),
        2: prefix([6]+[3]*4+[1]*6+[0]*5),
        3: prefix([4]+[1]*4+[0]*11),
    }
    parameters = [F(0),F(1,3),F(2,3),F(5,6),F(1),F(7,6),F(4,3)]
    inputs = [(F(0),F(0),F(1)), (F(9,25),F(3,5),F(4,5)),
              (F(1),F(1),F(0))]
    saved = {}
    cases = 0
    numeric_prefixes = 0
    max_violation = float("-inf")
    max_eigen_residual = 0.0
    for qvalue, amplitude0, amplitude_w in inputs:
        tick()
        r, coherent = 1-qvalue, amplitude0*amplitude_w
        v = family_vector(amplitude0, amplitude_w)
        rho = outer(v)
        must(tr(rho) == 1 and mm(rho,rho) == rho, "normalized pure input")
        h = layers(rho)
        r2, r3, chi2, chi3, missing = representations(r, coherent)
        must(mm(h[2],v_basis) == mm(v_basis,r2), "physical H2 invariant identity")
        must(mm(h[3],v_basis) == mm(v_basis,r3), "physical H3 invariant identity")
        must(len(chi2) == len(chi3) == 17, "characteristic degree")
        must(tr(h[1]) == 32 and tr(h[2]) == 24 and tr(h[3]) == 8,
             "physical layer traces")
        s1 = sum(2*trprod(partial(rho,(i,)), partial(rho,(i,)))-1
                 for i in range(4))
        eta = trprod(rho, spin(rho))
        moment = trprod(h[3],h[3])
        must(eta == 0 and s1 == 4-3*r*r, "family spin flip and S1")
        must(moment == 20-9*r*r == 8+3*s1+2*eta, "family H3 moment")
        cuts = [(i,) for i in range(4)] + [(0,j) for j in (1,2,3)]
        for cut in cuts:
            must(rank(schmidt_matrix(v,cut)) == (1 if qvalue == 1 else 2),
                 "physical Schmidt rank")
        if qvalue < 1:
            pair_expected = [
                [G(qvalue+r/2),G(coherent/2),G(coherent/2),Z],
                [G(coherent/2),G(r/4),G(r/4),Z],
                [G(coherent/2),G(r/4),G(r/4),Z],
                [Z,Z,Z,Z],
            ]
            for sites in ((0,1),(0,2),(0,3)):
                marginal = partial(rho,sites)
                must(marginal == pair_expected and rank(marginal) == 2,
                     "pair support from actual partial trace")
            support0, support1 = [O,Z,Z,Z], [Z,O,O,Z]
            def determinant2(w):
                return sub(mul(w[0],w[3]),mul(w[1],w[2]))
            must(determinant2(support0) == Z and determinant2(support1) == G(-1),
                 "pair-support product conic")
            mixed = [add(x,y) for x,y in zip(support0,support1)]
            must(determinant2(mixed) == G(-1), "pair-support mixed conic")
        transformed = conjugate(u,rho)
        transformed_h = layers(transformed)
        for m in (1,2,3):
            must(transformed_h[m] == conjugate(u,h[m]), "physical layer covariance")
        outputs_by_state = []
        for label, actual, actual_h in (
                ("base",rho,h), ("complex-LU",transformed,transformed_h)):
            psd(actual)
            for m in (1,2,3):
                psd(actual_h[m])
                for k, projector in enumerate(qs):
                    must(trprod(projector,actual_h[m]) <= ref_layers[m][k],
                         "fixed-projector layer prefix")
            outputs = {}
            for p in parameters:
                tick()
                output = erasure(actual,actual_h,p)
                must(output == pauli_channel(actual,p), "erasure versus Pauli")
                must(tr(output) == 1, "channel trace")
                psd(output)
                bound = reference(p)
                if p <= 1:
                    t, b = 1-p, p/2
                    for k, projector in enumerate(qs):
                        lhs = trprod(projector,output)
                        assembled = (t**4*trprod(projector,actual)
                                     +t**3*b*trprod(projector,actual_h[3])
                                     +t*t*b*b*trprod(projector,actual_h[2])
                                     +t*b**3*trprod(projector,actual_h[1])
                                     +(k+1)*b**4)
                        ref_assembled = (t**4+t**3*b*ref_layers[3][k]
                                         +t*t*b*b*ref_layers[2][k]
                                         +t*b**3*ref_layers[1][k]
                                         +(k+1)*b**4)
                        must(lhs == assembled, "same-projector channel assembly")
                        must(ref_assembled == bound[k], "co-ordered reference assembly")
                        must(lhs <= bound[k], "exact fixed-projector output bound")
                else:
                    positive = erasure(actual,actual_h,2-p)
                    must(output == spin(positive), "full-transpose output transport")
                    for k, projector in enumerate(qs):
                        transported = spin(projector)
                        must(mm(transported,transported) == transported
                             and transported == adj(transported)
                             and tr(transported) == k+1, "transported projector")
                        must(trprod(projector,output) == trprod(transported,positive),
                             "same-projector negative-branch pairing")
                        must(trprod(projector,output) <= bound[k],
                             "exact negative fixed-projector bound")
                if p == 0:
                    must(output == actual, "p zero endpoint")
                if p == 1:
                    must(output == lin([(F(1,16),eye(16))]), "p one endpoint")
                eigenvalues, residual = numerical_eigenvalues(output)
                max_eigen_residual = max(max_eigen_residual,residual)
                total = 0.0
                for k, eigenvalue in enumerate(eigenvalues):
                    total += eigenvalue
                    excess = total-float(bound[k])
                    max_violation = max(max_violation,excess)
                    must(excess <= TOL, "NUMERICAL output prefix")
                    numeric_prefixes += 1
                must(min(eigenvalues) >= -TOL, "NUMERICAL output PSD")
                outputs[p] = output
                cases += 1
            outputs_by_state.append(outputs)
        for p in parameters:
            must(outputs_by_state[1][p] == conjugate(u,outputs_by_state[0][p]),
                 "actual channel local covariance")
        saved[qvalue] = (rho,h,r2,r3,missing,transformed,transformed_h,
                         outputs_by_state,moment)
        print("EXACT written-factor comparison completed q =",str(qvalue),
              "H3 moment =",str(moment))
        print("H2 characteristic ascending coefficients:", " ".join(map(str,chi2)))
        print("H3 characteristic ascending coefficients:", " ".join(map(str,chi3)))
    middle = saved[F(9,25)]
    rho,h,r2,r3,missing,complex_rho,complex_h,outputs,moment = middle
    bad_sign = [row[:] for row in r3]
    bad_sign[0][1] = neg(bad_sign[0][1])
    bad_sign[1][0] = neg(bad_sign[1][0])
    reject("sqrt-sign", lambda: must(
        mm(h[3],v_basis) == mm(v_basis,bad_sign), "sqrt-sign"))
    bad_trace = [row[:] for row in r2]
    bad_trace[0][0] = add(bad_trace[0][0],O)
    reject("H2-block-trace", lambda: must(tr(bad_trace) == 24,"H2-block-trace"))
    reject("missing-multiplicity", lambda: must(
        len(missing) == 17, "missing-multiplicity"))
    source_sites, wrong_sites = (0,1,3), (0,1,2)
    actual_marginal = partial(complex_rho,source_sites)
    bad_index = lin([(F(1),complex_h[3]),
                     (F(-1),embed(actual_marginal,source_sites)),
                     (F(1),embed(actual_marginal,wrong_sites))])
    reject("third-qubit-physical-index", lambda: must(
        bad_index == complex_h[3], "third-qubit-physical-index"))
    positive = outputs[1][F(2,3)]
    wrong_transpose = conjugate_w(partial_transpose(positive,2))
    reject("partial-not-full-transpose", lambda: must(
        wrong_transpose == spin(positive), "partial-not-full-transpose"))
    reject("q-zero-is-not-product-vacuum", lambda: must(
        saved[F(0)][0][0][0] == O, "q-zero-is-not-product-vacuum"))
    reject("q-one-is-not-W", lambda: must(
        saved[F(1)][0][0][0] == Z, "q-one-is-not-W"))
    one_product_ray = 1
    reject("old-two-product-ray-class", lambda: must(
        one_product_ray == 2, "old-two-product-ray-class"))
    r = F(16,25)
    reject("wrong-family-moment", lambda: must(
        moment == 20-8*r*r, "wrong-family-moment"))
    thresholds = [F(x*x,k)+F((8-x)**2,16-k)
                  for k,x in ((2,5),(3,6),(4,7))]
    must(thresholds == [F(92,7),F(160,13),F(37,3)], "moment boundaries")
    reject("wrong-moment-threshold", lambda: must(
        min(thresholds) == F(160,12), "wrong-moment-threshold"))
    must(cases == 42 and numeric_prefixes == 672, "complete finite coverage")
    tick()
    print("PASS: exact physical-matrix identities and 10 intended-reason mutations")
    print("NUMERICAL, NOT EXACT: cases =",cases,"prefixes =",numeric_prefixes)
    print("NUMERICAL tolerance =",TOL,"max prefix excess =",max_violation)
    print("NUMERICAL max Jacobi off-diagonal row residual =",max_eigen_residual)
    print("Elapsed seconds =",time.monotonic()-START)
    print("LIMIT: family eta is zero; eta coefficient not finitely distinguished")
    print("LIMIT: no unrestricted target, novelty, independent-family or kernel claim")

try:
    run()
except Deadline as error:
    print("INCOMPLETE:",str(error),"; no PASS or completed-coverage claim")
    raise SystemExit(2)
