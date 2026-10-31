#!/usr/bin/env python3
"""F737 bounded exact finite checker; source prepared, NOT executed by author.

Parent must read this entire file, pin its bytes, and issue a fresh one-shot GO.
Run only as: python3 -I -B THIS_FILE
The controlling process must impose a 55 s external boundary.  This program's
cooperative limit is 42 s; its signal handlers only latch a stop request.
It reads no stdin/data files, starts no subprocess, and writes only one JSON
object to stdout.  Integer arithmetic only.  Finite checks are NOT a proof.

Encoding: 0,1,2,3 are (0,0),(1,0),(0,1),(1,1).  Full point and
frequency indices are (ell<<5)|(h_or_s<<4)|(i_or_beta<<2)|b_or_alpha.
The candidate's A4 has s1=0 in the assembled all-anchor equality pass; its
other seven odd F tables and s1=1 are NOT globally assembled.  Each one-row
physical A4 identity is nevertheless checked for both values of F and s1.
All distinct-kappa structural A0 checks use one defined physical ell=0 array,
not an exhaustive ell=0 search.  F725 and S6 are conditional input bodies, not
independently accepted proofs.  The original packet lacked the H_local
definition; the subsequently recovered definition is not tested here.
"""

import itertools
import json
import math
import signal
import sys
import time

START = time.monotonic()
DEADLINE = START + 42.0
STOP_REQUEST = None
PHASE = 'initialization'
COUNTS = {
    'local_physical_row_forms': 0,
    'local_A4_entries': 0,
    'domain_anchor_arrays': 0,
    'domain_anchor_kappa_tuples': 0,
    'domain_by_xor_v': {},
    'domain_by_multiplicity': {},
    'domain_tau_by_v_and_value': {},
    'repeated_kappa_arbitrary_w_cases': 0,
    'repeated_alpha_tests_by_multiplicity': {},
    'equality_physical_cases': 0,
    'equality_A4_frequency_comparisons': 0,
    'equality_full_paired_frequency_comparisons': 0,
    'equality_even_slice_E4_cases': 0,
    'distinct_kappa_equality_cases': 0,
    'distinct_aligned_character_frequency_comparisons': 0,
    'distinct_cap_implication_comparisons': 0,
    'distinct_A0_interface_anchor_beta_pairs': 0,
    'physical_fixture_transports': {},
    'intended_reason_controls': {},
}
DETAILS = {}
INPUTS = {
    'manifest_sha256': 'a938627746c54414b6da3fcab50da56264078ee217eb59e624e1e2a98dc3d996',
    'literal_packet_sha256': 'dfb064b343667081a530c794969050967e732883c5adbfbf185e899e6d9c2087',
    'packet_source_pins_parent_supplied': {
        'S1': 'a1eb0a70820eb9105a043fc22da1bcf9830b5daaa852fdcc5e84244d4d50b894',
        'S2': '63cc4fa48e0dececec9a381b32ca75191eec31e22e2cb3fb4907d7275437e890',
        'S3': 'a7deb23a7bf26185d8f9b3cb54c0fe79716bcbac739011ec59453f062cdd18d7',
        'S4': 'fa3b4e334713a4981b267e12be567d2f328ca00203fb525a45100bd1deae2d4a',
        'S5': '44970bbeb7af72f28d871c9c57eeff550707a62d40784deeee07f1cfa627b13a',
        'S6': '3e77eebe5c885ae8b53e04b76f3de46594c5cca2e5647086122bf408fa7052b4',
        'S7': '2253ac97d0b148dfc96406235658b5712c47c6014aecf65befe26e8f20d700ab',
    },
}
NOT_TESTED = [
    'Any scientific execution by the author: this source is a proposal until the parent reads it and issues a new GO.',
    'A universal theorem by finite enumeration; universal arguments remain the separate written authors\' burden.',
    'Actual H_local=0 is not checked by this source; the original packet lacked its definition, recovered only in a later supplement.',
    'The original Boolean caller, source identity, selected T/rank restoration, V and global NL242 conclusion.',
    'Any all-U3-capped physical y; both explicit physical fixtures fail U3 at the carried t.',
    'All other actual x, graph f/R phases, D0 allocations, sign completions or the full 256-entry caller family.',
    'All real ell=0 arrays: rank-one, three-cell and cap interfaces use one packet-defined physical ell=0 fixture plus explicitly described controls.',
    'Full equality-array assembly for the other seven odd F tables or s1=1; both values are covered only in the local row identity.',
    'All U3 caps and residue hypotheses for every equality array: the physical ell=0 fixture is reused without claiming those hypotheses.',
    'Independent model family, human review, proof assistant/kernel verification, novelty or parent acceptance.',
]

# CH[a][b] = (-1)^(a dot b), with dot product in F2^2.
CH = tuple(tuple(1 if (a & b) in (0, 3) else -1 for b in range(4))
           for a in range(4))
CH64 = tuple(tuple(1 if bin(a & b).count('1') % 2 == 0 else -1
                   for b in range(64)) for a in range(64))


