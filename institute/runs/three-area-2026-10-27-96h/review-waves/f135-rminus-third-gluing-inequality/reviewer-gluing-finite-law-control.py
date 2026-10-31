#!/usr/bin/env python3
"""Reviewer-written finite-law control for the conditional product gluing argument.

Gluing lemma (as used by the reviewer): for a law P on (X,D,F), X=(a,...,j), define
    Q(x,d,f) = P(x) * P(d|x) * P(f|x)   (0 where P(x)=0).
Then (i) Q is a law; (ii) Q_{X,D} = P_{X,D} and Q_{X,F} = P_{X,F} exactly; (iii) Q(d,f|x)=Q(d|x)Q(f|x),
so I_Q(D;F|X)=0; (iv) any coefficient vector supported on subsets of X+D or of X+F takes the same value
at P and Q. The glued variables are D and F, glued conditionally on the FULL original vector X.

Exact (Fraction) checks: (i)-(iii) and marginal equality. Numeric (Decimal, 60 digits) checks: the
identity residual at P and at Q, I_P(D;F|X)>0 (so the negative term is active), I_Q(D;F|X)=0,
all twelve glued CMIs >= 0, L3(P) = L3(Q) >= 0. A wrong-conditioning control glues on X minus {j}
and shows the (X,F) marginal and L3 change, i.e. the full-X conditioning is load bearing.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import json, random, subprocess

getcontext().prec = 60
LN2 = Decimal(2).ln()
HERE = Path(__file__).resolve().parent
OUT = HERE / 'reviewer-gluing-finite-law-control-receipt.json'
X = tuple('abcdefghij'); ALL = X + ('D', 'F')
L3_TERMS = [
    (-1, 'abcehi'), (-1, 'acefghi'), (+2, 'abcdefghij'),
    (+1, 'abcefhiD'), (+1, 'acefghiD'), (-1, 'acefhijD'), (+1, 'abcefhijD'), (-2, 'abcdefghijD'),
    (+1, 'abcehiF'), (-1, 'acefhiF'), (+1, 'acefghiF'), (-1, 'abcefghiF'),
    (-1, 'abcdfhjF'), (+1, 'abcdfghjF'), (+1, 'acefhijF'), (-1, 'abcefhijF'),
    (+1, 'abcdefhijF'), (-1, 'abcdefghijF'),
]
CMI_ROWS = [('b','g','acefhiDF'),('b','F','acefhijD'),('d','D','abcefhijF'),('d','D','abcefghiF'),
            ('e','g','abcdfhjDF'),('f','F','abcehiD'),('g','i','abcdefhjDF'),('g','D','abcdfhjF'),
            ('j','D','abcdefghiF'),('j','D','acefhiF'),('D','F','acefghi'),('D','F','abcehi')]


def clock():
    return subprocess.run(['/bin/date', '-u', '+%Y-%m-%dT%H:%M:%S.%NZ'], capture_output=True, text=True).stdout.strip()


def idx(vs):
    return tuple(ALL.index(v) for v in vs)


class Law:
    """Exact finite law: dict atom(tuple of 12 symbols) -> Fraction, with cached exact marginals and Decimal entropies."""
    def __init__(self, atoms):
        self.p = {k: v for k, v in atoms.items() if v != 0}
        if sum(self.p.values()) != 1:
            raise ValueError('NOT_NORMALISED')
        self._marg = {}; self._H = {}

    def marginal(self, vs):
        key = frozenset(vs)
        if key not in self._marg:
            ii = idx(sorted(key, key=ALL.index)); m = {}
            for atom, pr in self.p.items():
                k = tuple(atom[i] for i in ii); m[k] = m.get(k, Fraction(0)) + pr
            self._marg[key] = m
        return self._marg[key]

    def H(self, vs):
        key = frozenset(vs)
        if key not in self._H:
            h = Decimal(0)
            for pr in self.marginal(key).values():
                d = Decimal(pr.numerator) / Decimal(pr.denominator)
                h -= d * d.ln() / LN2
            self._H[key] = h
        return self._H[key]

    def cmi(self, a, b, c):
        a, b, c = frozenset(a), frozenset(b), frozenset(c)
        return self.H(a | c) + self.H(b | c) - self.H(a | b | c) - self.H(c)

    def l3(self):
        return sum((Decimal(c) * self.H(s) for c, s in L3_TERMS), Decimal(0))

    def rhs(self):
        return sum((self.cmi(a, b, c) for a, b, c in CMI_ROWS), Decimal(0)) - 2 * self.cmi('D', 'F', X)


def glue(law, cond):
    """Q(x,d,f) = P(x,d) * P(cond,f) / P(cond) restricted appropriately; cond=X is the lemma's gluing."""
    ci = idx(cond); di = ALL.index('D'); fi = ALL.index('F')
    px = law.marginal(X); pxd = law.marginal(X + ('D',)); pcf = law.marginal(tuple(cond) + ('F',)); pc = law.marginal(cond)
    xi = idx(X)
    # enumerate support of X*D and F|cond
    f_by_c = {}
    for k, v in pcf.items():
        f_by_c.setdefault(k[:-1], []).append((k[-1], v / pc[k[:-1]]))
    atoms = {}
    for k, v in pxd.items():
        x = k[:-1]; d = k[-1]; c = tuple(x[X.index(s)] for s in cond)
        for f, pf in f_by_c[c]:
            atom = [None] * 12
            for j, s in enumerate(X): atom[ALL.index(s)] = x[j]
            atom[di] = d; atom[fi] = f
            atoms[tuple(atom)] = atoms.get(tuple(atom), Fraction(0)) + v * pf
    return Law(atoms)


