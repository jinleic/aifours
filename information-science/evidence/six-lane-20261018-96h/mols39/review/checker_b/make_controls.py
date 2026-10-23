#!/usr/bin/env python3
"""Generate the checker_b control set into ./controls (exclusive create only).

Usage: python3 -I -B make_controls.py

Every control matrix is produced from a closed formula.  The expected outcome of
every case -- exit status, verdict, and the exact failing row pairs, squares and
square pairs -- was derived by hand (algebra in the 'intended' texts and in
report.md) and is written verbatim to controls/expected.json.  This script neither
imports nor runs checker_b.py.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CONTROLS = os.path.join(HERE, 'controls')
P = 'controls/'


def linear(n, mults):
    """Rows D_a(x) = a*x mod n, one per multiplier a, columns x = 0..n-1."""
    return [[(a * x) % n for x in range(n)] for a in mults]


def text(rows):
    """One row per line, single spaces, LF line ends."""
    return ''.join(' '.join(str(v) for v in row) + '\n' for row in rows)


def copy(rows):
    return [list(r) for r in rows]


M7 = list(range(7))
M13 = [5, 0, 12, 1, 7, 3, 10]
P7 = linear(7, M7)
P13 = linear(13, M13)

# (i) one transposition inside one row: row 4 (a = 7) of P13, columns 2 and 9.
NEG_I = copy(P13)
NEG_I[4][2], NEG_I[4][9] = NEG_I[4][9], NEG_I[4][2]

# (ii-a) duplicated row: row 6 of P13 replaced by a copy of row 0.
NEG_IIA = copy(P13)
NEG_IIA[6] = list(P13[0])

# (ii-b) duplicated row: row 5 of P7 replaced by a copy of row 2.
NEG_IIB = copy(P7)
NEG_IIB[5] = list(P7[2])

# (iii) Z_9, k = 4, rows 0, x, 2x, 4x.
NEG_III = linear(9, [0, 1, 2, 4])

# (iv) malformed: the last row of P7 loses its last entry (6 integers instead of 7).
NEG_IV = copy(P7)
NEG_IV[6] = NEG_IV[6][:-1]

# extra malformed variants of P7
OUT_OF_RANGE = copy(P7)
OUT_OF_RANGE[3][4] = 7                   # the value n itself
BAD_BYTE = [[str(v) for v in r] for r in P7]
BAD_BYTE[2][3] = '-1'                    # '-' is not an allowed byte
LEAD_ZERO = [[str(v) for v in r] for r in P7]
LEAD_ZERO[1][1] = '01'                   # non-canonical decimal

# extra positive: P7 with CRLF line ends, space/TAB runs, leading/trailing blanks, blank lines
CRLF = '\r\n'
for idx, row in enumerate(P7):
    CRLF += '  ' + ' \t '.join(str(v) for v in row) + ' \r\n'
    if idx == 3:
        CRLF += '\t\r\n'
CRLF += '\r\n'

FILES = {
    'pos_z7_linear.txt': text(P7),
    'pos_z13_linear.txt': text(P13),
    'neg_i_z13_transposition.txt': text(NEG_I),
    'neg_ii_a_z13_dup_row0.txt': text(NEG_IIA),
    'neg_ii_b_z7_dup_rows_2_5.txt': text(NEG_IIB),
    'neg_iii_z9_k4.txt': text(NEG_III),
    'neg_iv_malformed_length.txt': text(NEG_IV),
    'pos_z39_k3_linear.txt': text(linear(39, [0, 1, 2])),
    'neg_z39_k7_linear.txt': text(linear(39, list(range(7)))),
    'pos_z7_crlf_blank.txt': CRLF,
    'mf_out_of_range.txt': text(OUT_OF_RANGE),
    'mf_bad_byte.txt': text(BAD_BYTE),
    'mf_leading_zero.txt': text(LEAD_ZERO),
    'mf_single_row.txt': text([P7[1]]),
}


def ok(n, k):
    return {'exit': 0, 'verdict': 'PASS', 'n': n, 'k': k,
            'dm_fail_pairs': [], 'latin_fail': {}, 'orth_fail_pairs': []}


def fail(n, k, dm, latin, orth):
    return {'exit': 1, 'verdict': 'FAIL', 'n': n, 'k': k,
            'dm_fail_pairs': dm, 'latin_fail': latin, 'orth_fail_pairs': orth}


def malformed(*reason_parts):
    return {'exit': 2, 'verdict': 'MALFORMED', 'reason_contains': list(reason_parts)}


CASES = [
    {'name': 'P1_pos_z7_linear', 'kind': 'required positive',
     'file': P + 'pos_z7_linear.txt', 'args': [P + 'pos_z7_linear.txt'],
     'intended': 'rows a*x mod 7, a = 0..6 in order (D_0 = 0): every multiplier difference a_i - a_j is '
                 'a non-zero element of the field Z_7, hence a unit, so every difference row is a '
                 'permutation of Z_7; the 6 squares L_t[c][g] = (t*c + g) mod 7 are 6 MOLS(7)',
     'expect': ok(7, 7)},
    {'name': 'P2_pos_z13_linear', 'kind': 'required positive',
     'file': P + 'pos_z13_linear.txt', 'args': [P + 'pos_z13_linear.txt'],
     'intended': 'rows a*x mod 13, a = (5,0,12,1,7,3,10), pairwise distinct mod the prime 13, so every '
                 'difference row is a permutation; D_0 = 5x is not the zero row, so the D_0 subtraction '
                 'of the bridge is exercised; squares L_t[c][g] = ((a_t - 5)c + g) mod 13: 6 MOLS(13)',
     'expect': ok(13, 7)},
    {'name': 'N1_i_z13_transposition', 'kind': 'required negative (i)',
     'file': P + 'neg_i_z13_transposition.txt', 'args': [P + 'neg_i_z13_transposition.txt'],
     'intended': 'P2 with the entries at columns 2 and 9 of row 4 (a = 7) swapped. For linear rows r, j the '
                 'swap removes the differences (a_r-a_j)c1, (a_r-a_j)c2 and adds a_r*c2-a_j*c1, a_r*c1-a_j*c2; '
                 'the difference row stays a permutation iff these sets coincide, i.e. iff a_r(c2-c1) = 0 or '
                 'a_j(c2-c1) = 0 mod 13, i.e. iff a_r = 0 or a_j = 0. With a_4 = 7 exactly the row pairs (4,j) '
                 'with a_j != 0 fail: (0,4),(2,4),(3,4),(4,5),(4,6); (1,4) survives (row 1 is the zero row). '
                 'Bridge: (0,4) -> all 13 columns of L_4 not Latin (its rows stay Latin); (2,4),(3,4),(4,5),(4,6) '
                 '-> those square pairs not orthogonal; L_1 stays orthogonal to L_4',
     'expect': fail(13, 7, [[0, 4], [2, 4], [3, 4], [4, 5], [4, 6]], {'4': [0, 13]},
                    [[2, 4], [3, 4], [4, 5], [4, 6]])},
    {'name': 'N2a_ii_z13_dup_row0', 'kind': 'required negative (ii), variant a',
     'file': P + 'neg_ii_a_z13_dup_row0.txt', 'args': [P + 'neg_ii_a_z13_dup_row0.txt'],
     'intended': 'P2 with row 6 replaced by a copy of row 0 (a = 5): row pair (0,6) has all 13 differences 0; '
                 'every other pair keeps a non-zero multiplier difference (5 - a_s for a_s in 0,12,1,7,3). '
                 'Bridge: L_6[c][g] = g, every column constant -> all 13 columns of L_6 not Latin (rows Latin); '
                 'no orthogonality failure, since L_6 is still orthogonal to L_1..L_5 in the distinct-pairs sense',
     'expect': fail(13, 7, [[0, 6]], {'6': [0, 13]}, [])},
    {'name': 'N2b_ii_z7_dup_rows_2_5', 'kind': 'required negative (ii), variant b',
     'file': P + 'neg_ii_b_z7_dup_rows_2_5.txt', 'args': [P + 'neg_ii_b_z7_dup_rows_2_5.txt'],
     'intended': 'P1 with row 5 replaced by a copy of row 2: row pair (2,5) has all 7 differences 0; every '
                 'other pair keeps a non-zero multiplier difference. Bridge: L_2 = L_5 (identical Latin '
                 'squares) -> square pair (2,5) not orthogonal; all six squares Latin',
     'expect': fail(7, 7, [[2, 5]], {}, [[2, 5]])},
    {'name': 'N3_iii_z9_k4', 'kind': 'required negative (iii)',
     'file': P + 'neg_iii_z9_k4.txt', 'args': [P + 'neg_iii_z9_k4.txt'],
     'intended': 'Z_9, k = 4, rows 0, x, 2x, 4x. Multiplier differences: 1, 2, 4 against row 0, 1 for rows '
                 '(1,2), 3 for rows (1,3), 2 for rows (2,3). The units of Z_9 are the residues prime to 3, so '
                 '2 is a unit (2*5 = 10 = 1 mod 9) and the only non-unit difference is 3: exactly row pair '
                 '(1,3) fails (3x takes only the values 0, 3, 6). Bridge: L_1, L_2, L_3 have column '
                 'multipliers 1, 2, 4 (units) -> all Latin; square pair (1,3) not orthogonal',
     'expect': fail(9, 4, [[1, 3]], {}, [[1, 3]])},
    {'name': 'N4_iv_malformed_length', 'kind': 'required negative (iv)',
     'file': P + 'neg_iv_malformed_length.txt', 'args': [P + 'neg_iv_malformed_length.txt'],
     'intended': 'P1 whose last line (line 7) has 6 integers instead of 7: violates "each line has exactly n '
                 'integers"; must be rejected as MALFORMED (exit 2) before any property is evaluated',
     'expect': malformed('line 7: expected 7 integers', 'found 6')},
    {'name': 'X1_pos_z39_k3_linear', 'kind': 'extra positive',
     'file': P + 'pos_z39_k3_linear.txt', 'args': [P + 'pos_z39_k3_linear.txt', '--n', '39', '--k', '3'],
     'intended': 'rows 0, x, 2x mod 39: multiplier differences 1, 2, 1 are prime to 39 -> 2 MOLS(39); '
                 'exercises the target order and the --n/--k guard on a pass',
     'expect': ok(39, 3)},
    {'name': 'X2_neg_z39_k7_linear', 'kind': 'extra negative',
     'file': P + 'neg_z39_k7_linear.txt', 'args': [P + 'neg_z39_k7_linear.txt', '--n', '39', '--k', '7'],
     'intended': 'rows a*x mod 39, a = 0..6, at the target shape 7 x 39. The multiplier difference j - i is a '
                 'unit mod 39 = 3*13 iff 3 does not divide it, so exactly the row pairs with j - i in {3, 6} '
                 'fail: (0,3),(0,6),(1,4),(2,5),(3,6). Bridge: L_3, L_6 (column multipliers 3, 6) have all 39 '
                 'columns not Latin; square pairs (1,4),(2,5),(3,6) not orthogonal',
     'expect': fail(39, 7, [[0, 3], [0, 6], [1, 4], [2, 5], [3, 6]], {'3': [0, 39], '6': [0, 39]},
                    [[1, 4], [2, 5], [3, 6]])},
    {'name': 'X3_pos_z7_crlf_blank', 'kind': 'extra positive',
     'file': P + 'pos_z7_crlf_blank.txt', 'args': [P + 'pos_z7_crlf_blank.txt'],
     'intended': 'the P1 matrix written with CRLF line ends, space/TAB runs, leading and trailing blanks and '
                 'three blank lines; the grammar accepts all of these and yields the same matrix -> PASS',
     'expect': ok(7, 7)},
    {'name': 'X4_dims_mismatch', 'kind': 'extra negative',
     'file': P + 'pos_z7_linear.txt', 'args': [P + 'pos_z7_linear.txt', '--n', '39', '--k', '7'],
     'intended': 'a valid 7-row DM over Z_7 must not pass when --n 39 --k 7 is required',
     'expect': malformed('dimension mismatch: input has n=7 but --n 39 was required')},
    {'name': 'X5_out_of_range', 'kind': 'extra negative',
     'file': P + 'mf_out_of_range.txt', 'args': [P + 'mf_out_of_range.txt'],
     'intended': 'line 4, column 4 holds 7 = n, outside [0, n)',
     'expect': malformed('line 4, column 4 (0-based): integer 7 not in [0, 7)')},
    {'name': 'X6_bad_byte', 'kind': 'extra negative',
     'file': P + 'mf_bad_byte.txt', 'args': [P + 'mf_bad_byte.txt'],
     'intended': "line 3 holds the token '-1'; '-' (0x2d) is not an allowed byte",
     'expect': malformed('disallowed byte 0x2d', '(line 3)')},
    {'name': 'X7_leading_zero', 'kind': 'extra negative',
     'file': P + 'mf_leading_zero.txt', 'args': [P + 'mf_leading_zero.txt'],
     'intended': "line 2, column 1 holds '01', a non-canonical decimal",
     'expect': malformed("line 2, column 1 (0-based): non-canonical integer token '01'")},
    {'name': 'X8_single_row', 'kind': 'extra negative',
     'file': P + 'mf_single_row.txt', 'args': [P + 'mf_single_row.txt'],
     'intended': 'one row defines no square; k >= 2 is required',
     'expect': malformed('need at least 2 non-empty lines (rows), found 1')},
    {'name': 'X9_missing_input', 'kind': 'extra negative',
     'file': None, 'args': [P + 'no_such_file.txt'],
     'intended': 'unreadable input path',
     'expect': malformed('cannot read input: FileNotFoundError')},
    {'name': 'X10_usage_no_args', 'kind': 'extra negative',
     'file': None, 'args': [],
     'intended': 'missing positional argument: the argparse error still yields one JSON line and exit 2',
     'expect': malformed('command line: the following arguments are required: dm')},
    {'name': 'X11_emit_pos_z13', 'kind': 'extra positive (--emit)',
     'file': P + 'pos_z13_linear.txt', 'args': [P + 'pos_z13_linear.txt', '--emit', '{OUT}/squares.txt'],
     'intended': '--emit writes the 6 squares of P2; the harness compares the file byte for byte with the '
                 'closed form L_t[c][g] = ((a_t - a_0)c + g) mod 13 in the documented layout',
     'expect': ok(13, 7),
     'post': {'emit_linear': {'path': '{OUT}/squares.txt', 'n': 13, 'mults': M13}}},
    {'name': 'X12_emit_existing_refused', 'kind': 'extra negative (--emit)',
     'file': P + 'pos_z7_linear.txt', 'args': [P + 'pos_z7_linear.txt', '--emit', '{OUT}/squares.txt'],
     'intended': 'exclusive create: an existing --emit target is refused with exit 3 and left byte-identical',
     'expect': {'exit': 3, 'verdict': 'ERROR', 'reason_contains': ['cannot create --emit file: FileExistsError']},
     'post': {'unchanged': '{OUT}/squares.txt'}},
]


def main():
    for case in CASES:
        if case['file'] is not None and case['file'][len(P):] not in FILES:
            raise SystemExit('case %s refers to an unknown control file' % case['name'])
    os.mkdir(CONTROLS)  # refuses to reuse an existing controls/ directory
    for name, body in FILES.items():
        with open(os.path.join(CONTROLS, name), 'xb') as fh:
            fh.write(body.encode('ascii'))
    with open(os.path.join(CONTROLS, 'expected.json'), 'x', encoding='ascii') as fh:
        json.dump({'cases': CASES}, fh, indent=1)
        fh.write('\n')
    print('wrote %d control files and expected.json (%d cases) into %s' % (len(FILES), len(CASES), CONTROLS))


if __name__ == '__main__':
    main()