class CheckFailure(Exception):
    def __init__(self, reason, detail=None):
        self.reason = reason
        self.detail = detail
        super().__init__(reason)


class CooperativeStop(Exception):
    pass


def latch(signum, _frame):
    global STOP_REQUEST
    if STOP_REQUEST is None:
        STOP_REQUEST = int(signum)


def guard():
    if STOP_REQUEST is not None:
        raise CooperativeStop('signal_' + str(STOP_REQUEST))
    if time.monotonic() >= DEADLINE:
        raise CooperativeStop('cooperative_42_second_deadline')


def need(condition, reason, detail=None):
    if not condition:
        raise CheckFailure(reason, detail)


def inc(mapping, key, amount=1):
    key = str(key)
    mapping[key] = mapping.get(key, 0) + amount


def ix(ell, h, i, b):
    return (ell << 5) | (h << 4) | (i << 2) | b


def qswap(v):
    return ((v & 1) << 1) | ((v & 2) >> 1)


def xor4(values):
    return values[0] ^ values[1] ^ values[2] ^ values[3]


def walsh(values):
    """Unnormalized in-place butterfly on a copied power-of-two list."""
    out = list(values)
    width = 1
    while width < len(out):
        for start in range(0, len(out), 2 * width):
            for j in range(width):
                a = out[start + j]
                b = out[start + j + width]
                out[start + j] = a + b
                out[start + j + width] = a - b
        width *= 2
    return out


def direct64(values):
    return [sum(x * s for x, s in zip(values, CH64[k])) for k in range(64)]


def frow(i):
    return 1 if i == 3 else 0


def make_row(fbit, anchor, kappa, w, s1):
    """Eight actual h,b sites with the equality mate signs A3.

    w=sigma*(-1)^(s1*fbit), and s0=1+s1.  A row by itself need
    not satisfy the global n/tau parity; that is checked on assembly.
    """
    s0 = s1 ^ 1
    sigma = w * (-1 if (s1 and fbit) else 1)
    values = [0] * 8
    for b in range(4):
        g = sigma * CH[kappa][b]
        values[(fbit << 2) | b] = g
        if b != anchor:
            d = -(-1 if s0 else 1) * g
            values[((fbit ^ 1) << 2) | b] = 2 * d
    return values


def row_transform(values, s, alpha):
    return sum(values[(h << 2) | b] * (-1 if s and h else 1) * CH[alpha][b]
               for h in range(2) for b in range(4))


def formula_A4(anchors, kappas, w, alpha, beta, wrong_anchor_phase=False):
    total = 0
    for i in range(4):
        phase = CH[kappas[i] if wrong_anchor_phase else kappas[i] ^ alpha][anchors[i]]
        bracket = (12 if alpha == kappas[i] else 0) - 2 * phase
        total += CH[beta][i] * w[i] * bracket
    return total


def local_rows():
    cache = {}
    for fbit, anchor, kappa, signbit, s1 in itertools.product(
            range(2), range(4), range(4), range(2), range(2)):
        guard()
        w = -1 if signbit else 1
        row = make_row(fbit, anchor, kappa, w, s1)
        need(sum(x * x for x in row) == 16, 'ROW_ENERGY')
        for alpha in range(4):
            expected = w * ((12 if alpha == kappa else 0)
                            - 2 * CH[kappa ^ alpha][anchor])
            need(row_transform(row, s1, alpha) == expected,
                 'LOCAL_A4_ROW', [fbit, anchor, kappa, w, s1, alpha])
            COUNTS['local_A4_entries'] += 1
        COUNTS['local_physical_row_forms'] += 1
        if s1 == 0:
            transforms = tuple(tuple(row_transform(row, s, alpha)
                                     for alpha in range(4)) for s in range(2))
            cache[(fbit, anchor, kappa, w)] = (row, transforms)
    return cache


def physical_fixture(kind):
    """Exactly the fixed x_* or F725's b->b+j physical shear.

    The S6 Z4 point is selected from its explicitly allowed positions:
    (ell,h,i,b)=(0,0,0,1).  F725 specifies this same site explicitly.
    """
    xstar = [0] * 64
    a = [0] * 64
    g = [0] * 64
    for i in range(4):
        fi = frow(i)
        for b in range(4):
            rho = -1 if b != 3 else 1
            a[ix(1, fi, i, b)] = CH[i][b]
            g[ix(1, fi, i, b)] = rho
            g[ix(1, fi ^ 1, i, b)] = -2 * rho
            xstar[ix(1, fi, i, b)] = 1 if b == i else -1
        xstar[ix(1, fi ^ 1, i, 0)] = 2
        for h in range(2):
            g[ix(0, h, i, 0)] = 4 if i == 0 else -2
    for i, h, b, value in ((1, 1, 2, 2), (1, 1, 3, -2),
                            (2, 1, 1, -2), (2, 1, 3, 2),
                            (3, 0, 1, 2), (3, 0, 2, -2)):
        xstar[ix(0, h, i, b)] = value
    if kind == 'fixed':
        x = list(xstar)
    else:
        x = [xstar[ix(ell, h, i, b ^ i)]
             for ell in range(2) for h in range(2)
             for i in range(4) for b in range(4)]
    y = [0] * 64
    for i in range(4):
        fi = frow(i)
        anchor = 0 if kind == 'fixed' else i
        for b in range(4):
            p = ix(1, fi, i, b)
            y[p] = -a[p] * g[p] * x[p]
            if b != anchor:
                y[ix(1, fi ^ 1, i, b)] = 2
        for h in range(2):
            if i:
                y[ix(0, h, i, 0)] = -2 if kind == 'shear' and i == 1 and h == 0 else 2
            for b in range(1, 4):
                if x[ix(0, h, i, b)] != 0:
                    y[ix(0, h, i, b)] = 2
    need(y[ix(0, 0, 0, 1)] == 0, 'Z4_SITE_OVERLAP', kind)
    y[ix(0, 0, 0, 1)] = 4
    return x, y, a, g