def random_law(seed, alph_DF, support_frac):
    rng = random.Random(seed)
    alph = [2] * 10 + [alph_DF, alph_DF]
    atoms = {}
    import itertools
    for atom in itertools.product(*[range(n) for n in alph]):
        if rng.random() < support_frac:
            atoms[atom] = Fraction(rng.randint(1, 97))
    tot = sum(atoms.values())
    return Law({k: v / tot for k, v in atoms.items()})


def coin_law(seed):
    """D = F = a fair coin independent of X (I(D;F|X) = 1 bit exactly); X random full support."""
    rng = random.Random(seed); atoms = {}
    import itertools
    xs = {x: Fraction(rng.randint(1, 50)) for x in itertools.product(range(2), repeat=10)}
    tot = sum(xs.values())
    for x, w in xs.items():
        for coin in (0, 1):
            atoms[x + (coin, coin)] = w / tot / 2
    return Law(atoms)


def exact_checks(P, Q):
    out = {}
    out['Q_sums_to_one'] = sum(Q.p.values()) == 1
    out['Q_XD_marginal_equals_P_XD'] = Q.marginal(X + ('D',)) == P.marginal(X + ('D',))
    out['Q_XF_marginal_equals_P_XF'] = Q.marginal(X + ('F',)) == P.marginal(X + ('F',))
    qx = Q.marginal(X); qxd = Q.marginal(X + ('D',)); qxf = Q.marginal(X + ('F',))
    xi = idx(X); di = ALL.index('D'); fi = ALL.index('F')
    ok = True
    for atom, v in Q.p.items():
        x = tuple(atom[i] for i in xi)
        if v * qx[x] != qxd[x + (atom[di],)] * qxf[x + (atom[fi],)]:
            ok = False; break
    out['Q_conditional_independence_D_F_given_X_exact'] = ok
    return out


