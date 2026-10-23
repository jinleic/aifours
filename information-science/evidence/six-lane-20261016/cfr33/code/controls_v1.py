#!/usr/bin/env python3
"""Intended-reason mutation controls for cfr_check_events.py (A), cfr_check_posdiff.py (B), dm_check.py (lane cfr33).

Usage: controls_v1.py OUTDIR   (OUTDIR must not exist; created with os.mkdir; files mode 'x')
For each base file: the unmodified base must PASS both checkers; each mutation must FAIL both checkers with
the stated reason substring. Results -> OUTDIR/results.json; exit 1 if any expectation is violated.
"""
import hashlib, json, os, subprocess, sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = os.path.join(LANE, "code", "cfr_check_events.py")
B = os.path.join(LANE, "code", "cfr_check_posdiff.py")
DMC = os.path.join(LANE, "code", "dm_check.py")


def rows_of(text):
    return [ln.split(" ") for ln in text[:-1].split("\n")]


def join(rows):
    return "".join(" ".join(r) + "\n" for r in rows)


def mutations(text, n):
    rows = rows_of(text)
    out = []
    # 1 row 1 replaced by row 0 rotated by 3 (p_1 - p_0 constant): provably not a CFR
    r = [list(x) for x in rows]; r[1] = r[0][3:] + r[0][:3]
    out.append(("row1_is_rotation_of_row0", join(r), "occurs in row", "difference map repeats"))
    # 2 duplicated symbol in row 2
    r = [list(x) for x in rows]; r[2][1] = r[2][0]
    out.append(("duplicate_symbol_row2", join(r), "not a permutation", "repeated"))
    # 3 out-of-range symbol
    r = [list(x) for x in rows]; r[0][5] = str(n)
    out.append(("symbol_equal_n_row0", join(r), "not a permutation", "out of range"))
    # 4 last row dropped
    out.append(("drop_last_row", join(rows[:-1]), "expected %d rows" % len(rows), "row count"))
    # 5 non-canonical token (leading zero) on a nonzero symbol
    r = [list(x) for x in rows]; k = next(i for i, t in enumerate(r[1]) if t != "0"); r[1][k] = "0" + r[1][k]
    out.append(("leading_zero_token", join(r), "non-canonical token", "leading zero"))
    # 6 trailing space on line 1
    t = join(rows); first = t.index("\n"); t = t[:first] + " " + t[first:]
    out.append(("trailing_space", t, "tokens, found", "fields, need"))
    # 7 CRLF line endings
    out.append(("crlf", join(rows).replace("\n", "\r\n"), "outside [0-9 space LF]", "not a decimal numeral"))
    # 8 missing final LF
    out.append(("no_final_lf", join(rows)[:-1], "does not end with LF", "missing final LF"))
    # 9 swap two symbols inside row 2 (report-only: validity of the result is decided by the checkers)
    r = [list(x) for x in rows]; r[2][3], r[2][7] = r[2][7], r[2][3]
    out.append(("swap_two_symbols_row2(report-only)", join(r), None, None))
    return out


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.returncode, p.stdout.strip().splitlines()[-1] if p.stdout.strip() else p.stderr.strip()


def main():
    outdir = sys.argv[1]
    os.mkdir(outdir)
    bases = [("kirtchakov-cfr-5-25", os.path.join(LANE, "controls", "kirtchakov-cfr-5-25.raw"), 5, 25),
             ("priorart-cfr-4-33", os.path.join(LANE, "prior-art", "cfr-4-33-from-sage-dm.raw"), 4, 33),
             ("priorart-cfr-5-33", os.path.join(LANE, "prior-art", "cfr-5-33-from-sage-dm.raw"), 5, 33)]
    results, ok = [], True
    for name, path, r, n in bases:
        text = open(path).read()
        for chk in (A, B):
            rc, last = run(["python3", chk, path, str(r), str(n)])
            good = rc == 0 and last.endswith("PASS")
            ok &= good
            results.append({"base": name, "case": "unmodified", "checker": os.path.basename(chk), "rc": rc, "last": last, "as_expected": good})
        for case, mtext, ra, rb in mutations(text, n):
            fp = os.path.join(outdir, "%s__%s.raw" % (name, case.split("(")[0]))
            with open(fp, "x", newline="") as fh:
                fh.write(mtext)
            for chk, reason in ((A, ra), (B, rb)):
                rc, last = run(["python3", chk, fp, str(r), str(n)])
                if reason is None:
                    good = True
                else:
                    good = rc == 1 and "FAIL" in last and reason in last
                ok &= good
                results.append({"base": name, "case": case, "file": os.path.basename(fp),
                                "sha256": hashlib.sha256(mtext.encode()).hexdigest(), "checker": os.path.basename(chk),
                                "rc": rc, "last": last, "expected_reason": reason, "as_expected": good})
    # DM controls
    dm = os.path.join(LANE, "prior-art", "sage-dm-33-6-1.dmraw")
    rc, last = run(["python3", DMC, dm, "6", "33"])
    good = rc == 0 and last == "DM PASS"; ok &= good
    results.append({"base": "sage-dm-33-6-1", "case": "unmodified", "checker": "dm_check.py", "rc": rc, "last": last, "as_expected": good})
    rows = rows_of(open(dm).read())
    r2 = [list(x) for x in rows]; r2[3][10] = str((int(r2[3][10]) + 1) % 33)
    fp = os.path.join(outdir, "sage-dm-33-6-1__entry_plus_one.dmraw")
    with open(fp, "x") as fh:
        fh.write(join(r2))
    rc, last = run(["python3", DMC, fp, "6", "33"])
    good = rc == 1 and "differences not all distinct" in last; ok &= good
    results.append({"base": "sage-dm-33-6-1", "case": "entry_plus_one(row3,col10)", "checker": "dm_check.py", "rc": rc, "last": last, "as_expected": good})
    with open(os.path.join(outdir, "results.json"), "x") as fh:
        json.dump({"all_as_expected": ok, "results": results}, fh, indent=1)
    print("ALL_AS_EXPECTED" if ok else "SOME_UNEXPECTED", len(results))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
