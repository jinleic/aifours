#!/usr/bin/env python3
"""F776 X-side replay only. NOT RUN by author; no y/u/J/U3/original caller.

Parent: whole-read and pin these exact bytes before a separate <=55 s GO.
Stdlib/builtins only; no file/network/subprocess I/O, random seed, or imports.
The assertions checked here do not certify the written common-Y theorem.
"""

class CheckFailure(Exception):
    pass


def need(ok, reason):
    if not ok:
        raise CheckFailure(reason)


def sign(v):
    return -1 if v.bit_count() & 1 else 1


def point(ell, h, i, b):
    return (ell << 5) | (h << 4) | (i << 2) | b


# alpha masks: u=b0 is 2, v=b1 is 1, w=u+v is 3.
# E tuples are (i,h,b,sign); graph mate tuples are (i,b,sign).
DATA = {
    'I': ([(2,1),(2,1),(3,1),(3,1)],
          [(0,b,sign(b & 1)) for b in range(4)],
          [(2,0,2,1),(2,0,3,1),(2,1,1,-1),(2,1,2,-1),
           (3,0,1,1),(3,0,3,-1)],
          (0,0,0,1), (4,), ()),
    'II': ([(2,1),(2,1),(1,1),(1,-1)],
           [(0,0,1),(0,2,-1),(1,0,-1),(1,2,1)],
           [(2,0,1,1),(2,0,2,1),(2,1,1,-1),(2,1,3,-1),
            (3,0,2,1),(3,0,3,-1)],
           (0,0,0,1), (2,2), ()),
    'III': ([(2,1),(2,-1),(3,-1),(1,1)],
            [(0,0,1),(0,1,-1)],
            [(2,0,0,1),(2,0,1,1),(2,1,0,-1),(2,1,3,-1),
             (3,0,1,1),(3,0,2,-1),(0,0,2,1),(0,0,3,-1)],
            (0,0,0,1), (2,), (2,)),
    'IIIp': ([(2,1),(2,1),(3,-1),(1,-1)],
             [(0,0,1),(0,1,-1)],
             [(2,0,2,1),(2,0,3,1),(2,1,0,-1),(2,1,3,-1),
              (3,0,0,1),(3,0,3,-1),(0,0,2,1),(0,0,3,-1)],
             (0,0,0,1), (2,), (1,1)),
    'IV': ([(2,1),(2,-1),(1,1),(1,1)], [],
           [(1,0,0,1),(1,0,3,1),(1,1,0,-1),(1,1,3,-1),
            (2,0,0,1),(2,0,2,-1),(2,1,0,1),(2,1,1,-1),
            (3,0,1,1),(3,0,2,-1)],
           (0,0,0,1), (), (2,2)),
    'IVp': ([(2,1),(2,-1),(1,1),(1,1)], [],
            [(1,0,1,1),(1,0,2,1),(1,1,0,-1),(1,1,3,-1),
             (2,0,0,1),(2,0,2,-1),(2,1,0,-1),(2,1,1,1),
             (3,0,0,1),(3,0,3,-1)],
            (0,0,0,1), (), (2,1,1)),
    'F754': ([(1,1),(2,1),(2,1),(1,-1)], [],
             [(2,0,0,1),(2,0,2,1),(2,1,0,-1),(2,1,1,-1),
              (1,0,0,1),(1,0,3,-1),
              (3,0,0,1),(3,0,1,-1),(3,0,2,-1),(3,0,3,1)],
             (0,0,1,0), (), (2,1,1)),
}


def build(name, F):
    graph, mates, esites, _, _, _ = DATA[name]
    need(len(F) == 4 and all(f in (0,1) for f in F), 'F_DOMAIN')
    X = [0]*64
    for i,(alpha,sgn) in enumerate(graph):
        for b in range(4):
            p = point(1,F[i],i,b)
            need(X[p] == 0, 'DUPLICATE_SITE')
            X[p] = sgn * sign(alpha & b)
    for i,b,sgn in mates:
        p = point(1,1-F[i],i,b)
        need(X[p] == 0 and sgn in (-1,1), 'DUPLICATE_SITE')
        X[p] = 2*sgn
    for i,h,b,sgn in esites:
        p = point(0,h,i,b)
        need(X[p] == 0 and sgn in (-1,1), 'DUPLICATE_SITE')
        X[p] = 2*sgn
    return X


