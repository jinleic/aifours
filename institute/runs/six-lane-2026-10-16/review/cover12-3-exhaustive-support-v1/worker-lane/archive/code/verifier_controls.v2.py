#!/usr/bin/env python3
"""verifier_controls.py -- positive, boundary and mutation controls for code/verify_cs.py (README 1.5).

Writes fixture certificates into OUTDIR (a fresh directory; it must not exist), runs verify_cs.py on each, and checks
that the verdict starts with the intended prefix. Nothing is deleted or overwritten.
Usage: verifier_controls.py CPRO1_TAB_FILE OUTDIR
"""
import json
import os
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))


def main(argv):
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    cpro1, out = argv[1], argv[2]
    os.makedirs(out)
    bits36 = open(cpro1).read().split()
    assert len(bits36) == 36 and set(bits36) <= {"0", "1"}
    good36 = "COVERING-SEQUENCE 12 3 36\n" + " ".join(bits36) + "\n"
    cases = [
        # (name, content, extra args, expected verdict prefix)
        ("n1_r0_L1_seq0_allone_uncovered", "COVERING-SEQUENCE 1 0 1\n0\n", [], "INVALID coverage"),
        ("n1_r0_L2_seq01", "COVERING-SEQUENCE 1 0 2\n0 1\n", [], "VALID"),
        ("n3_r0_debruijn_00010111", "COVERING-SEQUENCE 3 0 8\n0 0 0 1 0 1 1 1\n", [], "VALID"),
        ("n3_r0_not_debruijn_00010110", "COVERING-SEQUENCE 3 0 8\n0 0 0 1 0 1 1 0\n", [], "INVALID coverage"),
        ("n4_r1_L6_111000_chung_cooper_example", "COVERING-SEQUENCE 4 1 6\n1 1 1 0 0 0\n", [], "VALID"),
        ("n10_r4_L4_1100_wraps_repeatedly", "COVERING-SEQUENCE 10 4 4\n1 1 0 0\n", [], "VALID"),
        ("n10_r4_L5_11000_no_code", "COVERING-SEQUENCE 10 4 5\n1 1 0 0 0\n", [], "INVALID coverage"),
        ("cpro1_12_3_36", good36, [], "VALID"),
        ("cpro1_12_3_36_expect_ok", good36, ["--expect", "12", "3", "36"], "VALID"),
        ("cpro1_12_3_36_expect_L35", good36, ["--expect", "12", "3", "35"], "INVALID binding"),
        ("cpro1_as_R2", good36.replace("12 3 36", "12 2 36", 1), [], "INVALID coverage"),
        ("allzero_12_3_36", "COVERING-SEQUENCE 12 3 36\n" + " ".join(["0"] * 36) + "\n", [], "INVALID coverage"),
        ("header_leading_zero", good36.replace("12 3 36", "12 3 036", 1), [], "INVALID format: bad header"),
        ("header_L35_tokens36", good36.replace("12 3 36", "12 3 35", 1), [],
         "INVALID format: header says L = 35 but line 2 has 36 tokens"),
        ("truncated_35_tokens", "COVERING-SEQUENCE 12 3 36\n" + " ".join(bits36[:35]) + "\n", [],
         "INVALID format: header says L = 36 but line 2 has 35 tokens"),
        ("bad_token_2", good36[:-2] + "2\n", [], "INVALID format: a token is not 0 or 1"),
        ("tab_separated_raw_cpro1", "COVERING-SEQUENCE 12 3 36\n" + "\t".join(bits36) + "\n", [],
         "INVALID format: header says L = 36 but line 2 has 1 tokens"),
        ("missing_final_newline", good36[:-1], [], "INVALID format: missing final newline"),
        ("extra_line", good36 + "0\n", [], "INVALID format: expected exactly 2 lines"),
        ("crlf", good36.replace("\n", "\r\n"), [], "INVALID format: carriage return"),
        ("double_space_in_bits", "COVERING-SEQUENCE 12 3 36\n" + " ".join(bits36[:5]) + "  " + " ".join(bits36[5:]) +
         "\n", [], "INVALID format: header says L = 36 but line 2 has 37 tokens"),
        ("double_space_in_header", good36.replace("12 3 36", "12  3 36", 1), [], "INVALID format: bad header"),
    ]
    # single-bit flips of the CPro1 sequence: informational (a flip may or may not break coverage)
    results, ok = [], True
    for name, content, extra, want in cases:
        path = os.path.join(out, name + ".cs")
        with open(path, "x", newline="") as f:
            f.write(content)
        p = subprocess.run([sys.executable, os.path.join(CODE, "verify_cs.py"), path] + extra,
                           capture_output=True, text=True)
        verdict = p.stdout.strip().split("\n")[-1]
        good = verdict.startswith(want) and ((p.returncode == 0) == (want == "VALID"))
        ok &= good
        results.append({"case": name, "expected": want, "got": verdict, "rc": p.returncode, "as_intended": good})
        print(f"{'ok ' if good else 'BAD'} {name}: expected {want!r}, got {verdict!r}")
    flips = []
    for i in range(36):
        b = list(bits36)
        b[i] = "1" if b[i] == "0" else "0"
        path = os.path.join(out, f"cpro1_flip_{i:02d}.cs")
        with open(path, "x") as f:
            f.write("COVERING-SEQUENCE 12 3 36\n" + " ".join(b) + "\n")
        p = subprocess.run([sys.executable, os.path.join(CODE, "verify_cs.py"), path], capture_output=True, text=True)
        flips.append(p.stdout.strip().split("\n")[-1].split(":")[0])
    print("single-bit flips of CPro1 (informational):", {v: flips.count(v) for v in sorted(set(flips))})
    with open(os.path.join(out, "verifier-controls.json"), "x") as f:
        json.dump({"results": results, "cpro1_single_flip_verdicts": flips, "all_as_intended": ok}, f, indent=1)
        f.write("\n")
    print("VERIFIER-CONTROLS", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
