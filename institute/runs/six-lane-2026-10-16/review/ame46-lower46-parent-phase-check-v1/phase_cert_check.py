#!/usr/bin/env python3
"""Parent check of the 24 LOWER46 phase certificates (AME(4,6) s>=46 candidate).
Inputs: certificates-from-audit.md (this dir) and the pinned evidence JSONs in
../ame46-lower46-parent-inputs-v1/evidence/. A certificate is a list of (sign, k, a, b, c, d):
the 2x2 block of reshaping k (0: 12|34, 1: 13|24, 2: 14|23) with corners r1c1 r1c2 r2c1 r2c2.
Each block must be a genuine component of N (both rows and both columns have exactly two
points of N). Unitarity of the reshaped matrix then forces phi_a - phi_b - phi_c + phi_d = pi
(mod 2 pi). A +-1 combination of an odd number of such forms that sums to the zero form
gives 0 = odd * pi (mod 2 pi), a contradiction. Read-only; prints JSON."""
import json, re, sys
from collections import Counter, defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
EV = HERE.parent / "ame46-lower46-parent-inputs-v1" / "evidence"
RESH = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
CASES = {"(30,0) {3,3}": ("t30_e0", [[3, 3], [2, 2, 2], [2, 2, 2], [2, 2, 2]]),
         "(28,0) {4,4}": ("t28_e0", [[4, 4], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]),
         "(28,0) {4,2,2}": ("t28_e0", [[4, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]),
         "(28,0) {2,2,2,2}\u2074": ("t28_e0", [[2, 2, 2, 2]] * 4)}
def parse(md):
    out, case = [], None
    for l in md.split("\n"):
        if not (l.startswith("|") and "[" in l):
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if cells[0]:
            case = cells[0]
        rep = cells[1].split()[0]
        orb = int(cells[1].split("(")[1].rstrip(")"))
        terms = [(1 if s == "+" else -1, int(k), a, b, c, d) for s, k, a, b, c, d in
                 re.findall(r"([+\u2212-])\[(\d): (\d{4}) (\d{4}) (\d{4}) (\d{4})\]", cells[2])]
        out.append((case, rep, orb, terms))
    return out
def check(N, terms):
    form = Counter()
    for s, k, a, b, c, d in terms:
        (a0, a1), (b0, b1) = RESH[k]
        row = lambda x: (x[a0], x[a1]); col = lambda x: (x[b0], x[b1])
        R, C = defaultdict(set), defaultdict(set)
        for x in N:
            R[row(x)].add(col(x)); C[col(x)].add(row(x))
        if not all(p in N for p in (a, b, c, d)):
            return "corner not in N"
        if not (row(a) == row(b) and row(c) == row(d) and col(a) == col(c) and col(b) == col(d)
                and row(a) != row(c) and col(a) != col(b)):
            return "not a 2x2 block"
        if not (len(R[row(a)]) == 2 and len(R[row(c)]) == 2 and len(C[col(a)]) == 2 and len(C[col(b)]) == 2):
            return "not a component"
        for p, w in ((a, 1), (b, -1), (c, -1), (d, 1)):
            form[p] += s * w
    if any(form.values()):
        return "nonzero sum"
    if len(terms) % 2 != 1:
        return "even number of forms"
    return "ok"
def main():
    certs = parse((HERE / "certificates-from-audit.md").read_text())
    res = []
    for case, rep, orb, terms in certs:
        f, prof = CASES[case]
        J = json.loads((EV / f"large_t_gen_{f}.json").read_text())
        P = [p for p in J["profiles"] if p["profile"] == prof]
        assert len(P) == 1
        r = P[0]["reps"][int(rep[1:])]
        N = set(r["N"])
        v = check(N, terms)
        if r["orbit_size"] != orb:
            v = "orbit size mismatch"
        if len(N) != 2 * J["h"] + J["e"]:
            v = "|N| mismatch"
        res.append({"case": case, "rep": rep, "orbit_size": orb, "forms": len(terms), "verdict": v,
                    "engine_phase_obstruction_flag": r["phase_obstruction_verified"]})
    print(json.dumps({"checked": len(res), "pass": sum(x["verdict"] == "ok" for x in res), "results": res}, indent=1))
    return 0 if all(x["verdict"] == "ok" for x in res) and len(res) == 24 else 1
if __name__ == "__main__":
    sys.exit(main())
