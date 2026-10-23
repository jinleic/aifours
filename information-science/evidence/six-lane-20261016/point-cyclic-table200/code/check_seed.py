#!/usr/bin/env python3
"""check_seed.py -- expand PC-SEED files with pc_expand_general.py, check the certificates with pc_check.py, and
compare the observed class orbit lengths with the seed's type (t, K): expected multiset {t} u {4k : k in K}.
Writes OUTDIR/<seed basename>.cert and OUTDIR/check-receipt.json; OUTDIR must not exist (fresh output directory);
never deletes or overwrites anything.
Usage: check_seed.py OUTDIR SEED [SEED ...]
"""
import ast
import hashlib
import json
import os
import subprocess
import sys

CODE = os.path.dirname(os.path.abspath(__file__))


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def seed_type(path):
    lines = open(path).read().rstrip("\n").split("\n")
    v, t = int(lines[0].split()[1]), int(lines[1].split()[1])
    K = [int(l.split()[1]) for l in lines if l.startswith("GROUP ")]
    return v, t, K


def main(argv):
    if len(argv) < 3:
        print(__doc__, file=sys.stderr)
        return 2
    out = argv[1]
    os.makedirs(out)                      # fails if it exists: fresh output directory
    rows, ok = [], True
    for seed in argv[2:]:
        v, t, K = seed_type(seed)
        cert = os.path.join(out, os.path.basename(seed).replace(".seed", "") + ".cert")
        p1 = subprocess.run([sys.executable, os.path.join(CODE, "pc_expand_general.py"), seed, cert],
                            capture_output=True, text=True)
        row = {"seed": seed, "seed_sha256": sha(seed), "v": v, "t": t, "K": K, "expand_rc": p1.returncode,
               "expand_out": p1.stdout.strip()}
        if p1.returncode == 0:
            p2 = subprocess.run([sys.executable, os.path.join(CODE, "pc_check.py"), cert],
                                capture_output=True, text=True)
            verdict = p2.stdout.strip().split("\n")[-1]
            orbits = None
            for line in p2.stdout.split("\n"):
                if line.startswith("class_orbits: "):
                    orbits = ast.literal_eval(line[len("class_orbits: "):])
            lengths = sorted(o["length"] for o in orbits) if orbits else None
            expected = sorted([t] + [4 * k for k in K])
            row.update({"cert": cert, "cert_sha256": sha(cert), "check_rc": p2.returncode, "verdict": verdict,
                        "orbit_lengths": lengths, "expected_orbit_lengths": expected,
                        "type_match": lengths == expected})
            good = p2.returncode == 0 and verdict == "PASS" and lengths == expected
        else:
            good = False
        row["ok"] = good
        ok &= good
        rows.append(row)
        print(f"{seed}: v={v} t={t} K={K} expand_rc={p1.returncode} "
              f"check={row.get('verdict')} orbits={row.get('orbit_lengths')} type_match={row.get('type_match')}")
    with open(os.path.join(out, "check-receipt.json"), "x") as f:
        json.dump({"checker_sha256": sha(os.path.join(CODE, "pc_check.py")),
                   "expander_sha256": sha(os.path.join(CODE, "pc_expand_general.py")), "rows": rows,
                   "all_ok": ok}, f, indent=1)
        f.write("\n")
    print("ALL-OK" if ok else "NOT-ALL-OK")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
