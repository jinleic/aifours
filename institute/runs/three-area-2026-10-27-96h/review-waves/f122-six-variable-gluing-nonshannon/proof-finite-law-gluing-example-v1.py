#!/usr/bin/env python3
"""proof-finite-law-gluing-example-v1.py -- f122 reviewer-authored finite-law controls.

A concrete finite joint law on six variables (B,C,R,H,P,Q), with B,C,R,H binary
and P,Q ternary, is built with exact rational probabilities such that P and Q
are conditionally DEPENDENT given Y=(B,C,R,H). Everything about distributions
is exact (fractions.Fraction); entropies use mpmath at 60 decimal digits.

Checks:
 (1) the conditional-product glued law p'(y,p,q) = p(y) p(p|y) p(q|y) is an exact
     probability law (nonnegative, sums to 1);
 (2) for every subset mask m of {B,C,R,H,P,Q}: the marginal TABLE of p and p'
     coincide exactly iff m does not contain both P and Q; the 16 written terms
     all use non-mixed masks, so each of the 16 entropies is identical;
 (3) I(P;Q|Y)=0 under p' by exact rational factorisation p'(y,p,q)p'(y)=p'(y,p)p'(y,q)
     for every cell, and I(P;Q|Y)>0 under p;
 (4) the nine-CMI identity Phi = sum_i w_i I_i holds on the actual entropies of
     both p and p' (residual < 1e-50);
 (5) Phi(p) = Phi(p') (residual < 1e-50); Phi(p') = sum of the eight positive
     CMIs under p', each >= 0; hence Phi(p) >= 0, exhibited here with Phi(p) > 0;
 (6) negative control: Phi_bad := 8 CMIs - 3 I(P;Q|BCRH) (= Phi - I(P;Q|BCRH))
     carries the mixed coordinate H(BCRHPQ) and is violated by the law
     "Y constant, P = Q uniform bit" (value -1 bit) while Phi = 0 on that law;
     on the dependent law p the gluing does NOT preserve Phi_bad;
 (7) conditioning control: an extra binary Z with two different conditional laws;
     sum_S c_S H(S,Z) equals the p(z)-average of the conditional Phi values and
     is >= 0 (the coefficient sum of Phi is 0, so no H(Z) term appears);
 (8) seeded random sweep: pseudo-random rational laws (full-support and sparse),
     Phi >= -1e-45, identity residual < 1e-45, glued Phi equal within 1e-45.

No author code is imported or executed. Output: JSON receipt on stdout.
"""
import json
import random
import sys
from fractions import Fraction as F
from itertools import product

import mpmath as mp

mp.mp.dps = 60

NAMES = ['B', 'C', 'R', 'H', 'P', 'Q']
BIT = {n: 1 << i for i, n in enumerate(NAMES)}


def mask(s):
    m = 0
    for ch in s:
        m |= BIT[ch]
    return m


TERMS = [('BC', -1), ('BR', -1), ('BCRH', 2),
         ('BCP', 1), ('BRP', 1), ('BCRP', -1), ('BHP', -1), ('BCHP', 1), ('BCRHP', -1),
         ('BQ', -1), ('BCQ', 1), ('BRQ', 1), ('BHQ', 1), ('CHQ', -1), ('CRHQ', 1), ('BCRHQ', -2)]
CMI = [('B', 'R', 'CHPQ', 1), ('C', 'R', 'BPQ', 1), ('C', 'Q', 'BHP', 1),
       ('R', 'P', 'CHQ', 1), ('H', 'P', 'BQ', 1), ('H', 'Q', 'BCRP', 1),
       ('P', 'Q', 'BR', 1), ('P', 'Q', 'BC', 1), ('P', 'Q', 'BCRH', -2)]
YMASK = mask('BCRH')
PM, QM = BIT['P'], BIT['Q']


def is_mixed(m):
    return bool(m & PM) and bool(m & QM)


# ---------- exact distributions ----------------------------------------------
# a law is a dict: outcome tuple (b,c,r,h,p,q) -> Fraction
def marginal(law, m):
    out = {}
    for x, pr in law.items():
        key = tuple(x[i] if (m >> i) & 1 else None for i in range(6))
        out[key] = out.get(key, F(0)) + pr
    return out


def entropy(table):
    h = mp.mpf(0)
    for pr in table.values():
        if pr:
            q = mp.mpf(pr.numerator) / pr.denominator
            h -= q * mp.log(q, 2)
    return h


