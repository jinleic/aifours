#!/usr/bin/env python3
"""checker_controls_v3.py -- lane btd14-28 copy of checker_controls_v2.py (btd12-20) with only the binding control
retargeted to BTD 14 28 8 3 14 7 6.  Positive and intended-reason mutation controls for code/verify_btd.py and
bin/btd_check (README 1.5).  Published designs are transcribed reproducibly from the pinned layout texts by line range (the layout
files' SHA-256 are checked first).  Writes fixture certificates into OUTDIR (fresh; must not exist) and a JSON
summary; nothing is deleted or overwritten.
Usage: checker_controls.py OUTDIR
"""
import hashlib
import json
import os
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(CODE)
SRC = os.path.join(LANE, "sources")

LAYOUTS = {
    "rosin-2501": ("parent-screen-rosin-2501.17725v1.layout.txt",
                   "b61496e34b267a4d73f260984b1c52a8c52b26e36570955b3b3bc44c1f64e794"),
    "rosin-2505": ("parent-screen-rosin-2505.23881v1.layout.txt",
                   "35e78fe64808cbf4fd4d920f76937206f3f39bcc7ef8949dcd7b851bbec82dad"),
    "francel-hurd": ("parent-screen-francel-hurd-2008.layout.txt",
                     "aab8e78e2162b15e4c4189c631ee932a45ca1c4f3cdb6282cb12b896edddfdc6"),
}
# (name, layout key, first line, last line (1-based, inclusive), drop leading tokens, params V B p1 p2 R K L)
PUBLISHED = [
    ("cpro1_2505_fig4_btd_16_22_9_1_11_8_5", "rosin-2505", 882, 897, 0, (16, 22, 9, 1, 11, 8, 5)),
    ("cpro1_2501_fig20_btd_12_16_4_4_12_9_8", "rosin-2501", 1027, 1038, 0, (12, 16, 4, 4, 12, 9, 8)),
    ("cpro1_2501_fig19_btd_14_21_6_3_12_8_6", "rosin-2501", 1006, 1019, 0, (14, 21, 6, 3, 12, 8, 6)),
    ("francel_hurd_fig2_btd_4_12_3_6_15_5_16", "francel-hurd", 72, 75, 1, (4, 12, 3, 6, 15, 5, 16)),
]


def cert(params, rows):
    return "BTD " + " ".join(map(str, params)) + "\n" + "".join(" ".join(map(str, r)) + "\n" for r in rows)


def transcribe(key, a, b, drop, params):
    fname, sha = LAYOUTS[key]
    data = open(os.path.join(SRC, fname), "rb").read()
    assert hashlib.sha256(data).hexdigest() == sha, f"layout SHA mismatch for {fname}"
    lines = data.decode("utf-8").split("\n")[a - 1:b]
    rows = []
    for ln in lines:
        toks = ln.split()[drop:]
        rows.append([int(t) for t in toks])
    V, B = params[0], params[1]
    assert len(rows) == V and all(len(r) == B for r in rows), f"transcription shape mismatch for {key} {a}-{b}"
    return rows


def run_both(path, extra_py=(), extra_c=()):
    p = subprocess.run([sys.executable, os.path.join(CODE, "verify_btd.py"), path] + list(extra_py),
                       capture_output=True, text=True)
    vpy = p.stdout.strip().split("\n")[-1] if p.stdout.strip() else ""
    c = subprocess.run([os.path.join(LANE, "bin", "btd_check"), path] + list(extra_c), capture_output=True, text=True)
    vc = c.stdout.strip()
    return (p.returncode, vpy), (c.returncode, vc)


