#!/usr/bin/env python3
"""make_controls.py - build the route-C control set in ./controls (new files only).

Run once:  python3 -I -B make_controls.py
Creates controls/ (fails if it already exists), the control matrices and
controls/expected.json.  Positives are linear difference matrices
D_a(c) = a*c mod n (plus a row/column-shifted copy and a layout variant); every
negative is an explicit perturbation with an intended failure reason.  The
expectations were derived by hand (derivations in report.md); no checker is
imported or run here.
"""

import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CDIR = os.path.join(HERE, "controls")

POS1 = "pos1_z7_k7_linear.txt"
POS2 = "pos2_z13_k7_linear.txt"
POS3 = "pos3_z13_k7_shifted.txt"
POS4 = "pos4_z39_k3_linear.txt"
POS5 = "pos5_z7_k7_layout.txt"
NEG1 = "negi_z13_k7_swap.txt"
NEG2 = "negii_z13_k7_single_entry.txt"
NEG3 = "negiii_z9_k4_mult0124.txt"
NEGX = "negx_z39_k7_linear.txt"
MALA = "maliv_a_short_row.txt"
MALB = "maliv_b_out_of_range.txt"
MALC = "maliv_c_negative_token.txt"
MALD = "maliv_d_missing_line.txt"
MALE = "maliv_e_extra_line.txt"
MALF = "maliv_f_fullwidth_digit.txt"
ABSENT = "absent_never_created.txt"
RECEIPT = "@RUN@/receipt_P7.json"


def linear(n, multipliers):
    """Rows D_a(c) = a*c mod n, one row per multiplier a."""
    return [[(a * c) % n for c in range(n)] for a in multipliers]


def line(row, sep=" "):
    return sep.join(str(value) for value in row)


def file_bytes(lines, encoding="ascii"):
    return "".join(text + "\n" for text in lines).encode(encoding)


def replaced(row, index, token):
    tokens = [str(value) for value in row]
    tokens[index] = token
    return " ".join(tokens)


def args(n, k, name, *extra):
    return ["--n", str(n), "--k", str(k)] + list(extra) + ["controls/" + name]


def well_formed(dm_pairs, dm_distinct, oa_pairs, oa_missing, bad_rows, cfr_pairs, triples, blank=0):
    state = "FAIL" if dm_pairs else "PASS"
    return {
        "exit": 1 if dm_pairs else 0,
        "verdict": state,
        "checks": {"cfr": state, "dm_definition": state, "oa_strength2": state},
        "dm_failing_row_pairs": dm_pairs,
        "dm_distinct_values": dm_distinct,
        "oa_failing_coordinate_pairs": oa_pairs,
        "oa_missing_pairs_values": oa_missing,
        "cfr_rows_not_permutation": bad_rows,
        "cfr_conflicting_row_pairs": cfr_pairs,
        "cfr_conflicting_triples": triples,
        "bridge_consistent": True,
        "blank_lines_ignored": blank,
    }


def passing(blank=0):
    return well_formed([], [], [], [], [], [], 0, blank)


def malformed(kind, line_number):
    return {"exit": 2, "verdict": "MALFORMED", "malformed_kind": kind, "malformed_line": line_number}


def refused(verdict):
    return {"exit": 2, "verdict": verdict}