def fixture_checks(kind):
    x, y, a, g = physical_fixture(kind)
    spectra = [walsh(z) for z in (x, y, a, g)]
    for name, z, transformed in zip(('x', 'y', 'a', 'g'), (x, y, a, g), spectra):
        need(transformed == direct64(z), 'FIXTURE_DIRECT_WALSH', [kind, name])
    xhat, yhat, ahat, ghat = spectra
    need(sum(v*v for v in x) == 56 and sum(v*v for v in y) == 128,
         'FIXTURE_ENERGY', kind)
    need(sum(v == 0 for v in y) == 23, 'FIXTURE_Y_ZERO_COUNT', kind)
    need(sum(v == 0 for v in xhat) == 8 and
         sum(v == 8 for v in xhat) == 28 and
         sum(v == -8 for v in xhat) == 28, 'FIXTURE_X_WALSH_CENSUS', kind)
    need(all(v % 8 == 4 for v in ahat + ghat + yhat), 'FIXTURE_RESIDUE', kind)
    expected_dc = 44 if kind == 'fixed' else 52
    need(yhat[0] == expected_dc, 'FIXTURE_U3_DC', kind)
    expected_k = (3, 0, 0, 3) if kind == 'fixed' else (3, 2, 1, 0)
    expected_sigma = (1, -1, -1, -1) if kind == 'fixed' else (1, 1, 1, 1)
    for i in range(4):
        for b in range(4):
            need(y[ix(1, frow(i), i, b)] == expected_sigma[i] * CH[expected_k[i]][b],
                 'FIXTURE_GRAPH_CHARACTER', [kind, i, b])
    for t in range(64):
        guard()
        xx = [x[c] * CH64[t][c] for c in range(64)]
        yy = [y[c] * CH64[t][c] for c in range(64)]
        need(walsh(xx) == [xhat[k ^ t] for k in range(64)], 'X_T_TRANSPORT', [kind, t])
        need(walsh(yy) == [yhat[k ^ t] for k in range(64)], 'Y_T_TRANSPORT', [kind, t])
        need(xhat[0] == 0 and yhat[0] == expected_dc, 'CARRIED_T_LABEL', [kind, t])
        support = 0
        nonzero_w0 = 0
        graph_w0 = [0] * 4
        off_w0 = {'F': 0, 'D0': 0, 'D3': 0, 'Z2': 0, 'Z4': 0, 'Z0': 0}
        for ell in range(2):
            for h in range(2):
                for i in range(4):
                    for b in range(4):
                        c = ix(ell, h, i, b)
                        for u1 in (-1, 1):
                            for u2 in (-1, 1):
                                numerator = xx[c] + 3*a[c]*u1 + g[c]*u2 + yy[c]*u1*u2
                                need(numerator % 4 == 0 and numerator // 4 in (-1, 0, 1),
                                     'FIXTURE_TERNARY_INVERSE', [kind, t, c, u1, u2])
                                value = numerator // 4
                                support += int(value != 0)
                                if u1 == 1 and u2 == 1 and value:
                                    nonzero_w0 += 1
                                    if ell == 1 and h == frow(i):
                                        graph_w0[b] += 1
                                    elif ell == 1:
                                        off_w0['D0' if yy[c] == 0 else 'D3'] += 1
                                    elif b == 0:
                                        off_w0['F' if i == 0 else 'D3'] += 1
                                    else:
                                        off_w0['Z' + str(abs(yy[c]))] += 1
        need(support == 116 and nonzero_w0 % 2 == 1, 'FIXTURE_SUPPORT_OR_J', [kind, t])
        if t == 0:
            expected_graph = [1, 2, 2, 4] if kind == 'fixed' else [4, 2, 2, 4]
            expected_off = {'F': 2, 'D0': 4 if kind == 'fixed' else 3,
                            'D3': 8 if kind == 'fixed' else 10,
                            'Z2': 3, 'Z4': 1, 'Z0': 0}
            need(graph_w0 == expected_graph and off_w0 == expected_off,
                 'FIXTURE_W0_CENSUS', [kind, graph_w0, off_w0])
            if kind == 'shear':
                need(nonzero_w0 == 31, 'SHEAR_J_COUNT')
            DETAILS[kind + '_t0'] = {
                'x_walsh_zeros_plus8_minus8': [8, 28, 28],
                'y_dc': yhat[0], 'support': support, 'w0_nonzeros': nonzero_w0,
                'w0_graph_by_b': graph_w0, 'w0_off_graph': off_w0,
            }
        COUNTS['physical_fixture_transports'][kind] = t + 1
    return x, y, a, g