def all_entropies(law):
    return [entropy(marginal(law, m)) if m else mp.mpf(0) for m in range(64)]


def cmi(Hs, a, b, z):
    A, Bm, Z = mask(a), mask(b), mask(z)
    return Hs[A | Z] + Hs[Bm | Z] - Hs[A | Bm | Z] - Hs[Z]


def phi(Hs, terms=TERMS):
    return sum(c * Hs[mask(s)] for s, c in terms)


def cmi_sum(Hs, rows=CMI):
    return sum(w * cmi(Hs, a, b, z) for a, b, z, w in rows)


def glue(law):
    """conditional-product gluing of (P,Q) given Y=(B,C,R,H)."""
    py = marginal(law, YMASK)
    pyp = marginal(law, YMASK | PM)
    pyq = marginal(law, YMASK | QM)
    out = {}
    ys = {k for k in py}
    for yk in ys:
        y = yk[:4]
        ps = {k[4] for k in pyp if k[:4] == y}
        qs = {k[5] for k in pyq if k[:4] == y}
        for p_ in ps:
            for q_ in qs:
                val = pyp[(y + (p_, None))] * pyq[(y + (None, q_))] / py[yk]
                if val:
                    out[y + (p_, q_)] = val
    return out


def factorises_given_y(law):
    py = marginal(law, YMASK); pyp = marginal(law, YMASK | PM); pyq = marginal(law, YMASK | QM)
    for x, pr in law.items():
        y = x[:4]
        if pr * py[y + (None, None)] != pyp[y + (x[4], None)] * pyq[y + (None, x[5])]:
            return False
    # also zero cells of the product support must be zero in law
    for yk in py:
        y = yk[:4]
        for p_ in range(3):
            for q_ in range(3):
                lhs = law.get(y + (p_, q_), F(0)) * py[yk]
                rhs = pyp.get(y + (p_, None), F(0)) * pyq.get(y + (None, q_), F(0))
                if lhs != rhs:
                    return False
    return True


# ---------- the structured dependent law L1 -----------------------------------
def structured_law(variant=0):
    law = {}
    wy = {}
    for b, c, r, h in product(range(2), repeat=4):
        wy[(b, c, r, h)] = 1 + b + 2 * c + 3 * r + 4 * h + b * c + r * h + variant * (2 * b + h)
    tot_y = sum(wy.values())
    for y, w in wy.items():
        b, c, r, h = y
        T = [[1 + ((i + 2 * j + b + c * i + r * j + h * i * j + variant * (i + j)) % 5) + 2 * (i == j) * (1 + b)
              for j in range(3)] for i in range(3)]
        s = sum(map(sum, T))
        for i in range(3):
            for j in range(3):
                law[y + (i, j)] = F(w, tot_y) * F(T[i][j], s)
    return law


def random_law(rng, sparse):
    law = {}
    for x in product(range(2), range(2), range(2), range(2), range(3), range(3)):
        w = rng.randint(0, 5) if sparse else rng.randint(1, 50)
        if w:
            law[x] = F(w)
    tot = sum(law.values())
    return {x: v / tot for x, v in law.items()}


def s(x):
    return mp.nstr(x, 30)


