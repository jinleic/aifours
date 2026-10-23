#!/usr/bin/env python3
"""Build and run controls for verify_cpcw.py.
Positive fixtures: optimal codes transcribed from Baicheva-Topalova, Axioms 15(1) (2026) 35 (sources/axioms-15-00035.pdf):
Figure 1 (v=43) and Appendix A Tables A1 (k=5) and A2 (k=6).  The tables omit the element 0 of every codeword; it is
added here.  Mutations must be rejected for the intended check; validity-preserving changes must be accepted.
Writes controls/positive/*.txt, controls/negative/*.txt, controls/preserving/*.txt and controls/receipt.json."""
import hashlib
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(HERE)
VER = os.path.join(HERE, "verify_cpcw.py")

PUB = {  # (v,k): codewords WITHOUT 0, as printed
    (43, 5): [(1, 3, 7, 19), (5, 13, 22, 33)],                       # Figure 1 (printed with 0)
    (90, 5): [(1, 3, 7, 18), (5, 25, 33, 52), (13, 39, 53, 69), (9, 31, 55, 67)],
    (103, 5): [(1, 3, 15, 96), (9, 49, 65, 92), (4, 37, 50, 79), (6, 41, 58, 77), (5, 30, 64, 85)],
    (122, 5): [(1, 3, 21, 33), (10, 34, 93, 106), (8, 36, 76, 111), (6, 51, 58, 113), (4, 42, 85, 99), (5, 49, 74, 105)],
    (126, 5): [(1, 3, 25, 122), (6, 23, 85, 100), (8, 38, 75, 91), (11, 44, 72, 92), (12, 68, 86, 99), (9, 66, 80, 116)],
    (140, 5): [(1, 3, 7, 34), (9, 26, 78, 127), (8, 29, 43, 66), (10, 55, 83, 102), (5, 64, 89, 129), (12, 36, 80, 122)],
    (152, 5): [(1, 3, 10, 95), (11, 33, 110, 133), (8, 54, 91, 125), (6, 31, 72, 93), (5, 101, 114, 140),
               (4, 28, 44, 107), (14, 29, 84, 134)],
    (106, 6): [(1, 3, 7, 15, 36), (5, 45, 56, 65, 84), (10, 26, 44, 57, 74)],
    (120, 6): [(1, 3, 7, 12, 22), (8, 24, 51, 74, 92), (13, 33, 47, 78, 95)],
    (125, 6): [(1, 3, 19, 31, 54), (5, 47, 64, 93, 104), (7, 41, 50, 77, 110), (4, 67, 80, 105, 119)],
    (131, 6): [(1, 3, 23, 36, 105), (6, 65, 73, 97, 116), (9, 37, 54, 79, 93), (4, 11, 16, 57, 87)],
    (150, 6): [(1, 3, 7, 12, 45), (8, 39, 87, 124, 134), (13, 54, 69, 86, 136), (19, 49, 72, 107, 129)],
}


def render(v, k, code, header=None):
    return (header or "CPCW %d %d" % (v, k)) + "\n" + "".join(" ".join(map(str, cw)) + "\n" for cw in code)


