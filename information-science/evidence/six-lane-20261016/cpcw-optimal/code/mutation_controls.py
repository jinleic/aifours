#!/usr/bin/env python3
"""Mutation and validity-preserving controls for the lane certificates, run through the lane copy of the prep
verifier (code/verify_cpcw.py, SHA-256 85f93e8b...e7be8).  Stdlib only.

For every certificate certs/v<V>/cpcw_<V>_<K>.txt: build fixtures in controls/fixtures/<V>/, call the verifier
with the fixture's own SHA-256 (unless the control is a SHA mismatch), and compare (verdict, failed_check) with the
expectation.  Writes controls/mutation-receipt.json and prints a summary.  Exit 0 iff every fixture matches.
"""
import hashlib
import json
import math
import os
import subprocess
import sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERIFIER = os.path.join(LANE, "code", "verify_cpcw.py")
CERTS = [(122, 6), (123, 6), (124, 6), (143, 5), (144, 5), (146, 5), (162, 5), (167, 5)]


def render(v, k, code, header=None, eol="\n", final=True):
    lines = [header if header is not None else "CPCW %d %d" % (v, k)]
    lines += [" ".join(str(x) for x in cw) for cw in code]
    txt = eol.join(lines) + (eol if final else "")
    return txt.encode("ascii")


def run(path, v, k, sha):
    p = subprocess.run([sys.executable, VERIFIER, path, "--v", str(v), "--k", str(k), "--sha256", sha],
                       capture_output=True, text=True)
    try:
        rep = json.loads(p.stdout)
    except ValueError:
        rep = {"verdict": "ERROR", "stderr": p.stderr}
    return p.returncode, rep


def fixtures(v, k, code):
    """yield (name, bytes, cli_v, cli_k, sha_override, expected_verdict, expected_check)"""
    s = len(code)
    srt = lambda cw: sorted(x % v for x in cw)
    # validity-preserving
    t = 17
    yield "translate_cw0", render(v, k, [srt([x + t for x in code[0]])] + code[1:]), v, k, None, "ACCEPT", None
    yield "negate_cw1", render(v, k, [code[0], srt([-x for x in code[1]])] + code[2:]), v, k, None, "ACCEPT", None
    yield "reorder", render(v, k, code[::-1]), v, k, None, "ACCEPT", None
    m = next(u for u in range(2, v) if math.gcd(u, v) == 1)
    yield "multiplier_%d" % m, render(v, k, [srt([m * x for x in cw]) for cw in code]), v, k, None, "ACCEPT", None
    # D-type faults
    yield "cw1_translate_of_cw0", render(v, k, [code[0], srt([x + 5 for x in code[0]])] + code[2:]), v, k, None, "REJECT", "D"
    cw = list(code[0]); cw[1] = (cw[1] + 1) % v
    if len(set(cw)) == k:
        yield "cw0_elem_plus1", render(v, k, [srt(cw)] + code[1:]), v, k, None, "REJECT", "D"
    a, b = code[0][1], code[1][1]
    c0 = [x if x != a else b for x in code[0]]; c1 = [x if x != b else a for x in code[1]]
    if len(set(c0)) == k and len(set(c1)) == k:
        yield "swap_elem_cw0_cw1", render(v, k, [srt(c0), srt(c1)] + code[2:]), v, k, None, "REJECT", "D"
    if v % 2 == 0:
        y = (code[0][1] + v // 2) % v
        if y not in code[0]:
            yield "half_v_pair", render(v, k, [srt(code[0][:-1] + [y])] + code[1:]), v, k, None, "REJECT", "D"
    # F-type faults
    yield "cli_wrong_v", render(v, k, code), v + 1, k, None, "REJECT", "F"
    yield "cli_wrong_k", render(v, k, code), v, k + 1, None, "REJECT", "F"
    yield "header_wrong_v", render(v, k, code, header="CPCW %d %d" % (v + 1, k)), v, k, None, "REJECT", "F"
    yield "sha_mismatch", render(v, k, [srt([x + 1 for x in code[0]])] + code[1:]), v, k, "ORIG", "REJECT", "F"
    yield "missing_cw", render(v, k, code[:-1]), v, k, None, "REJECT", "F"
    yield "extra_cw", render(v, k, code + [code[-1]]), v, k, None, "REJECT", "F"
    yield "out_of_range", render(v, k, [code[0][:-1] + [v]] + code[1:]), v, k, None, "REJECT", "F"
    yield "repeated_elem", render(v, k, [code[0][:-1] + [code[0][0]]] + code[1:]), v, k, None, "REJECT", "F"
    lead = render(v, k, code).replace(b"\n0 ", b"\n00 ", 1)
    yield "leading_zero", lead, v, k, None, "REJECT", "F"
    yield "crlf", render(v, k, code, eol="\r\n"), v, k, None, "REJECT", "F"
    yield "no_final_lf", render(v, k, code, final=False), v, k, None, "REJECT", "F"
    yield "short_cw", render(v, k, [code[0][:-1]] + code[1:]), v, k, None, "REJECT", "F"


def main():
    out, bad, n = [], 0, 0
    for v, k in CERTS:
        cert = os.path.join(LANE, "certs", "v%d" % v, "cpcw_%d_%d.txt" % (v, k))
        data = open(cert, "rb").read()
        orig_sha = hashlib.sha256(data).hexdigest()
        lines = data.decode("ascii").rstrip("\n").split("\n")
        code = [[int(x) for x in ln.split(" ")] for ln in lines[1:]]
        rc, rep = run(cert, v, k, orig_sha)
        rec = {"v": v, "k": k, "certificate": os.path.relpath(cert, LANE), "sha256": orig_sha,
               "original": {"verdict": rep.get("verdict"), "uncovered": rep.get("uncovered")}, "fixtures": []}
        n += 1
        if rep.get("verdict") != "ACCEPT":
            bad += 1
        fdir = os.path.join(LANE, "controls", "fixtures", str(v))
        os.makedirs(fdir, exist_ok=True)
        for name, blob, cv, ck, shao, ev, ec in fixtures(v, k, code):
            path = os.path.join(fdir, name + ".txt")
            with open(path, "wb") as f:
                f.write(blob)
            sha = orig_sha if shao == "ORIG" else hashlib.sha256(blob).hexdigest()
            rc, rep = run(path, cv, ck, sha)
            got = (rep.get("verdict"), rep.get("failed_check"))
            ok = got[0] == ev and (ev == "ACCEPT" or got[1] == ec)
            n += 1
            if not ok:
                bad += 1
            rec["fixtures"].append({"name": name, "file": os.path.relpath(path, LANE),
                                    "fixture_sha256": hashlib.sha256(blob).hexdigest(), "expected": [ev, ec],
                                    "got": list(got), "reason": rep.get("reason"), "match": ok})
        out.append(rec)
    vsha = hashlib.sha256(open(VERIFIER, "rb").read()).hexdigest()
    receipt = {"verifier": os.path.relpath(VERIFIER, LANE), "verifier_sha256": vsha, "checks": n, "mismatches": bad,
               "certificates": out}
    with open(os.path.join(LANE, "controls", "mutation-receipt.json"), "w") as f:
        json.dump(receipt, f, indent=1, sort_keys=True)
        f.write("\n")
    print("verifier %s checks=%d mismatches=%d" % (vsha, n, bad))
    for rec in out:
        print(rec["v"], rec["original"]["verdict"], len(rec["fixtures"]), "fixtures,",
              sum(1 for x in rec["fixtures"] if x["match"]), "match")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
