#!/usr/bin/env python3
"""proof-identity-and-witness-check-v1.py -- f122 reviewer-authored exact checker.

Independent (reviewer-written, structurally distinct from the author's checker)
verification of the six-variable gluing inequality Phi and its Shannon-cone witness.

What is checked (all exact integer / Fraction arithmetic):
  (A) Nine-CMI identity, expanded DENSELY over all 64 subset coordinates. The
      nine CMI rows and the sixteen written entropy terms are transcribed here
      from the markdown proof text (not from the witness JSON). Every one of the
      64 coordinates is compared; the nine mixed (P and Q) coordinates are
      reported with their individual contributions.
  (B) Cross-agreement: markdown 64-entry table == JSON values_by_subset_mask;
      markdown 16 terms == JSON inequality_coefficients_by_mask.
  (C) Witness is a polymatroid: r(empty)=0; FULL monotonicity (all 64 x 6
      (S, S+i) pairs); FULL submodularity (all 64 x 64 subset pairs, 4096
      checks). Separately the 246 elemental inequalities (6 + 15*2^4) are
      enumerated and counted as a cross-check of the author's count.
  (D) Exact value Phi(r) = -50548/6900000 = -12637/1725000 < 0, computed both
      from the 16-term vector and from the dense 64-coordinate CMI expansion.
  (E) Controls. Negative (must be REJECTED): wrong coefficient of the negative
      CMI (-1 and -3), three wrong conditioning sets, swapped variable roles,
      dropped positive row, wrong written coefficient; witness perturbations
      breaking r(empty)=0, monotonicity, and a tight submodular pair.
      Positive (must be ACCEPTED): row permutation, witness scaled by 2 (cone
      property), independent-uniform-bits polymatroid (Phi = 0).

No author code is imported or executed. The only author file read is the
witness JSON (data), and it is read only to compare against the independent
markdown transcription. Output is a JSON receipt printed to stdout.
"""
import json
import sys
from fractions import Fraction
from hashlib import sha256
from itertools import combinations
from pathlib import Path

BIT = {'B': 1, 'C': 2, 'R': 4, 'H': 8, 'P': 16, 'Q': 32}
FULL = 63
SCALE = 6900000


def mask(names):
    m = 0
    for ch in names:
        m |= BIT[ch]
    return m


# ---- (A) transcription from the markdown proof text -------------------------
# 16-term written inequality (markdown "Inequality and gluing proof" block)
MD_TERMS = [('BC', -1), ('BR', -1), ('BCRH', 2),
            ('BCP', 1), ('BRP', 1), ('BCRP', -1), ('BHP', -1), ('BCHP', 1), ('BCRHP', -1),
            ('BQ', -1), ('BCQ', 1), ('BRQ', 1), ('BHQ', 1), ('CHQ', -1), ('CRHQ', 1), ('BCRHQ', -2)]
# nine CMI rows (markdown "direct symbolic expansion" block): I(a;b|cond) with weight
MD_CMI = [('B', 'R', 'CHPQ', 1), ('C', 'R', 'BPQ', 1), ('C', 'Q', 'BHP', 1),
          ('R', 'P', 'CHQ', 1), ('H', 'P', 'BQ', 1), ('H', 'Q', 'BCRP', 1),
          ('P', 'Q', 'BR', 1), ('P', 'Q', 'BC', 1), ('P', 'Q', 'BCRH', -2)]
# 64-entry table transcribed from the markdown code block (rows 0-7 ... 56-63)
MD_TABLE = [
    0, 3875000, 6900000, 6900000, 3025000, 6900000, 8300000, 8300000,
    2975000, 5650000, 8300000, 8300000, 5675000, 8300000, 8300000, 8300000,
    6598260, 10309011, 11178976, 11178976, 8461329, 11329176, 12075000, 12075000,
    9420084, 12075000, 12075000, 12075000, 10057128, 12075000, 12075000, 12075000,
    3280188, 6928908, 9708504, 9708504, 5950419, 9585546, 10950000, 10950000,
    5682009, 8326158, 10950000, 10950000, 8331852, 10950000, 10950000, 10950000,
    7996200, 10825200, 11466900, 11466900, 9479700, 11577300, 12205200, 12205200,
    9969600, 12205200, 12205200, 12205200, 10549200, 12205200, 12205200, 12205200,
]
MD_CLAIMED_SCALED_VALUE = -50548


