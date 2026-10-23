#!/usr/bin/env python3
"""Checker controls for lane sw25-16: positives and intended-reason negatives, run through BOTH checkers.

Usage (lane root): python3 -B code/checker_controls.py OUTDIR
Creates OUTDIR (must not exist), writes every control file (mode x) and OUTDIR/checker-controls.json.
Pass = every positive VALID for both checkers; every negative INVALID with the intended primary reason and the
intended failing set, identical for both checkers.
"""
import hashlib
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sw_common as C  # noqa: E402

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run_checkers(path, n, w):
    py = subprocess.run([sys.executable, "-B", os.path.join(LANE, "code/verify_sw.py"), path, "--expect", str(n),
                         str(w)], capture_output=True, text=True)
    cc = subprocess.run([os.path.join(LANE, "bin/sw_check"), path, str(n), str(w)], capture_output=True, text=True)
    return py.returncode, py.stdout.strip(), cc.returncode, cc.stdout.strip()


def parse_result(line):
    if line.startswith("RESULT VALID"):
        return "VALID", "", ""
    parts = dict(p.split("=", 1) for p in line.split()[2:] if "=" in p)
    return "INVALID", parts.get("primary", "?"), parts.get("failing", "?")


def main():
    out = sys.argv[1]
    os.mkdir(out)
    cases = []

    def put(name, text, n, w, expect, primary="", failing=""):
        path = os.path.join(out, name)
        with open(path, "x", encoding="ascii", newline="") as f:
            f.write(text)
        cases.append((name, path, n, w, expect, primary, failing))

    sw23 = C.parse_magma(os.path.join(LANE, "sources/web/munemasa-SW-23-16.magma"))
    sw23d = C.parse_bracket(os.path.join(LANE, "sources/web/dinitz-W2316symmetric.txt"))
    w25 = C.parse_magma(os.path.join(LANE, "sources/web/munemasa-W-25-16.magma"))
    w25d = C.parse_bracket(os.path.join(LANE, "sources/web/dinitz-weighing2516.txt"))
    facts = {
        "munemasa_SW23_equals_dinitz_SW23": sw23 == sw23d,
        "munemasa_W25_equals_dinitz_W25": w25 == w25d,
        "munemasa_W25_is_weighing_16": C.is_weighing(w25, 16),
        "munemasa_W25_is_symmetric": all(w25[i][j] == w25[j][i] for i in range(25) for j in range(25)),
    }
    conf = {
        6: C.paley_conference(5, 1, (0,)),
        10: C.paley_conference(3, 2, (2, 0)),
        14: C.paley_conference(13, 1, (0,)),
        18: C.paley_conference(17, 1, (0,)),
        26: C.paley_conference(5, 2, (2, 0)),
    }
    # positives
    put("P-sw23-16-munemasa.sw", C.to_strict(sw23, 23, 16), 23, 16, "VALID")
    for q1, M in conf.items():
        put(f"P-paley-conference-{q1}.sw", C.to_strict(M, q1, q1 - 1), q1, q1 - 1, "VALID")
    put("P-sylvester-16.sw", C.to_strict(C.sylvester(4), 16, 16), 16, 16, "VALID")
    # intended-reason negatives
    put("N-posted-W25-16-asymmetric.sw", C.to_strict(w25, 25, 16), 25, 16, "INVALID", "SYMMETRY", "SYMMETRY")
    put("N-conference26-as-weight16.sw", C.to_strict(conf[26], 26, 16), 26, 16, "INVALID", "WEIGHT", "WEIGHT")
    # one symmetric off-diagonal nonzero pair sign-flipped
    i, j = next((i, j) for i in range(23) for j in range(i + 1, 23) if sw23[i][j] != 0)
    flip = [r[:] for r in sw23]
    flip[i][j] = -flip[i][j]
    flip[j][i] = -flip[j][i]
    put("N-sw23-signflip-one-pair.sw", C.to_strict(flip, 23, 16), 23, 16, "INVALID", "ORTHO", "ORTHO")
    two = [r[:] for r in sw23]
    two[i][j] = 2
    two[j][i] = 2
    put("N-sw23-entry-2.sw", C.to_strict(two, 23, 16), 23, 16, "INVALID", "ENTRIES", "ENTRIES,WEIGHT,ORTHO")
    # one diagonal entry flipped (if nonzero) -> ORTHO only
    d = next((k for k in range(23) if sw23[k][k] != 0), None)
    if d is not None:
        dg = [r[:] for r in sw23]
        dg[d][d] = -dg[d][d]
        put("N-sw23-diag-flip.sw", C.to_strict(dg, 23, 16), 23, 16, "INVALID", "ORTHO", "ORTHO")
    # zeroed symmetric pair -> WEIGHT and ORTHO
    z = [r[:] for r in sw23]
    z[i][j] = 0
    z[j][i] = 0
    put("N-sw23-zero-pair.sw", C.to_strict(z, 23, 16), 23, 16, "INVALID", "WEIGHT", "WEIGHT,ORTHO")
    base = C.to_strict(sw23, 23, 16)
    lines = base[:-1].split("\n")
    put("N-header-wrong-weight.sw", base, 23, 9, "INVALID", "HEADER", "HEADER")
    put("N-crlf.sw", base.replace("\n", "\r\n"), 23, 16, "INVALID", "FORMAT", "FORMAT")
    put("N-no-final-lf.sw", base[:-1], 23, 16, "INVALID", "FORMAT", "FORMAT")
    put("N-extra-blank-line.sw", base + "\n", 23, 16, "INVALID", "FORMAT", "FORMAT")
    put("N-tab-separator.sw", "\n".join([lines[0]] + [lines[1].replace(" ", "\t")] + lines[2:]) + "\n", 23, 16,
        "INVALID", "FORMAT", "FORMAT")
    put("N-trailing-space.sw", "\n".join([lines[0], lines[1] + " "] + lines[2:]) + "\n", 23, 16, "INVALID",
        "FORMAT", "FORMAT")
    put("N-missing-last-row.sw", "\n".join(lines[:-1]) + "\n", 23, 16, "INVALID", "FORMAT", "FORMAT")
    toks = lines[1].split(" ")
    k1 = toks.index("1")
    t2 = toks[:]
    t2[k1] = "+1"
    put("N-plus-token.sw", "\n".join([lines[0], " ".join(t2)] + lines[2:]) + "\n", 23, 16, "INVALID", "FORMAT",
        "FORMAT")
    k0 = toks.index("0")
    t3 = toks[:]
    t3[k0] = "-0"
    put("N-minus-zero-token.sw", "\n".join([lines[0], " ".join(t3)] + lines[2:]) + "\n", 23, 16, "INVALID",
        "FORMAT", "FORMAT")
    km = next(k for k, t in enumerate(toks) if t == "-1") if "-1" in toks else None
    if km is not None:
        t4 = toks[:]
        t4[km] = "\u22121"
        txt = "\n".join([lines[0], " ".join(t4)] + lines[2:]) + "\n"
        path = os.path.join(out, "N-unicode-minus.sw")
        with open(path, "xb") as f:
            f.write(txt.encode("utf-8"))
        cases.append(("N-unicode-minus.sw", path, 23, 16, "INVALID", "FORMAT", "FORMAT"))

    results = []
    ok_all = True
    for name, path, n, w, expect, primary, failing in cases:
        prc, pout, crc, cout = run_checkers(path, n, w)
        pv, pp, pf = parse_result(pout)
        cv, cp, cf = parse_result(cout)
        ok = (pv == cv == expect) and (pp == cp == primary) and (pf == cf == failing) and \
             ((prc == 0) == (expect == "VALID")) and ((crc == 0) == (expect == "VALID"))
        ok_all &= ok
        results.append({"case": name, "sha256": hashlib.sha256(open(path, "rb").read()).hexdigest(),
                        "n": n, "w": w, "expect": expect, "intended_primary": primary, "intended_failing": failing,
                        "verify_sw_py": pout, "sw_check_c": cout, "pass": ok})
        print(("PASS " if ok else "FAIL ") + name + " | " + pout + " | " + cout)
    rec = {"facts": facts, "cases": results, "all_pass": ok_all and all(facts[k] for k in facts if k !=
                                                                         "munemasa_W25_is_symmetric")
           and not facts["munemasa_W25_is_symmetric"],
           "checker_sha256": {p: hashlib.sha256(open(os.path.join(LANE, p), "rb").read()).hexdigest()
                              for p in ["code/verify_sw.py", "code/sw_check.c", "bin/sw_check", "code/sw_common.py",
                                        "code/checker_controls.py"]}}
    with open(os.path.join(out, "checker-controls.json"), "x") as f:
        json.dump(rec, f, indent=1)
        f.write("\n")
    print("facts", facts)
    print("CHECKER-CONTROLS", "PASS" if rec["all_pass"] else "FAIL", len(results), "cases")


if __name__ == "__main__":
    main()