def main():
    os.mkdir(CDIR)  # refuse to touch an existing control set
    z7 = linear(7, range(7))
    z13 = linear(13, range(7))
    # Row shifts r_i and column shifts s_c change D_i(c) - D_j(c) only by r_i - r_j.
    r = [5, 0, 7, 1, 12, 3, 9]
    s = [(3 * c * c + 1) % 13 for c in range(13)]
    shifted = [[(z13[i][c] + r[i] + s[c]) % 13 for c in range(13)] for i in range(7)]
    # POS1's matrix in a valid but irregular layout: CRLF line ends, two blank
    # lines, double spaces, tabs and no final newline.
    layout = ("\r\n" + line(z7[0], "  ") + "\r\n" + line(z7[1], "\t") + "\r\n" + " \t \r\n"
              + "\r\n".join(line(row) for row in z7[2:])).encode("ascii")
    swap = [row[:] for row in z13]
    swap[3][1], swap[3][2] = swap[3][2], swap[3][1]  # row 3 starts 0 3 6 -> 0 6 3
    single = [row[:] for row in z13]
    single[5][4] = (single[5][4] + 1) % 13  # D_5(4): 7 -> 8
    base = [line(row) for row in z13]
    files = {
        POS1: file_bytes(line(row) for row in z7),
        POS2: file_bytes(base),
        POS3: file_bytes(line(row) for row in shifted),
        POS4: file_bytes(line(row) for row in linear(39, range(3))),
        POS5: layout,
        NEG1: file_bytes(line(row) for row in swap),
        NEG2: file_bytes(line(row) for row in single),
        NEG3: file_bytes(line(row) for row in linear(9, [0, 1, 2, 4])),
        NEGX: file_bytes(line(row) for row in linear(39, range(7))),
        MALA: file_bytes(base[:2] + [line(z13[2][:-1])] + base[3:]),
        MALB: file_bytes(base[:3] + [replaced(z13[3], 4, "13")] + base[4:]),
        MALC: file_bytes(base[:1] + [replaced(z13[1], 1, "-1")] + base[2:]),
        MALD: file_bytes(base[:6]),
        MALE: file_bytes(base + [base[6]]),
        MALF: file_bytes(base[:4] + [replaced(z13[4], 2, "\uff13")] + base[5:], "utf-8"),
    }
    sha = {}
    for name in sorted(files):
        with open(os.path.join(CDIR, name), "xb") as handle:
            handle.write(files[name])
        sha[name] = hashlib.sha256(files[name]).hexdigest()

    def case(cid, cls, ref, argv, name, intended, expect, **extra):
        entry = {"id": cid, "class": cls, "task_ref": ref, "argv": argv, "file": "controls/" + name,
                 "sha256": sha.get(name), "intended": intended, "expect": expect}
        entry.update(extra)
        return entry

    cases = [
        case("P1", "positive", "positive Z_7", args(7, 7, POS1), POS1,
             "linear (Z_7,7;1) DM D_a(c)=a*c mod 7, a=0..6; every difference a-b is a unit mod 7",
             passing()),
        case("P2", "positive", "positive Z_13", args(13, 7, POS2), POS2,
             "linear (Z_13,7;1) DM D_a(c)=a*c mod 13, a=0..6",
             passing()),
        case("P3", "positive", "extra", args(13, 7, POS3), POS3,
             "P2 plus row shifts r=(5,0,7,1,12,3,9) and column shifts s_c=3c^2+1 mod 13: differences move by "
             "r_i-r_j only, so still a DM, while D_0 is neither zero nor a permutation (no normalisation assumed)",
             passing()),
        case("P4", "positive", "extra", args(39, 3, POS4), POS4,
             "linear (Z_39,3;1) DM, a=0,1,2 (two MOLS of order 39; exercises the n=39 grammar)",
             passing()),
        case("P5", "positive", "extra", args(7, 7, POS5), POS5,
             "P1 in a valid irregular layout: CRLF, blank first line, whitespace-only line, double spaces, tabs, "
             "no final newline; blank_lines_ignored must be 2",
             passing(2)),
        case("P6", "positive", "extra", args(13, 7, POS2, "--sha256", sha[POS2]), POS2,
             "P2 with the correct --sha256",
             passing()),
        case("P7", "positive", "extra", args(7, 7, POS1, "--output", RECEIPT), POS1,
             "P1 with --output: the receipt must equal the stdout line byte for byte",
             passing(), receipt=RECEIPT, receipt_matches="P7"),
        case("N1", "negative", "(i)", args(13, 7, NEG1), NEG1,
             "P2 with the entries D_3(1)=3 and D_3(2)=6 swapped: D_3 stays a permutation, so DM pair (0,3) "
             "survives, but D_3-D_j gets two collisions for j=1,2,4,5,6: L_3 stays Latin and is not orthogonal "
             "to L_1,L_2,L_4,L_5,L_6; CFR row 3 conflicts with rows 1,2,4,5,6",
             well_formed([[1, 3], [2, 3], [3, 4], [3, 5], [3, 6]], [11],
                         [[2, 4], [3, 4], [4, 5], [4, 6], [4, 7]], [26],
                         [], [[1, 3], [2, 3], [3, 4], [3, 5], [3, 6]], 20)),
        case("N2", "negative", "(ii)", args(13, 7, NEG2), NEG2,
             "P2 with the single entry D_5(4) changed 7 -> 8: every difference D_5-D_j (j != 5) gets one "
             "collision; L_5 is not column-Latin and not orthogonal to the other five squares; CFR row 5 is "
             "not a permutation",
             well_formed([[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [5, 6]], [12],
                         [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 7]], [13],
                         [5], [], 0)),
        case("N3", "negative", "(iii)", args(9, 4, NEG3), NEG3,
             "rows 0, x, 2x, 4x over Z_9 (k=4): D_3-D_1 = 3x is not a bijection because 3 is a zero divisor "
             "mod 9; the other differences x, 2x, 4x, x, 2x are bijections; L_1 and L_3 are Latin but not "
             "orthogonal",
             well_formed([[1, 3]], [3], [[2, 4]], [54], [], [[1, 3]], 18)),
        case("N4", "negative", "extra", args(39, 7, NEGX), NEGX,
             "target shape n=39, k=7, linear multipliers 0..6: pairs whose multiplier difference is 3 or 6 "
             "(gcd 3 with 39) fail: (0,3),(0,6),(1,4),(2,5),(3,6); CFR rows 3 and 6 are not permutations; "
             "rows 1/4 and 2/5 conflict",
             well_formed([[0, 3], [0, 6], [1, 4], [2, 5], [3, 6]], [13],
                         [[1, 4], [1, 7], [2, 5], [3, 6], [4, 7]], [1014],
                         [3, 6], [[1, 4], [2, 5]], 156)),
        case("M1", "malformed", "(iv)", args(13, 7, MALA), MALA,
             "line 3 holds 12 integers -> TOKEN_COUNT at line 3",
             malformed("TOKEN_COUNT", 3)),
        case("M2", "malformed", "(iv)", args(13, 7, MALB), MALB,
             "line 4 token 5 is 13 = n -> OUT_OF_RANGE at line 4",
             malformed("OUT_OF_RANGE", 4)),
        case("M3", "malformed", "(iv)", args(13, 7, MALC), MALC,
             "line 2 token 2 is -1 -> NOT_INTEGER at line 2",
             malformed("NOT_INTEGER", 2)),
        case("M4", "malformed", "(iv)", args(13, 7, MALD), MALD,
             "6 non-empty lines for k=7 -> LINE_COUNT",
             malformed("LINE_COUNT", None)),
        case("M5", "malformed", "(iv)", args(13, 7, MALE), MALE,
             "8 non-empty lines for k=7 -> LINE_COUNT",
             malformed("LINE_COUNT", None)),
        case("M6", "malformed", "(iv)", args(13, 7, MALF), MALF,
             "line 5 token 3 is U+FF13 FULLWIDTH DIGIT THREE in UTF-8 (Python int() would read it as 3) "
             "-> NON_ASCII",
             malformed("NON_ASCII", None)),
        case("M7", "malformed", "(iv)", args(13, 7, POS1), POS1,
             "P1 (n=7) checked with --n 13 --k 7: a wrong declared order is rejected as malformed, not "
             "evaluated -> TOKEN_COUNT at line 1",
             malformed("TOKEN_COUNT", 1)),
        case("M8", "malformed", "(iv)", args(13, 7, ABSENT), ABSENT,
             "input file does not exist -> UNREADABLE",
             malformed("UNREADABLE", None), absent=True),
        case("M9", "cli", "extra", ["--n", "13", "controls/" + POS2], POS2,
             "command line without --k -> USAGE_ERROR",
             refused("USAGE_ERROR")),
        case("M10", "cli", "extra", args(13, 7, POS2, "--sha256", "0" * 64), POS2,
             "P2 with a wrong --sha256 (64 zeros) -> SHA256_MISMATCH; the matrix is not evaluated",
             refused("SHA256_MISMATCH")),
        case("M11", "cli", "extra", args(7, 7, POS1, "--output", RECEIPT), POS1,
             "P7 repeated with the same --output path -> USAGE_ERROR (refuses to overwrite); the receipt must "
             "still equal the stdout of P7",
             refused("USAGE_ERROR"), receipt=RECEIPT, receipt_matches="P7"),
    ]
    doc = {"generator": "make_controls.py", "cases": cases}
    with open(os.path.join(CDIR, "expected.json"), "x", encoding="ascii") as handle:
        handle.write(json.dumps(doc, indent=1, sort_keys=True) + "\n")
    for name in sorted(sha):
        print(sha[name], "controls/" + name)
    print(len(cases), "cases -> controls/expected.json")


if __name__ == "__main__":
    main()