def dense_terms(terms):
    v = [0] * 64
    for names, c in terms:
        v[mask(names)] += c
    return v


def dense_cmi(rows):
    """Dense 64-vector of sum_w w*I(a;b|z) with I(a;b|z)=H(az)+H(bz)-H(abz)-H(z).
    H(empty) is coordinate 0 and is kept (it must end at 0 for any valid identity
    since r(empty)=0; we check it explicitly rather than silently dropping it)."""
    v = [0] * 64
    ledger = {}
    for a, b, z, w in rows:
        A, Bm, Z = mask(a), mask(b), mask(z)
        if A & Bm or A & Z or Bm & Z:
            raise ValueError(f'overlapping CMI arguments {a};{b}|{z}')
        for m, c in ((A | Z, 1), (Bm | Z, 1), (A | Bm | Z, -1), (Z, -1)):
            v[m] += w * c
            ledger.setdefault(m, []).append((f'I({a};{b}|{z})', w * c))
    return v, ledger


def identity_holds(rows, terms):
    lhs, ledger = dense_cmi(rows)
    rhs = dense_terms(terms)
    diff = {m: (lhs[m], rhs[m]) for m in range(64) if lhs[m] != rhs[m]}
    return (not diff), diff, lhs, ledger


def is_mixed(m):
    return bool(m & BIT['P']) and bool(m & BIT['Q'])


# ---- (C) polymatroid checks -------------------------------------------------
def polymatroid_full(r):
    """Full (non-elemental) check. Returns (ok, reason, stats)."""
    if len(r) != 64:
        return False, f'length {len(r)}', {}
    if r[0] != 0:
        return False, f'r(empty)={r[0]}', {}
    mono = sub = 0
    for S in range(64):
        for i in range(6):
            T = S | (1 << i)
            if r[T] < r[S]:
                return False, f'monotonicity S={S} i={i}', {}
            mono += 1
    for S in range(64):
        for T in range(64):
            if r[S] + r[T] < r[S | T] + r[S & T]:
                return False, f'submodularity S={S} T={T}', {}
            sub += 1
    return True, '', {'monotonicity_pairs': mono, 'submodularity_pairs': sub}


def elemental(r):
    """Enumerate the 246 elemental inequalities; return (count, n_tight, min_slack)."""
    count = 0
    tight = 0
    min_slack = None
    for i in range(6):
        s = r[FULL] - r[FULL ^ (1 << i)]
        if s < 0:
            raise ValueError('elemental monotonicity failed')
        count += 1
        tight += (s == 0)
        min_slack = s if min_slack is None else min(min_slack, s)
    for i, j in combinations(range(6), 2):
        a, b = 1 << i, 1 << j
        rest = [k for k in range(6) if k not in (i, j)]
        for bits in range(16):
            z = 0
            for t in range(4):
                if bits >> t & 1:
                    z |= 1 << rest[t]
            s = r[z | a] + r[z | b] - r[z | a | b] - r[z]
            if s < 0:
                raise ValueError('elemental submodularity failed')
            count += 1
            tight += (s == 0)
            min_slack = min(min_slack, s)
    return count, tight, min_slack


def phi_scaled(r, vec):
    return sum(c * r[m] for m, c in enumerate(vec) if c)