def layout_reason(y0):
    z2 = [(h, i, b) for h in range(2) for i in range(4) for b in range(1, 4)
          if abs(y0[ix(0, h, i, b)]) == 2]
    z4 = [(h, i, b) for h in range(2) for i in range(4) for b in range(1, 4)
          if abs(y0[ix(0, h, i, b)]) == 4]
    if len(z2) != 6:
        return 'Z2_COUNT'
    cells = {}
    for h, i, _ in z2:
        cells[(h, i)] = cells.get((h, i), 0) + 1
    if any(v != 2 for v in cells.values()):
        return 'CELL_ARITY'
    if len(cells) != 3:
        return 'CELL_COUNT'
    if len(z4) != 1:
        return 'Z4_COUNT'
    for i in range(4):
        v0, v1 = y0[ix(0, 0, i, 0)], y0[ix(0, 1, i, 0)]
        if not ((v0 == v1 == 0) or (abs(v0) == abs(v1) == 2)):
            return 'E_ROW_FORM'
    return None


def occupied_cells(y0):
    return {(h, i) for h in range(2) for i in range(4) for b in range(1, 4)
            if abs(y0[ix(0, h, i, b)]) == 2}


def paired_cell_reason(y0):
    cells = occupied_cells(y0)
    if any((h ^ 1, i) not in cells for h, i in cells):
        return 'ODD_CELL_PARITY'
    return None


def paired_site_reason(y0):
    for h in range(2):
        for i in range(4):
            for b in range(1, 4):
                if abs(y0[ix(0, h, i, b)]) == 2 and abs(y0[ix(0, h ^ 1, i, b)]) != 2:
                    return 'UNPAIRED_SITE'
    return None


def spatial_B(y0, anchors):
    return [[sum(y0[ix(0, h, i, bprime ^ anchors[i])] for h in range(2))
             for bprime in range(4)] for i in range(4)]


def rank_reason(B, beta0):
    if any(B[i][b] != CH[beta0][i] * B[0][b]
           for i in range(4) for b in range(4)):
        return 'A0_NOT_RANK_ONE'
    return None


def support_reason(B, beta0):
    for alpha in range(4):
        for beta in range(4):
            if beta != beta0:
                value = sum(B[i][b] * CH[alpha][b] * CH[beta][i]
                            for i in range(4) for b in range(4))
                if value != 0:
                    return 'A0_FORBIDDEN_BETA'
    return None


def affine_columns(anchors):
    c = anchors[0]
    col0, col1 = anchors[1] ^ c, anchors[2] ^ c
    need(anchors[3] == c ^ col0 ^ col1, 'NONAFFINE_ANCHORS_IN_ALIGNMENT', anchors)
    return c, col0, col1


def transpose_apply(alpha, col0, col1):
    return int(CH[alpha][col0] == -1) | (int(CH[alpha][col1] == -1) << 1)


def shear_frequency_reason(values, anchors, omit_beta_shift=False, omit_phase=False):
    c, col0, col1 = affine_columns(anchors)
    # This is the actual pullback Y'(ell,h,i,b')=Y(ell,h,i,b'+b_i).
    shifted = [values[ix(ell, h, i, b ^ anchors[i])]
               for ell in range(2) for h in range(2)
               for i in range(4) for b in range(4)]
    original_hat, shifted_hat = walsh(values), walsh(shifted)
    for nu, s, beta, alpha in itertools.product(range(2), range(2), range(4), range(4)):
        oldbeta = beta if omit_beta_shift else beta ^ transpose_apply(alpha, col0, col1)
        phase = 1 if omit_phase else CH[alpha][c]
        predicted = phase * original_hat[ix(nu, s, oldbeta, alpha)]
        if shifted_hat[ix(nu, s, beta, alpha)] != predicted:
            return 'SHEAR_FREQUENCY_LABEL' if omit_beta_shift else 'SHEAR_FREQUENCY_PHASE'
    return None


def alignment_reason(row, fbit, anchor, s0):
    for b in range(4):
        g = row[(fbit << 2) | b]
        mate = row[((fbit ^ 1) << 2) | b]
        expected = 0 if b == anchor else -2 * (-1 if s0 else 1) * g
        if mate != expected:
            return 'MATE_ALIGNMENT'
    return None


def formula_reason(values, anchors, kappas, w, wrong=False):
    spectrum = walsh(values)
    for alpha in range(4):
        for beta in range(4):
            p = ix(0, 0, beta, alpha)
            actual_twice = spectrum[p] - spectrum[p | 32]
            expected_twice = 2 * formula_A4(anchors, kappas, w, alpha, beta, wrong)
            if actual_twice != expected_twice:
                return 'A4_ANCHOR_PHASE'
    return None