def column(X, s, alpha):
    out = []
    for ell in range(2):
        for i in range(4):
            raw = sum(X[point(ell,h,i,b)]*sign(s*h)*sign(alpha & b)
                      for h in range(2) for b in range(4))
            need(raw % 4 == 0, 'PROFILE_INTEGRALITY')
            out.append(raw//4)
    return out


def profiles(X):
    cols = {}
    for s in range(2):
        for alpha in range(4):
            z = column(X,s,alpha)
            cols[s,alpha] = z
            if (s,alpha) == (0,0):
                need(not any(z), 'ZERO_FLAT')
                continue
            support = [k for k,v in enumerate(z) if v]
            if len(support) == 1:
                need(abs(z[support[0]]) == 2, 'SINGLETON_VALUE')
            else:
                need(len(support) == 4 and all(abs(z[k]) == 1 for k in support),
                     'PROFILE_SHAPE')
                a,b,c,d = support
                need((a ^ b ^ c ^ d) == 0, 'AFFINE_PLANE')
                need(z[a]*z[b]*z[c]*z[d] == -1, 'SIGN_PRODUCT')
    return cols


def quotient_count(z, expected):
    vals = [sum(z[j]*sign(k & j) for j in range(8)) for k in range(8)]
    need(sum(abs(v) == 2 for v in vals) == expected and
         all(abs(v) == 2 for v in vals), 'QUOTIENT_COUNT')


def expected_columns(name, s):
    r = 1 if s == 0 else -1
    if name == 'I':
        return ({4:1,5:1,2:-1,3:1}, {4:2*r}, {6:1,7:r,2:r,3:-1})
    if name == 'II':
        return ({4:2} if s == 0 else {5:2},
                {6:1,7:-r,2:r,3:1}, {4:r,5:-r,2:-1,3:-1})
    if name == 'III':
        return ({4:1,5:-1,2:1,3:1}, {4:r,7:r,0:1,3:-1},
                {4:r,6:-1,2:-r,0:-1})
    if name == 'IIIp':
        return ({4:1,5:1,2:-1,3:1}, {4:r,7:-r,0:1,3:1},
                {4:r,6:-1,2:-r,0:-1})
    if name == 'IV':
        return ({4:1,5:-1,2:1,3:1}, {6:1,7:r,2:r,3:-1},
                {2:2} if s == 0 else {1:2})
    if name == 'IVp':
        return ({4:1,5:-1,2:1,3:1}, {6:1,7:r,2:-r,3:1},
                {1:-2} if s == 0 else {2:2})
    if name == 'F754':
        return ({5:1,6:r,1:1,2:-r}, {4:1,7:-1,1:1,2:1}, {3:2})
    raise CheckFailure('UNKNOWN_EXAMPLE')


def check_displayed_columns(name, cols):
    singleton = 1 if name in ('IV','IVp') else 2
    need(cols[1,0] == [2 if k == singleton else 0 for k in range(8)],
         'DISPLAYED_LAMBDA')
    for s in range(2):
        for alpha, values in zip((2,1,3), expected_columns(name,s)):
            need(cols[s,alpha] == [values.get(k,0) for k in range(8)],
                 'DISPLAYED_COLUMN')


def census(name, X, F):
    need(all(X[point(0,h,0,0)] == 0 for h in range(2)), 'FULL_SITE')
    graph = [point(1,F[i],i,b) for i in range(4) for b in range(4)]
    mates = [[point(1,1-F[i],i,b) for b in range(4)] for i in range(4)]
    e = [[point(0,h,i,0) for h in range(2)] for i in range(1,4)]
    z = [point(0,h,i,b) for h in range(2) for i in range(4) for b in (1,2,3)]
    need(all(abs(X[p]) == 1 for p in graph), 'GRAPH_AMPLITUDE')
    need(all(abs(X[p]) in (0,2) for row in mates+e for p in row), 'D_AMPLITUDE')
    need(all(abs(X[p]) in (0,2) for p in z), 'Z_AMPLITUDE')
    m = tuple(sorted((sum(X[p] != 0 for p in row) for row in mates), reverse=True))
    ecount = tuple(sorted((sum(X[p] != 0 for p in row) for row in e), reverse=True))
    m = tuple(v for v in m if v)
    ecount = tuple(v for v in ecount if v)
    need(m == DATA[name][4] and ecount == DATA[name][5], 'OCCUPANCY')
    W = [p for row in mates+e for p in row if X[p]] + [p for p in z if X[p]]
    need(sum(m)+sum(ecount) == 4 and len(W) == 10, 'D0_CENSUS')
    need(sum(X[p] != 0 for p in z) == 6, 'Z2_CENSUS')
    need(sum(X[p] == 0 for p in z) == 18, 'Z4_CHOICES')
    need(sum(v*v for v in X) == 56, 'X_ENERGY')
    return graph,W


def xor_values(values):
    x = 0
    for value in values:
        x ^= value
    return x


def walsh(X, freq):
    return sum(v*sign(freq & p) for p,v in enumerate(X))


def carried_zero(x,t):
    need(walsh(x,t) == 0, 'CARRIED_ZERO')


def check_transport(X, graph, W, t):
    x = [v*sign(t & p) for p,v in enumerate(X)]
    carried_zero(x,t)
    spectrum = [walsh(x,k) for k in range(64)]
    need(all(v == 0 or abs(v) == 8 for v in spectrum), 'U0_CAP_DIVISIBILITY')
    need(sum(v == 0 for v in spectrum) == 8, 'U0_ZERO_CENSUS')
    P = [p for p in graph if x[p] < 0]
    N = [p for p in W if x[p] < 0]
    need(len(P) % 2 == 0, 'C_EVEN_GRAPH')
    need((len(P)//2 + len(N)) % 2 == 1, 'C_PARITY')
    need(xor_values(P) == xor_values(W), 'C_XOR')


def predicted_F(name,F):
    a,b,c,d = F
    if name in ('III','IIIp'):
        return a == b == c and d != a
    if name == 'F754':
        return a == d and b != c
    return a == b and c != d


def expect_failure(reason, callback):
    try:
        callback()
    except CheckFailure as exc:
        need(str(exc) == reason, 'WRONG_CONTROL_REASON')
        return
    raise CheckFailure('CONTROL_ACCEPTED_' + reason)


def main():
    f_seen = 0
    f_valid = 0
    transports = 0
    for name in DATA:
        base = DATA[name][3]
        X0 = build(name,base)
        cols0 = profiles(X0)
        check_displayed_columns(name,cols0)
        census(name,X0,base)
        for x in range(16):
            F = tuple((x >> k) & 1 for k in (3,2,1,0))
            if sum(F) % 2 != 1:
                continue
            f_seen += 1
            X = build(name,F)
            try:
                cols = profiles(X)
                valid = True
            except CheckFailure:
                valid = False
                cols = None
            need(valid == predicted_F(name,F), 'F_CLASSIFICATION')
            if not valid:
                continue
            f_valid += 1
            graph,W = census(name,X,F)
            for eta,z in cols.items():
                if eta != (0,0):
                    quotient_count(z,8)
            for t in range(64):
                check_transport(X,graph,W,t)
                transports += 1
    need((f_seen,f_valid,transports) == (56,24,1536), 'COVERAGE_CENSUS')

    # Intended-reason controls, not counted as mathematical witnesses.
    base = DATA['I'][3]
    X0 = build('I',base)
    mutant = X0.copy()
    mutant[point(0,0,2,2)] *= -1
    expect_failure('ZERO_FLAT', lambda: profiles(mutant))
    expect_failure('SIGN_PRODUCT', lambda: profiles(build('I',(1,0,1,1))))
    expect_failure('QUOTIENT_COUNT', lambda: quotient_count(column(X0,1,0),4))
    mutant = X0.copy()
    mutant[point(0,0,0,0)] = 2
    expect_failure('FULL_SITE', lambda: census('I',mutant,base))
    expect_failure('CARRIED_ZERO', lambda: carried_zero(X0,1))
    print('PASS_X_ONLY f_checked=56 f_profile_valid=24 transports=1536 '
          'z4_choices_per_transport=18 controls=5')
    print('NOT_A_WITNESS: no common u/y, phase completion, J, U3 caps, V or caller')


if __name__ == '__main__':
    main()