def main(argv):
    out = {'script': 'proof-identity-and-witness-check-v1.py', 'sections': {}}
    witness_path = Path(argv[1])
    raw = witness_path.read_bytes()
    out['witness_json_sha256'] = sha256(raw).hexdigest()
    out['witness_json_bytes'] = len(raw)
    doc = json.loads(raw)

    # (A) identity
    ok, diff, lhs, ledger = identity_holds(MD_CMI, MD_TERMS)
    mixed = {m: ledger.get(m, []) for m in range(64) if is_mixed(m) and m in ledger}
    out['sections']['A_identity'] = {
        'dense_64_coordinate_identity_holds': ok,
        'differing_coordinates': diff,
        'nonzero_coordinates_in_cmi_expansion': {m: lhs[m] for m in range(64) if lhs[m]},
        'count_nonzero': sum(1 for x in lhs if x),
        'empty_set_coordinate': lhs[0],
        'mixed_PQ_coordinates_touched_and_cancelled': {m: v for m, v in mixed.items()},
        'all_touched_mixed_cancel_to_zero': all(lhs[m] == 0 for m in mixed),
        'written_terms_contain_no_PQ_mixed_mask': all(not is_mixed(mask(n)) for n, _ in MD_TERMS),
        'coefficient_sum_of_written_terms': sum(c for _, c in MD_TERMS),
    }
    assert ok, diff

    # (B) cross-agreement markdown vs JSON
    md_vec = dense_terms(MD_TERMS)
    json_vec = [0] * 64
    for m, c in doc['inequality_coefficients_by_mask']:
        json_vec[int(m)] += int(c)
    out['sections']['B_markdown_vs_json'] = {
        'variable_order_json': doc['variable_order'],
        'scale_json': doc['scale'],
        'table_markdown_equals_json': MD_TABLE == [int(x) for x in doc['values_by_subset_mask']],
        'coefficients_markdown_equals_json': md_vec == json_vec,
        'json_scaled_value_field': doc['scaled_inequality_value'],
    }
    assert out['sections']['B_markdown_vs_json']['table_markdown_equals_json']
    assert out['sections']['B_markdown_vs_json']['coefficients_markdown_equals_json']
    assert doc['variable_order'] == list('BCRHPQ') and doc['scale'] == SCALE

    # (C) polymatroid
    r = MD_TABLE
    pok, preason, pstats = polymatroid_full(r)
    ecount, etight, emin = elemental(r)
    out['sections']['C_polymatroid'] = {
        'full_check_ok': pok, 'full_check_reason': preason, **pstats,
        'elemental_count': ecount, 'elemental_tight_at_witness': etight,
        'elemental_min_slack_scaled': emin,
        'all_values_nonnegative_integers': all(isinstance(x, int) and x >= 0 for x in r),
    }
    assert pok and ecount == 246

    # (D) exact value
    v16 = phi_scaled(r, md_vec)
    v64 = phi_scaled(r, lhs)
    val = Fraction(v16, SCALE)
    out['sections']['D_value'] = {
        'scaled_value_from_16_terms': v16,
        'scaled_value_from_dense_cmi_expansion': v64,
        'exact_value': f'{val.numerator}/{val.denominator}',
        'matches_markdown_claim_-50548': v16 == MD_CLAIMED_SCALED_VALUE,
        'matches_markdown_reduced_-12637/1725000': val == Fraction(-12637, 1725000),
        'negative': val < 0,
    }
    assert v16 == v64 == MD_CLAIMED_SCALED_VALUE

    # (E) controls
    ctrl = {}

    def neg_identity(tag, rows, terms):
        ok2, diff2, _, _ = identity_holds(rows, terms)
        ctrl[tag] = {'expected': 'REJECT', 'identity_holds': ok2,
                     'differing_coordinates': {k: v for k, v in sorted(diff2.items())}}
        assert not ok2, tag

    rows = list(MD_CMI)
    neg_identity('ID1_negative_coefficient_-1', rows[:-1] + [('P', 'Q', 'BCRH', -1)], MD_TERMS)
    neg_identity('ID2_negative_coefficient_-3', rows[:-1] + [('P', 'Q', 'BCRH', -3)], MD_TERMS)
    neg_identity('ID3_cond_row1_CHPQ_to_CHP', [('B', 'R', 'CHP', 1)] + rows[1:], MD_TERMS)
    neg_identity('ID4_cond_row7_BR_to_BH', rows[:6] + [('P', 'Q', 'BH', 1)] + rows[7:], MD_TERMS)
    neg_identity('ID5_cond_row9_BCRH_to_BCH', rows[:-1] + [('P', 'Q', 'BCH', -2)], MD_TERMS)
    neg_identity('ID6_swap_roles_row3_C;Q|BHP_to_C;P|BHQ', rows[:2] + [('C', 'P', 'BHQ', 1)] + rows[3:], MD_TERMS)
    neg_identity('ID7_drop_row4_R;P|CHQ', rows[:3] + rows[4:], MD_TERMS)
    neg_identity('ID8_written_coefficient_BCRHQ_-2_to_-1', rows, MD_TERMS[:-1] + [('BCRHQ', -1)])
    neg_identity('ID9_written_term_CHQ_to_BHQ_sign', rows, [t if t[0] != 'CHQ' else ('CHQ', 1) for t in MD_TERMS])
    # positive: permuted rows
    okp, _, _, _ = identity_holds(list(reversed(rows)), MD_TERMS)
    ctrl['ID10_permuted_rows'] = {'expected': 'ACCEPT', 'identity_holds': okp}
    assert okp

    # witness negative controls
    def neg_witness(tag, rr):
        ok3, reason3, _ = polymatroid_full(rr)
        ctrl[tag] = {'expected': 'REJECT', 'polymatroid': ok3, 'reason': reason3}
        assert not ok3, tag

    w = list(r); w[0] = 1
    neg_witness('W1_empty_set_value_1', w)
    w = list(r); w[63] -= 1
    neg_witness('W2_r63_minus_1_breaks_monotonicity', w)
    # find a tight elemental submodular pair and break it
    tight_pair = None
    for i, j in combinations(range(6), 2):
        a, b = 1 << i, 1 << j
        rest = [k for k in range(6) if k not in (i, j)]
        for bits in range(16):
            z = 0
            for t in range(4):
                if bits >> t & 1:
                    z |= 1 << rest[t]
            if r[z | a] + r[z | b] - r[z | a | b] - r[z] == 0:
                tight_pair = (a, b, z)
                break
        if tight_pair:
            break
    a, b, z = tight_pair
    w = list(r); w[z | a | b] += 1
    neg_witness(f'W3_tight_pair_a={a}_b={b}_z={z}_raise_union_by_1', w)
    w = list(r); w[z] += 1  # raising r(z) also breaks the tight pair (and maybe monotonicity)
    neg_witness(f'W4_tight_pair_raise_condition_z={z}_by_1', w)

    # witness positive controls
    w2 = [2 * x for x in r]
    ok4, _, _ = polymatroid_full(w2)
    ctrl['W5_scaled_by_2'] = {'expected': 'ACCEPT', 'polymatroid': ok4,
                              'scaled_value': phi_scaled(w2, md_vec),
                              'is_double': phi_scaled(w2, md_vec) == 2 * MD_CLAIMED_SCALED_VALUE}
    assert ok4 and ctrl['W5_scaled_by_2']['is_double']
    unif = [bin(S).count('1') * SCALE for S in range(64)]
    ok5, _, _ = polymatroid_full(unif)
    ctrl['W6_independent_uniform_bits'] = {'expected': 'ACCEPT_and_Phi_zero', 'polymatroid': ok5,
                                           'scaled_value': phi_scaled(unif, md_vec)}
    assert ok5 and ctrl['W6_independent_uniform_bits']['scaled_value'] == 0
    # coefficient flip sensitivity (value must change)
    flip = list(md_vec); flip[3] = +1
    ctrl['W7_flip_coefficient_mask3_value_changes'] = {'expected': 'VALUE_CHANGES',
                                                       'scaled_value': phi_scaled(r, flip),
                                                       'changed': phi_scaled(r, flip) != MD_CLAIMED_SCALED_VALUE}
    assert ctrl['W7_flip_coefficient_mask3_value_changes']['changed']
    out['sections']['E_controls'] = ctrl

    out['verdict_of_this_script'] = 'ALL_CHECKS_PASSED'
    print(json.dumps(out, indent=1, sort_keys=False))


if __name__ == '__main__':
    main(sys.argv)