def run_case(name, P):
    Q = glue(P, X)
    ex = exact_checks(P, Q)
    tol = Decimal('1e-45')
    l3p, l3q = P.l3(), Q.l3()
    cip, ciq = P.cmi('D', 'F', X), Q.cmi('D', 'F', X)
    glued_cmis = [Q.cmi(a, b, c) for a, b, c in CMI_ROWS]
    res = {
        'support_atoms_P': len(P.p), 'support_atoms_Q': len(Q.p),
        'exact': ex,
        'I_P(D;F|X)': str(cip.quantize(Decimal('1e-30'))),
        'I_Q(D;F|X)': str(ciq.quantize(Decimal('1e-30'))),
        'identity_residual_at_P': str((l3p - P.rhs()).quantize(Decimal('1e-50'))),
        'identity_residual_at_Q': str((l3q - Q.rhs()).quantize(Decimal('1e-50'))),
        'L3_P': str(l3p.quantize(Decimal('1e-30'))),
        'L3_Q': str(l3q.quantize(Decimal('1e-30'))),
        'L3_P_equals_L3_Q_to_1e-45': abs(l3p - l3q) < tol,
        'sum_glued_CMIs': str(sum(glued_cmis, Decimal(0)).quantize(Decimal('1e-30'))),
        'all_glued_CMIs_nonnegative': all(v > -tol for v in glued_cmis),
        'min_glued_CMI': str(min(glued_cmis).quantize(Decimal('1e-30'))),
        'L3_nonnegative': l3p > -tol,
    }
    passed = (all(ex.values()) and abs(l3p - P.rhs()) < tol and abs(l3q - Q.rhs()) < tol and abs(ciq) < tol
              and res['L3_P_equals_L3_Q_to_1e-45'] and res['all_glued_CMIs_nonnegative'] and res['L3_nonnegative'])
    res['PASS'] = passed
    if not passed:
        raise SystemExit(('CASE_FAILED', name, res))
    return res


def main():
    receipt = {'clock_start_utc': clock(), 'cases': {}}
    cases = {
        'random_full_support_binary_seed1': random_law(1, 2, 1.0),
        'random_sparse_binary_seed2': random_law(2, 2, 0.35),
        'random_full_support_ternary_DF_seed3': random_law(3, 3, 1.0),
        'coin_D_equals_F_independent_of_X_seed4': coin_law(4),
    }
    for name, P in cases.items():
        receipt['cases'][name] = run_case(name, P)
    # all four exercised a strictly positive I_P(D;F|X)? (the coin case is exactly 1 bit)
    receipt['all_cases_have_positive_I_P(D;F|X)'] = all(Decimal(c['I_P(D;F|X)']) > Decimal('1e-12') for c in receipt['cases'].values())
    # wrong-conditioning control: glue on X minus {j}; (X,F) marginal must generally change, hence L3 changes
    P = cases['random_full_support_binary_seed1']
    Qbad = glue(P, tuple(v for v in X if v != 'j'))
    receipt['wrong_conditioning_control_glue_on_X_minus_j'] = {
        'Q_XD_marginal_preserved': Qbad.marginal(X + ('D',)) == P.marginal(X + ('D',)),
        'Q_XF_marginal_preserved': Qbad.marginal(X + ('F',)) == P.marginal(X + ('F',)),
        'L3_changed': abs(Qbad.l3() - P.l3()) > Decimal('1e-12'),
        'L3_bad': str(Qbad.l3().quantize(Decimal('1e-30'))),
        'note': 'demonstrates the lemma needs conditioning on the full X; a proper subset does not preserve the (X,F) marginal',
    }
    if receipt['wrong_conditioning_control_glue_on_X_minus_j']['Q_XF_marginal_preserved'] or not receipt['wrong_conditioning_control_glue_on_X_minus_j']['L3_changed']:
        raise SystemExit('WRONG_CONDITIONING_CONTROL_UNEXPECTED')
    # negative identity control at a finite law: dropping CMI row 1 must leave a nonzero residual
    def rhs_minus_row(law, k):
        return sum((law.cmi(a, b, c) for i, (a, b, c) in enumerate(CMI_ROWS) if i != k), Decimal(0)) - 2 * law.cmi('D', 'F', X)
    resid = P.l3() - rhs_minus_row(P, 0)
    receipt['negative_control_identity_without_row1_at_finite_law'] = {'residual': str(resid.quantize(Decimal('1e-30'))), 'rejected': abs(resid) > Decimal('1e-12')}
    if not receipt['negative_control_identity_without_row1_at_finite_law']['rejected']:
        raise SystemExit('NEGATIVE_CONTROL_FAILED')
    receipt['verdict_gluing'] = 'LEMMA_AND_IDENTITY_CONFIRMED_ON_FINITE_LAWS'
    receipt['script_sha256'] = sha256(Path(__file__).read_bytes()).hexdigest()
    receipt['clock_end_utc'] = clock()
    with OUT.open('x', encoding='utf-8') as fh:
        json.dump(receipt, fh, indent=1); fh.write('\n')
    print(json.dumps(receipt, indent=1))


if __name__ == '__main__':
    main()
