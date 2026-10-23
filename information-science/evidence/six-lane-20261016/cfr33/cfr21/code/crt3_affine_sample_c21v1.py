#!/usr/bin/env python3
"""Versioned sampler of structured (Z7,7;3)-DM patterns, followed by exact CRT/F3 lifting.
No SAT, no symmetry-exhaustion claim; each pattern solved exactly or labelled UNKNOWN.
Usage: crt3_affine_sample_c21v1.py SEED SECONDS OUTDIR [MAXPATTERNS]
OUTDIR must not exist. Fields/lifts: code/crt3_lift_c21v1.py.

Columns are (block t in {0,1,2}, c in F7), 7 rows i in F7.
beta_i(t,c) = a[t][i]*c + b[t][i] mod7. Every a[t] is a permutation
of F7, so every row-pair difference hits each residue once per block.
Normalisation: a[0]=id, b[0]=0; a[1],a[2] fix0,1 (random permutations
of2..6); b[t][0]=b[t][1]=0 (t=1,2). These are RESTRICTED pattern families.
Family by index modulo3:
  0 affine-random: independent b[t][i] in F7 (t=1,2; i=2..6).
  1 polynomial23: b[t][i]=u_t*(a[t][i]^2-a[t][i]) +
                              v_t*(a[t][i]^3-a[t][i]) mod7,
                    u_t,v_t independently in F7.
  2 common-slope-polynomial23: same formula, but a[t]=id for every block.
Within a pattern all top-digit choices are explored by the exact lift solver,
with per-pattern native deadline min(2s, remaining chunk time). Random patterns
may repeat; no claim of exhaustive coverage or uniform sampling of designs.
On a lift: write pattern.json + candidate.dmraw + receipt.json, exit10.
A rank/dimension histogram and the first example of each new dimension signature
are retained; inputs are reproducible from seed and Python's recorded version.
"""
import collections
import hashlib
import json
import os
from pathlib import Path
import random
import signal
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

import crt3_lift_c21v1 as lift


def clock():
    return datetime.now(ZoneInfo("America/Los_Angeles")).isoformat()


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    seed, seconds, outdir = int(sys.argv[1]), float(sys.argv[2]), sys.argv[3]
    maxpatterns = int(sys.argv[4]) if len(sys.argv) > 4 else 10 ** 18
    os.mkdir(outdir)
    rng = random.Random(seed)
    t0 = time.monotonic()
    signal.signal(signal.SIGTERM, lift.on_term)
    signal.signal(signal.SIGINT, lift.on_term)
    start = {"clock": clock(), "seed": seed, "seconds": seconds, "maxpatterns": maxpatterns,
             "python": sys.version, "sampler_sha256": digest(__file__), "solver_sha256": digest(lift.__file__)}
    with open(outdir + "/start.json", "x") as fh:
        json.dump(start, fh, indent=1)
    hist = collections.Counter()
    verdicts = collections.Counter()
    families = collections.Counter()
    examples = set()
    count = 0
    last = t0
    found = False
    with open(outdir + "/progress.jsonl", "x") as log:
        while count < maxpatterns and not lift.STOP and time.monotonic() - t0 < seconds:
            typ = count % 3
            family = ("affine-random", "polynomial23", "common-slope-polynomial23")[typ]
            slopes = [list(range(7)) for _ in range(3)]
            for t in (1, 2):
                if typ != 2:
                    tail = list(range(2, 7))
                    rng.shuffle(tail)
                    slopes[t] = [0, 1] + tail
            offsets = [[0] * 7 for _ in range(3)]
            coefficients = []
            for t in (1, 2):
                if typ == 0:
                    for i in range(2, 7):
                        offsets[t][i] = rng.randrange(7)
                else:
                    u, v = rng.randrange(7), rng.randrange(7)
                    coefficients.append([u, v])
                    for i in range(2, 7):
                        a = slopes[t][i]
                        offsets[t][i] = (u * (a * a - a) + v * (a ** 3 - a)) % 7
            beta = [[(slopes[t][i] * c + offsets[t][i]) % 7 for t in range(3) for c in range(7)] for i in range(7)]
            remaining = seconds - (time.monotonic() - t0)
            if remaining <= 0:
                break
            rec, D = lift.solve_pattern(7, beta, min(2.0, remaining))
            rec.update(family=family, index=count, clock=clock())
            signature = (family, rec["kernel_dimension"], rec.get("inequality_rank"), rec["verdict"])
            hist[signature] += 1
            verdicts[rec["verdict"]] += 1
            families[family] += 1
            pattern = {"q": 7, "beta": beta, "family": family, "index": count, "slopes": slopes,
                       "offsets": offsets, "polynomial_coefficients": coefficients}
            if signature not in examples:
                ex = outdir + "/example-%04d.json" % len(examples)
                with open(ex, "x") as fh:
                    json.dump({"pattern": pattern, "receipt": rec}, fh)
                examples.add(signature)
            count += 1
            if D is not None:
                with open(outdir + "/pattern.json", "x") as fh:
                    json.dump(pattern, fh, indent=1)
                rec["pattern_sha256"] = digest(outdir + "/pattern.json")
                lift.write_solution(outdir + "/candidate", rec, D)
                found = True
                break
            if time.monotonic() - last >= 30:
                p = {"clock": clock(), "wall_s": time.monotonic() - t0, "patterns": count, "verdicts": dict(verdicts)}
                log.write(json.dumps(p) + "\n")
                log.flush()
                print(json.dumps(p), flush=True)
                last = time.monotonic()
    final = {**start, "end_clock": clock(), "wall_s": time.monotonic() - t0, "patterns": count,
             "families": dict(families), "verdicts": dict(verdicts), "stopped_by_signal": lift.STOP,
             "histogram": [{"signature": key, "count": n} for key, n in sorted(hist.items(), key=lambda kv: str(kv[0]))],
             "status": "CANDIDATE" if found else "UNKNOWN (restricted pattern sample, not a nonexistence result)"}
    with open(outdir + "/record.json", "x") as fh:
        json.dump(final, fh, indent=1)
    print(json.dumps({k: final[k] for k in ("end_clock", "wall_s", "patterns", "verdicts", "status")}), flush=True)
    raise SystemExit(10 if found else 0)


if __name__ == "__main__":
    main()