def kappa_domain_reason(anchors, kappas):
    if xor4(kappas) != qswap(xor4(anchors)):
        return 'KAPPA_XOR'
    return None


def actual_controls(y):
    y0 = y[:32]
    need(layout_reason(y0) is None, 'POSITIVE_LAYOUT')
    bad = list(y0)
    bad[ix(0, 1, 1, 2)] = 0
    need(layout_reason(bad) == 'Z2_COUNT', 'CONTROL_Z2_COUNT')
    COUNTS['intended_reason_controls']['removed_z2'] = 'Z2_COUNT'
    bad = list(y0)
    bad[ix(0, 1, 1, 2)] = 0
    bad[ix(0, 0, 1, 2)] = 2
    need(layout_reason(bad) == 'CELL_ARITY', 'CONTROL_CELL_ARITY')
    COUNTS['intended_reason_controls']['moved_z2'] = 'CELL_ARITY'
    paired = [0] * 32
    for h, i, b in itertools.product(range(2), (1, 2), (1, 2)):
        paired[ix(0, h, i, b)] = 2
    need(paired_cell_reason(paired) is None and paired_site_reason(paired) is None,
         'POSITIVE_PAIRED_CELLS')
    bad = list(paired)
    bad[ix(0, 1, 2, 1)] = 0
    need(paired_site_reason(bad) == 'UNPAIRED_SITE', 'CONTROL_UNPAIRED_SITE')
    COUNTS['intended_reason_controls']['removed_one_mate'] = 'UNPAIRED_SITE'
    bad[ix(0, 1, 2, 2)] = 0
    need(paired_cell_reason(bad) == 'ODD_CELL_PARITY', 'CONTROL_ODD_CELLS')
    COUNTS['intended_reason_controls']['removed_mate_cell'] = 'ODD_CELL_PARITY'
    need(paired_cell_reason(y0) == 'ODD_CELL_PARITY', 'ACTUAL_THREE_CELL_PARITY')
    base = [0] * 32
    for h in range(2):
        for i in range(4):
            base[ix(0, h, i, 0)] = 2
    B = spatial_B(base, (0, 0, 0, 0))
    need(rank_reason(B, 0) is None and support_reason(B, 0) is None,
         'POSITIVE_A0_RANK_AND_SUPPORT')
    bad = list(base)
    bad[ix(0, 1, 1, 0)] = -2
    Bbad = spatial_B(bad, (0, 0, 0, 0))
    need(rank_reason(Bbad, 0) == 'A0_NOT_RANK_ONE', 'CONTROL_A0_RANK')
    need(support_reason(Bbad, 0) == 'A0_FORBIDDEN_BETA', 'CONTROL_A0_SUPPORT')
    COUNTS['intended_reason_controls']['flipped_E_rank'] = 'A0_NOT_RANK_ONE'
    COUNTS['intended_reason_controls']['flipped_E_spectrum'] = 'A0_FORBIDDEN_BETA'
    need(shear_frequency_reason(y, (1, 0, 3, 2)) is None, 'POSITIVE_AFFINE_SHEAR')
    need(shear_frequency_reason(y, (1, 0, 3, 2), omit_beta_shift=True)
         == 'SHEAR_FREQUENCY_LABEL', 'CONTROL_SHEAR_LABEL')
    need(shear_frequency_reason(y, (1, 0, 3, 2), omit_phase=True)
         == 'SHEAR_FREQUENCY_PHASE', 'CONTROL_SHEAR_PHASE')
    COUNTS['intended_reason_controls']['omitted_shear_beta_shift'] = 'SHEAR_FREQUENCY_LABEL'
    COUNTS['intended_reason_controls']['omitted_affine_phase'] = 'SHEAR_FREQUENCY_PHASE'
    anchors, kappas, w = (0, 1, 0, 1), (0, 1, 2, 3), (1, 1, 1, 1)
    values = list(y0) + [0] * 32
    for i in range(4):
        row = make_row(frow(i), anchors[i], kappas[i], w[i], 0)
        for h in range(2):
            for b in range(4):
                values[ix(1, h, i, b)] = row[(h << 2) | b]
    need(formula_reason(values, anchors, kappas, w) is None, 'POSITIVE_A4')
    need(formula_reason(values, anchors, kappas, w, wrong=True) == 'A4_ANCHOR_PHASE',
         'CONTROL_A4_PHASE')
    COUNTS['intended_reason_controls']['omitted_alpha_anchor_phase'] = 'A4_ANCHOR_PHASE'
    row = make_row(0, 0, 0, 1, 0)
    need(alignment_reason(row, 0, 0, 1) is None, 'POSITIVE_MATE_ALIGNMENT')
    row[(1 << 2) | 1] *= -1
    need(alignment_reason(row, 0, 0, 1) == 'MATE_ALIGNMENT', 'CONTROL_MATE_ALIGNMENT')
    COUNTS['intended_reason_controls']['flipped_physical_mate'] = 'MATE_ALIGNMENT'
    domain_anchors = (0, 0, 0, 1)
    need(kappa_domain_reason(domain_anchors, (0, 0, 0, 2)) is None,
         'POSITIVE_KAPPA_XOR')
    need(kappa_domain_reason(domain_anchors, (0, 0, 0, 1)) == 'KAPPA_XOR',
         'CONTROL_QSWAP_DOMAIN')
    COUNTS['intended_reason_controls']['forgotten_Qswap_on_nonzero_v'] = 'KAPPA_XOR'