def main(argv):
    if len(argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    out = argv[1]
    os.makedirs(out)
    cases = []
    tiny = [[2, 0, 1], [1, 2, 0], [0, 1, 2]]
    cases.append(("btd_3_3_1_1_3_3_2_rows_201_120_012", cert((3, 3, 1, 1, 3, 3, 2), tiny), "VALID"))
    pub = {}
    for name, key, a, b, drop, params in PUBLISHED:
        rows = transcribe(key, a, b, drop, params)
        pub[name] = (params, rows)
        cases.append((name, cert(params, rows), "VALID"))
    # duplicate-column positive: two copies of the tiny design side by side, BTD(3,6;2,2,6;6? no) -> take the
    # Francel-Hurd packed BTD(3;3;1,1,3;3;2) twice: BTD(3,6;2,2,6;3,4), which has repeated columns.
    dbl = [r + r for r in tiny]
    cases.append(("btd_3_6_2_2_6_3_4_doubled_repeated_columns", cert((3, 6, 2, 2, 6, 3, 4), dbl), "VALID"))
    # mutations of the 12x16 CPro1 design (rows 0..11, 16 columns)
    params, rows = pub["cpro1_2501_fig20_btd_12_16_4_4_12_9_8"]
    good = cert(params, rows)

    def mut(f):
        r = [list(x) for x in rows]
        f(r)
        return cert(params, r)

    def set3(r):
        r[0][0] = 3

    def one_to_two(r):
        j = r[0].index(1)
        r[0][j] = 2

    def move_in_row(r):
        # move a nonzero entry of row 0 to a zero position: row counts unchanged, two column sums change
        j1 = r[0].index(1)
        j0 = r[0].index(0)
        r[0][j1], r[0][j0] = 0, 1

    def swap_rows_entries(r):
        # swap two entries in one column between rows 0 and 1, and the same in another column in reverse:
        # row compositions and column sums are preserved, a pair product changes
        for j in range(16):
            for j2 in range(16):
                if j != j2 and r[0][j] != r[1][j] and r[0][j2] == r[1][j] and r[1][j2] == r[0][j]:
                    a, b = r[0][j], r[1][j]
                    r[0][j], r[1][j], r[0][j2], r[1][j2] = b, a, a, b
                    return
        raise AssertionError("no swap found")

    cases += [
        ("mut_entry_3", mut(set3), "INVALID range"),
        ("mut_one_to_two_row0", mut(one_to_two), "INVALID row-count"),
        ("mut_move_within_row0", mut(move_in_row), "INVALID column-sum"),
        ("mut_cross_swap_rows01", mut(swap_rows_entries), "INVALID pair-product"),
        ("mut_header_R_mismatch", good.replace("BTD 12 16 4 4 12 9 8", "BTD 12 16 4 4 13 9 8", 1), "INVALID header"),
        ("mut_header_leading_zero", good.replace("BTD 12 16", "BTD 012 16", 1), "INVALID format"),
        ("mut_missing_final_lf", good[:-1], "INVALID format"),
        ("mut_extra_line", good + "0\n", "INVALID format"),
        ("mut_crlf", good.replace("\n", "\r\n"), "INVALID format"),
        ("mut_double_space", good.replace(" ", "  ", 9), "INVALID format"),
        ("mut_dropped_row", "".join(good.split("\n", 2)[0:1]) + "\n" + good.split("\n", 2)[2], "INVALID format"),
        ("mut_tab_separated", good.split("\n", 1)[0] + "\n" + good.split("\n", 1)[1].replace(" ", "\t"),
         "INVALID format"),
    ]
    results, ok = [], True
    for name, content, want in cases:
        path = os.path.join(out, name + ".btd")
        with open(path, "x", newline="") as f:
            f.write(content)
        (rpy, vpy), (rc_, vc) = run_both(path)
        good_py = vpy.startswith(want) and ((rpy == 0) == (want == "VALID"))
        good_c = vc.startswith(want) and ((rc_ == 0) == (want == "VALID"))
        # the two checkers order their format checks differently; a format-vs-format agreement is enough there
        ok &= good_py and good_c
        results.append({"case": name, "expected": want, "python": vpy, "python_rc": rpy, "native": vc,
                        "native_rc": rc_, "as_intended": good_py and good_c,
                        "sha256": hashlib.sha256(content.encode()).hexdigest()})
        print(f"{'ok ' if good_py and good_c else 'BAD'} {name}: want {want!r}; py {vpy!r}; c {vc!r}")
    # binding controls
    path = os.path.join(out, "cpro1_2501_fig20_btd_12_16_4_4_12_9_8.btd")
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    for name, args_py, args_c, want in [
        ("bind_expect_ok", ["--expect", "12", "16", "4", "4", "12", "9", "8", "--sha256", sha],
         ["12", "16", "4", "4", "12", "9", "8"], "VALID"),
        ("bind_expect_target_params", ["--expect", "14", "28", "8", "3", "14", "7", "6"],
         ["14", "28", "8", "3", "14", "7", "6"], "INVALID binding"),
        ("bind_wrong_sha", ["--sha256", "0" * 64], None, "INVALID binding"),
    ]:
        (rpy, vpy), (rc_, vc) = run_both(path, args_py, args_c or [])
        good_py = vpy.startswith(want)
        good_c = True if args_c is None else vc.startswith(want)
        ok &= good_py and good_c
        results.append({"case": name, "expected": want, "python": vpy, "native": vc if args_c else None,
                        "as_intended": good_py and good_c})
        print(f"{'ok ' if good_py and good_c else 'BAD'} {name}: want {want!r}; py {vpy!r}; c {vc if args_c else '-'!r}")
    with open(os.path.join(out, "checker-controls.json"), "x") as f:
        json.dump({"verify_btd_sha256": hashlib.sha256(open(os.path.join(CODE, "verify_btd.py"), "rb").read()).hexdigest(),
                   "btd_check_c_sha256": hashlib.sha256(open(os.path.join(CODE, "btd_check.c"), "rb").read()).hexdigest(),
                   "btd_check_bin_sha256": hashlib.sha256(open(os.path.join(LANE, "bin", "btd_check"), "rb").read()).hexdigest(),
                   "controls_script_sha256": hashlib.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest(),
                   "results": results, "all_as_intended": ok}, f, indent=1)
        f.write("\n")
    print("CHECKER-CONTROLS", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