def write(rel, text):
    path = os.path.join(LANE, "controls", rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as fh:
        fh.write(text)
    return path


def run(path, v, k, sha):
    p = subprocess.run([sys.executable, VER, path, "--v", str(v), "--k", str(k), "--sha256", sha],
                       capture_output=True, text=True)
    return p.returncode, json.loads(p.stdout) if p.stdout.strip() else {}


def main():
    rows, bad = [], 0
    for (v, k), cws in sorted(PUB.items()):
        code = [[0] + list(c) for c in cws]
        base = render(v, k, code)
        cases = [("positive/axioms_%d_%d.txt" % (v, k), base, v, k, None, "ACCEPT", None)]
        if (v, k) in [(90, 5), (122, 5), (152, 5), (106, 6), (150, 6)]:
            c = [list(x) for x in code]
            c[0][2] = next(y for y in range(c[0][2] + 1, c[0][2] + v) if y % v not in c[0]) % v
            cases.append(("negative/%d_%d_changed_element.txt" % (v, k), render(v, k, c), v, k, None, "REJECT", "D"))
            c = [list(x) for x in code]
            c[0][1], c[1][1] = c[1][1], c[0][1]
            cases.append(("negative/%d_%d_swapped_elements.txt" % (v, k), render(v, k, c), v, k, None, "REJECT", "D"))
            c = [list(x) for x in code]
            c[1] = [(x + 1) % v for x in c[0]]
            cases.append(("negative/%d_%d_duplicated_difference.txt" % (v, k), render(v, k, c), v, k, None, "REJECT", "D"))
            if v % 2 == 0:
                c = [list(x) for x in code]
                c[0][-1] = (c[0][0] + v // 2) % v
                cases.append(("negative/%d_%d_half_v.txt" % (v, k), render(v, k, c), v, k, None, "REJECT", "D"))
            cases.append(("negative/%d_%d_cli_wrong_v.txt" % (v, k), base, v + 1, k, None, "REJECT", "F"))
            cases.append(("negative/%d_%d_cli_wrong_k.txt" % (v, k), base, v, k + 1, None, "REJECT", "F"))
            cases.append(("negative/%d_%d_header_wrong_v.txt" % (v, k), render(v, k, code, "CPCW %d %d" % (v + 1, k)), v, k, None, "REJECT", "F"))
            cases.append(("negative/%d_%d_sha_mismatch.txt" % (v, k), base, v, k, "0" * 64, "REJECT", "F"))
            cases.append(("negative/%d_%d_missing_codeword.txt" % (v, k), render(v, k, code[:-1]), v, k, None, "REJECT", "F"))
            cases.append(("negative/%d_%d_extra_codeword.txt" % (v, k), render(v, k, code + [[(x + 1) % v for x in code[0]]]), v, k, None, "REJECT", "F"))
            c = [list(x) for x in code]
            c[0][1] = c[0][0]
            cases.append(("negative/%d_%d_repeated_element.txt" % (v, k), render(v, k, c), v, k, None, "REJECT", "F"))
            c = [list(x) for x in code]
            c[0][1] = v
            cases.append(("negative/%d_%d_out_of_range.txt" % (v, k), render(v, k, c), v, k, None, "REJECT", "F"))
            cases.append(("negative/%d_%d_leading_zero.txt" % (v, k), base.replace("\n0 ", "\n00 ", 1), v, k, None, "REJECT", "F"))
            cases.append(("negative/%d_%d_crlf.txt" % (v, k), base.replace("\n", "\r\n"), v, k, None, "REJECT", "F"))
            c = [list(x) for x in code]
            c[0] = [(x + 5) % v for x in c[0]]
            cases.append(("preserving/%d_%d_translate.txt" % (v, k), render(v, k, c), v, k, None, "ACCEPT", None))
            c = [list(x) for x in code]
            c[1] = [(-x) % v for x in c[1]]
            cases.append(("preserving/%d_%d_negate.txt" % (v, k), render(v, k, c), v, k, None, "ACCEPT", None))
            cases.append(("preserving/%d_%d_reorder.txt" % (v, k), render(v, k, code[::-1]), v, k, None, "ACCEPT", None))
        for rel, text, cv, ck, csha, expect, check in cases:
            path = write(rel, text)
            sha = hashlib.sha256(text.encode("ascii", "replace")).hexdigest() if csha is None else csha
            sha_file = hashlib.sha256(open(path, "rb").read()).hexdigest()
            if csha is None:
                sha = sha_file
            rc, rep = run(path, cv, ck, sha)
            ok = rep.get("verdict") == expect and (expect == "ACCEPT" and rc == 0 or rep.get("failed_check") == check and rc == 1)
            bad += not ok
            rows.append(dict(file=rel, cli_v=cv, cli_k=ck, expect=expect, intended=check, rc=rc, verdict=rep.get("verdict"),
                             failed_check=rep.get("failed_check"), reason=rep.get("reason"), uncovered=rep.get("uncovered"),
                             sha256=sha_file, ok=ok))
            print("%s %-45s %s %s %s" % ("ok " if ok else "BAD", rel, rep.get("verdict"), rep.get("failed_check") or "",
                                        rep.get("uncovered") if expect == "ACCEPT" and rel.startswith("positive") else ""))
    vsha = hashlib.sha256(open(VER, "rb").read()).hexdigest()
    with open(os.path.join(LANE, "controls", "receipt.json"), "w") as fh:
        json.dump(dict(verifier_sha256=vsha, fixtures=len(rows), mismatches=bad, rows=rows), fh, indent=1)
    print("fixtures=%d mismatches=%d verifier_sha256=%s" % (len(rows), bad, vsha))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