def check_A0_interface(y0, anchors, beta0):
    B = spatial_B(y0, anchors)
    support = support_reason(B, beta0)
    rank = rank_reason(B, beta0)
    need((support is None) == (rank is None), 'A0_SUPPORT_RANK_EQUIVALENCE',
         [anchors, beta0, support, rank])
    z2_rows = {i for h in range(2) for i in range(4) for b in range(1, 4)
               if abs(y0[ix(0, h, i, b)]) == 2}
    vacant = [i for i in range(4) if i not in z2_rows]
    need(bool(vacant), 'THREE_CELL_NO_VACANT_I', anchors)
    need(all(abs(value) in (0, 4) for value in B[vacant[0]]),
         'VACANT_I_NOT_0_OR_4', anchors)
    if rank is None:
        need(all(abs(value) in (0, 4) for row in B for value in row),
             'RANK_ONE_MAGNITUDE_PROPAGATION', anchors)
        need(paired_site_reason(y0) is None, 'RANK_ONE_UNPAIRED_SITE', anchors)
        need(paired_cell_reason(y0) is None, 'RANK_ONE_THREE_CELL_PARITY', anchors)
        raise CheckFailure('IMPOSSIBLE_THREE_CELL_RANK_ONE', [anchors, beta0])
    COUNTS['distinct_A0_interface_anchor_beta_pairs'] += 1


def expected_domain():
    """Derive, rather than guess, both admissible kappa-domain counts."""
    explicit = {v: [] for v in range(4)}
    for kappa in itertools.product(range(4), repeat=4):
        for v in range(4):
            if xor4(kappa) == qswap(v):
                explicit[v].append(kappa)
    for v in range(4):
        generated = {(a, b, c, a ^ b ^ c ^ qswap(v))
                     for a, b, c in itertools.product(range(4), repeat=3)}
        need(set(explicit[v]) == generated, 'INDEPENDENT_KAPPA_DOMAIN', v)
    anchor_per_v = 4 ** 3
    even_all_same = 4
    even_two_pair = math.comb(4, 2) * math.comb(4, 2)
    even_all_distinct = math.factorial(4)
    nonzero_three_one = 4 * 4
    nonzero_two_one_one = 4 ** 3 - nonzero_three_one
    derived = {
        '4': anchor_per_v * even_all_same,
        '2+2': anchor_per_v * even_two_pair,
        '1+1+1+1': anchor_per_v * even_all_distinct,
        '3+1': 3 * anchor_per_v * nonzero_three_one,
        '2+1+1': 3 * anchor_per_v * nonzero_two_one_one,
    }
    need(sum(derived.values()) == (4 ** 4) * (4 ** 3), 'DERIVED_DOMAIN_TOTAL')
    DETAILS['independently_derived_domain_expectation'] = {
        'anchors_per_v': anchor_per_v,
        'kappa_per_anchor': 4 ** 3,
        'multiplicity_counts': derived,
        'derivation': 'v=0: 4 all-same + C(4,2)^2 two-pair + 4! distinct; '
                      'v!=0: 4 choices repeated value * 4 singleton positions for 3+1; '
                      'remaining 4^3 have 2+1+1.',
    }
    return explicit, derived