def main():
    out = {'script': 'proof-finite-law-gluing-example-v1.py', 'mp_dps': mp.mp.dps, 'sections': {}}
    TOL = mp.mpf('1e-50')

    # (1)-(5) structured law
    L = structured_law(0)
    assert sum(L.values()) == 1 and all(v > 0 for v in L.values()) and len(L) == 144
    G = glue(L)
    assert sum(G.values()) == 1 and all(v > 0 for v in G.values())
    HL, HG = all_entropies(L), all_entropies(G)
    eq_tables = {m: (marginal(L, m) == marginal(G, m)) for m in range(1, 64)}
    non_mixed_all_equal = all(eq_tables[m] for m in range(1, 64) if not is_mixed(m))
    mixed_differ = [m for m in range(1, 64) if is_mixed(m) and not eq_tables[m]]
    mixed_equal = [m for m in range(1, 64) if is_mixed(m) and eq_tables[m]]
    term_entropy_equal = all(HL[mask(t)] == HG[mask(t)] for t, _ in TERMS)
    ipq_L = cmi(HL, 'P', 'Q', 'BCRH'); ipq_G = cmi(HG, 'P', 'Q', 'BCRH')
    fact_G = factorises_given_y(G); fact_L = factorises_given_y(L)
    phiL, phiG = phi(HL), phi(HG)
    idL = phiL - cmi_sum(HL); idG = phiG - cmi_sum(HG)
    eight_G = [(f'I({a};{b}|{z})', cmi(HG, a, b, z)) for a, b, z, w in CMI[:-1]]
    eight_L = [(f'I({a};{b}|{z})', cmi(HL, a, b, z)) for a, b, z, w in CMI[:-1]]
    sum8G = sum(v for _, v in eight_G)
    out['sections']['1_laws'] = {
        'L_support_cells': len(L), 'L_sum_is_one': sum(L.values()) == 1,
        'G_support_cells': len(G), 'G_sum_is_one': sum(G.values()) == 1, 'G_all_nonneg': all(v >= 0 for v in G.values()),
        'L_first_cells': {str(k): str(v) for k, v in list(sorted(L.items()))[:6]},
        'G_first_cells': {str(k): str(v) for k, v in list(sorted(G.items()))[:6]},
    }
    out['sections']['2_marginal_tables'] = {
        'all_47_non_mixed_marginal_tables_identical_exact': non_mixed_all_equal,
        'count_non_mixed_masks': sum(1 for m in range(1, 64) if not is_mixed(m)),
        'mixed_masks_whose_tables_differ': mixed_differ,
        'mixed_masks_whose_tables_coincide': mixed_equal,
        'all_16_written_term_entropies_identical_exact_mpf': term_entropy_equal,
    }
    out['sections']['3_conditional_independence'] = {
        'I(P;Q|Y)_under_L_bits': s(ipq_L), 'I(P;Q|Y)_under_L_positive': bool(ipq_L > mp.mpf('1e-6')),
        'I(P;Q|Y)_under_G_bits': s(ipq_G), 'I(P;Q|Y)_under_G_below_1e-50': bool(abs(ipq_G) < TOL),
        'G_factorises_exactly_rational': fact_G, 'L_factorises_exactly_rational': fact_L,
    }
    out['sections']['4_identity_on_actual_entropies'] = {
        'residual_L': s(idL), 'residual_G': s(idG),
        'both_below_1e-50': bool(abs(idL) < TOL and abs(idG) < TOL),
    }
    out['sections']['5_gluing_preserves_phi'] = {
        'Phi_L_bits': s(phiL), 'Phi_G_bits': s(phiG), 'difference': s(phiL - phiG),
        'equal_below_1e-50': bool(abs(phiL - phiG) < TOL),
        'eight_positive_CMIs_under_G': {k: s(v) for k, v in eight_G},
        'eight_positive_CMIs_under_L': {k: s(v) for k, v in eight_L},
        'all_eight_nonneg_under_G': all(v >= -TOL for _, v in eight_G),
        'sum_eight_G_minus_Phi_G': s(sum8G - phiG), 'Phi_L_strictly_positive': bool(phiL > mp.mpf('1e-6')),
        'eight_sum_L_minus_2IPQ_L_minus_Phi_L': s(sum(v for _, v in eight_L) - 2 * ipq_L - phiL),
    }
    assert non_mixed_all_equal and term_entropy_equal and fact_G and not fact_L
    assert abs(idL) < TOL and abs(idG) < TOL and abs(phiL - phiG) < TOL and abs(sum8G - phiG) < TOL
    assert ipq_L > 0 and abs(ipq_G) < TOL and phiL > 0

    # (6) negative control Phi_bad
    L0 = {(0, 0, 0, 0, 0, 0): F(1, 2), (0, 0, 0, 0, 1, 1): F(1, 2)}
    H0 = all_entropies(L0)
    bad_rows = CMI[:-1] + [('P', 'Q', 'BCRH', -3)]
    # dense expansion of Phi_bad to show it has mixed coordinates
    dense = [0] * 64
    for a, b, z, w in bad_rows:
        A, Bm, Z = mask(a), mask(b), mask(z)
        for m, c in ((A | Z, 1), (Bm | Z, 1), (A | Bm | Z, -1), (Z, -1)):
            dense[m] += w * c
    bad_mixed = {m: dense[m] for m in range(64) if dense[m] and is_mixed(m)}
    phibad = lambda Hs: cmi_sum(Hs, bad_rows)
    out['sections']['6_negative_control_phi_bad'] = {
        'Phi_bad_definition': '8 positive CMIs - 3*I(P;Q|BCRH) = Phi - I(P;Q|BCRH)',
        'Phi_bad_nonzero_mixed_coordinates': bad_mixed,
        'law_L0': 'Y constant; P=Q uniform bit',
        'Phi_on_L0_bits': s(phi(H0)), 'Phi_bad_on_L0_bits': s(phibad(H0)),
        'Phi_bad_violated_on_L0': bool(phibad(H0) < -mp.mpf('0.5')),
        'Phi_bad_L_bits': s(phibad(HL)), 'Phi_bad_G_bits': s(phibad(HG)),
        'gluing_preserves_Phi_bad': bool(abs(phibad(HL) - phibad(HG)) < TOL),
    }
    assert abs(phi(H0)) < TOL and abs(phibad(H0) + 1) < TOL and bad_mixed
    assert not out['sections']['6_negative_control_phi_bad']['gluing_preserves_Phi_bad']

    # (7) conditioning control with Z
    L2 = structured_law(1)
    H2 = all_entropies(L2)
    pz = {0: F(1, 3), 1: F(2, 3)}
    LZ = {}
    for z, lawz in ((0, L), (1, L2)):
        for x, v in lawz.items():
            LZ[x + (z,)] = v * pz[z]
    assert sum(LZ.values()) == 1

    def marg7(law, m, with_z):
        o = {}
        for x, pr in law.items():
            key = tuple(x[i] if (m >> i) & 1 else None for i in range(6)) + ((x[6],) if with_z else (None,))
            o[key] = o.get(key, F(0)) + pr
        return o
    HSZ = [entropy(marg7(LZ, m, True)) for m in range(64)]
    phi_cond = sum(c * HSZ[mask(t)] for t, c in TERMS)
    avg = mp.mpf(pz[0].numerator) / pz[0].denominator * phi(HL) + mp.mpf(pz[1].numerator) / pz[1].denominator * phi(H2)
    out['sections']['7_conditioning_on_Z'] = {
        'coefficient_sum_of_Phi': sum(c for _, c in TERMS),
        'Phi_conditioned_sum_cS_H(S,Z)_bits': s(phi_cond), 'average_of_conditional_Phi_bits': s(avg),
        'difference': s(phi_cond - avg), 'equal_below_1e-50': bool(abs(phi_cond - avg) < TOL),
        'Phi_L2_bits': s(phi(H2)), 'conditioned_value_nonneg': bool(phi_cond >= -TOL),
    }
    assert abs(phi_cond - avg) < TOL and phi_cond >= 0

    # (8) random sweep
    rng = random.Random(122)
    T45 = mp.mpf('1e-45')
    stats = {'full_support': 0, 'sparse': 0, 'min_phi': None, 'max_identity_residual': mp.mpf(0),
             'max_glue_difference': mp.mpf(0), 'max_IPQ_under_glued': mp.mpf(0), 'phi_bad_negative_count': 0,
             'min_phi_bad': None}
    for k in range(300):
        sparse = (k % 3 == 2)
        law = random_law(rng, sparse)
        Hs = all_entropies(law)
        Hg = all_entropies(glue(law))
        p = phi(Hs)
        stats['min_phi'] = p if stats['min_phi'] is None else min(stats['min_phi'], p)
        stats['max_identity_residual'] = max(stats['max_identity_residual'], abs(p - cmi_sum(Hs)))
        stats['max_glue_difference'] = max(stats['max_glue_difference'], abs(p - phi(Hg)))
        stats['max_IPQ_under_glued'] = max(stats['max_IPQ_under_glued'], abs(cmi(Hg, 'P', 'Q', 'BCRH')))
        pb = phibad(Hs)
        stats['min_phi_bad'] = pb if stats['min_phi_bad'] is None else min(stats['min_phi_bad'], pb)
        stats['phi_bad_negative_count'] += int(pb < -T45)
        stats['sparse' if sparse else 'full_support'] += 1
        assert p >= -T45 and abs(p - cmi_sum(Hs)) < T45 and abs(p - phi(Hg)) < T45
    out['sections']['8_random_sweep'] = {k: (s(v) if isinstance(v, mp.mpf) else v) for k, v in stats.items()}
    out['sections']['8_random_sweep']['seed'] = 122
    out['sections']['8_random_sweep']['all_phi_nonneg_identity_and_gluing_within_1e-45'] = True

    out['verdict_of_this_script'] = 'ALL_CHECKS_PASSED'
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