def all_anchor_check(cache, y0):
    domains, derived_counts = expected_domain()
    ell0hat = walsh(y0)
    structural_seen = set()
    for anchors in itertools.product(range(4), repeat=4):
        guard()
        COUNTS['domain_anchor_arrays'] += 1
        v = xor4(anchors)
        for kappas in domains[v]:
            guard()
            need(kappa_domain_reason(anchors, kappas) is None, 'KAPPA_XOR', [anchors, kappas])
            multiplicities = [kappas.count(alpha) for alpha in range(4)]
            pattern = '+'.join(str(m) for m in sorted((m for m in multiplicities if m), reverse=True))
            taus = [(multiplicities[alpha] + int(CH[alpha][v] == -1)) % 2
                    for alpha in range(4)]
            need(len(set(taus)) == 1, 'TAU_NOT_CONSTANT', [anchors, kappas, taus])
            tau = taus[0]
            COUNTS['domain_anchor_kappa_tuples'] += 1
            inc(COUNTS['domain_by_xor_v'], v)
            inc(COUNTS['domain_by_multiplicity'], pattern)
            inc(COUNTS['domain_tau_by_v_and_value'], str(v) + ':' + str(tau))
            repeated = [(alpha, m) for alpha, m in enumerate(multiplicities) if m >= 2]
            anchor_kappa_parity = sum(CH[kappas[i]][anchors[i]] == -1 for i in range(4)) % 2
            for mask in range(16):
                if mask % 4 == 0:
                    guard()
                w = tuple(-1 if mask & (1 << i) else 1 for i in range(4))
                if repeated:
                    for alpha, m in repeated:
                        magnitudes = [abs(formula_A4(anchors, kappas, w, alpha, beta))
                                      for beta in range(4)]
                        lower = {2: 16, 3: 28, 4: 20}[m]
                        need(max(magnitudes) >= lower, 'REPEATED_KAPPA_BETA_MAGNITUDE',
                             [anchors, kappas, w, alpha, magnitudes])
                        inc(COUNTS['repeated_alpha_tests_by_multiplicity'], m)
                    COUNTS['repeated_kappa_arbitrary_w_cases'] += 1
                sign_parity = sum(1 for z in w if z == -1) % 2
                if (sign_parity ^ anchor_kappa_parity) != (1 ^ tau):
                    continue
                # Here s1=0, s0=1 and sigma=w. The product condition above is
                # independently checked again by counting all twelve actual signs.
                values = list(y0) + [0] * 32
                rows = []
                n = 0
                for i in range(4):
                    row, transforms = cache[(frow(i), anchors[i], kappas[i], w[i])]
                    rows.append(transforms)
                    for h in range(2):
                        for b in range(4):
                            value = row[(h << 2) | b]
                            values[ix(1, h, i, b)] = value
                            if h == (frow(i) ^ 1) and b != anchors[i] and value < 0:
                                n += 1
                need((n + tau) % 2 == 1, 'ACTUAL_MATE_PARITY',
                     [anchors, kappas, w, n, tau])
                fullhat = walsh(values)
                E = 0
                for s in range(2):
                    for alpha in range(4):
                        for beta in range(4):
                            pos = (s << 4) | (beta << 2) | alpha
                            a1 = sum(CH[beta][i] * rows[i][s][alpha] for i in range(4))
                            a0 = ell0hat[pos]
                            need(fullhat[pos] == a0 + a1 and fullhat[pos | 32] == a0 - a1,
                                 'FULL_PAIRED_FREQUENCY_LABEL', [anchors, kappas, w, s, alpha, beta])
                            need(a1 % 8 == 4 * ((n + s + tau) % 2),
                                 'A2_RESIDUE', [anchors, kappas, w, s, alpha, beta, a1])
                            COUNTS['equality_full_paired_frequency_comparisons'] += 2
                            if s == 0:
                                need(a1 == formula_A4(anchors, kappas, w, alpha, beta),
                                     'A4_PHYSICAL_ARRAY', [anchors, kappas, w, alpha, beta])
                                COUNTS['equality_A4_frequency_comparisons'] += 1
                            else:
                                need(a1 in (-8, 0, 8), 'EVEN_SLICE_RANGE', a1)
                                E += int(abs(a1) == 8)
                need(E == 4, 'PARTIAL_PARSEVAL_EQUALITY_E', [anchors, kappas, w, E])
                COUNTS['equality_even_slice_E4_cases'] += 1
                COUNTS['equality_physical_cases'] += 1
                if not repeated:
                    need(v == 0 and tau == 1, 'DISTINCT_KAPPA_NOT_AFFINE', [anchors, kappas])
                    c, col0, col1 = affine_columns(anchors)
                    wp = tuple(w[i] * CH[kappas[i]][anchors[i]] for i in range(4))
                    need(math.prod(wp) == 1, 'DISTINCT_ALIGNED_ROW_PRODUCT', [anchors, kappas, wp])
                    beta_candidates = [beta for beta in range(4)
                                       if len({wp[i] * CH[beta][i] for i in range(4)}) == 1]
                    need(len(beta_candidates) == 1, 'COMMON_CHARACTER_BETA0', [anchors, kappas, wp])
                    beta0 = beta_candidates[0]
                    key = (anchors, beta0)
                    if key not in structural_seen:
                        check_A0_interface(y0, anchors, beta0)
                        structural_seen.add(key)
                    for alpha in range(4):
                        for beta in range(4):
                            oldbeta = beta ^ transpose_apply(alpha, col0, col1)
                            pos = (oldbeta << 2) | alpha
                            a0p = CH[alpha][c] * ell0hat[pos]
                            a1p = CH[alpha][c] * ((fullhat[pos] - fullhat[pos | 32]) // 2)
                            expected_magnitude = 4 if beta == beta0 else 12
                            need(abs(a1p) == expected_magnitude, 'DISTINCT_BETA0_MAGNITUDE',
                                 [anchors, kappas, w, alpha, beta, beta0, a1p])
                            COUNTS['distinct_aligned_character_frequency_comparisons'] += 1
                            if beta != beta0:
                                capped = max(abs(a0p + a1p), abs(a0p - a1p)) <= 12
                                need(capped == (a0p == 0), 'DISTINCT_A0_CAP_INTERFACE',
                                     [anchors, kappas, w, alpha, beta, a0p, a1p])
                                COUNTS['distinct_cap_implication_comparisons'] += 1
                    COUNTS['distinct_kappa_equality_cases'] += 1
    need(COUNTS['domain_anchor_arrays'] == 4 ** 4, 'ANCHOR_COUNT')
    need(COUNTS['domain_anchor_kappa_tuples'] == 4 ** 7, 'ANCHOR_KAPPA_COUNT')
    need(COUNTS['domain_by_multiplicity'] == derived_counts, 'MULTIPLICITY_CENSUS',
         [COUNTS['domain_by_multiplicity'], derived_counts])
    need(all(COUNTS['domain_by_xor_v'].get(str(v)) == 4 ** 6 for v in range(4)),
         'ANCHOR_V_CENSUS')
    total = COUNTS['domain_anchor_kappa_tuples']
    distinct = COUNTS['domain_by_multiplicity']['1+1+1+1']
    need(COUNTS['repeated_kappa_arbitrary_w_cases'] == (total - distinct) * 16,
         'REPEATED_ARBITRARY_W_CENSUS')
    need(COUNTS['equality_physical_cases'] == total * 8, 'EQUALITY_PARITY_CENSUS')
    need(COUNTS['equality_A4_frequency_comparisons'] == total * 8 * 16, 'A4_CENSUS')
    need(COUNTS['equality_full_paired_frequency_comparisons'] == total * 8 * 64,
         'FULL_PAIRED_CENSUS')
    need(COUNTS['distinct_kappa_equality_cases'] == distinct * 8, 'DISTINCT_CENSUS')
    need(COUNTS['distinct_A0_interface_anchor_beta_pairs'] == 4 ** 3 * 4,
         'A0_STRUCTURAL_CENSUS')


def main():
    global PHASE
    PHASE = 'local_physical_rows'
    cache = local_rows()
    PHASE = 'defined_physical_fixtures'
    fixture_checks('fixed')
    _, y, _, _ = fixture_checks('shear')
    PHASE = 'reason_specific_physical_mutants'
    actual_controls(y)
    PHASE = 'all_anchors_and_allowed_kappas'
    all_anchor_check(cache, y[:32])
    PHASE = 'complete'


status = 'INCOMPLETE'
error = None
try:
    signal.signal(signal.SIGINT, latch)
    signal.signal(signal.SIGTERM, latch)
    guard()
    main()
    guard()
    status = 'PASS_FINITE_SCOPES_ONLY'
except CooperativeStop as exc:
    error = {'reason': str(exc), 'phase': PHASE}
except CheckFailure as exc:
    status = 'FAIL'
    error = {'reason': exc.reason, 'detail': exc.detail, 'phase': PHASE}
except Exception as exc:
    status = 'FAIL'
    error = {'reason': 'UNEXPECTED_EXCEPTION', 'type': type(exc).__name__,
             'message': str(exc), 'phase': PHASE}

receipt = {
    'status': status,
    'elapsed_seconds': round(time.monotonic() - START, 6),
    'cooperative_deadline_seconds': 42,
    'external_limit_seconds_required': 55,
    'phase_at_settlement': PHASE,
    'latched_signal': STOP_REQUEST,
    'error': error,
    'inputs': INPUTS,
    'coverage_counts_completed_before_settlement': COUNTS,
    'details': DETAILS,
    'coverage_definition': {
        'domain': 'all 4^4 actual anchor arrays, all 4^3 ordered kappa tuples per anchor with xor(kappa)=Q xor(anchor)',
        'repeated': 'all 16 arbitrary row-sign vectors for every repeated-kappa domain tuple; every repeated alpha and all 4 beta',
        'equality': 'for each domain tuple, all 8 parity-consistent row-sign vectors, F=(0,0,0,1), s1=0, s0=1; actual 32 physical ell=1 sites and one physical ell=0 array',
        'paired_frequency': 'for each equality array, independently direct h/b row sums versus full 64-site butterfly at both ell-frequency labels, both s and all alpha,beta',
        'distinct': 'every affine-anchor, all-distinct-kappa equality case; affine beta-frequency transport, unique beta0, +/-4 versus +/-12, cap-to-A0 implication, and one physical three-cell A0',
        'local_rows': 'all fbit, anchor, kappa, row signs and s1 individually; not all odd F tables jointly',
        'fixtures': 'packet S6 fixed x with an allowed actual Z4 site and packet S3 physical shear; all 64 t modulations and all 256 inverse entries per t',
        'controls': 'actual spatial/sign mutations and distinct named failure reasons; not separate counterexamples to the theorem',
    },
    'not_tested': NOT_TESTED,
    'interpretation': 'A completed finite pass corroborates only these exact interfaces; written proof, parent full-source read, GO and disposition remain separate.',
}
print(json.dumps(receipt, sort_keys=True, separators=(',', ':')))
sys.exit(0 if status == 'PASS_FINITE_SCOPES_ONLY' else (2 if status == 'INCOMPLETE' else 1))
