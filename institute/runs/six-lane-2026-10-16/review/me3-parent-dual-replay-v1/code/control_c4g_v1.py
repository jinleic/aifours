#!/usr/bin/env python3
"""control_c4g_v1.py -- supplement to controls_v2 (run r15), whose C4.1-C4.3 found no real G leaf box with Im W < 0
in the scanned cells (those cells are certified by SMALL on large boxes, so no leaf enclosure has Im W < 0).
The wrong-branch guard of dualcheck_v2.ev_G is exercised on synthetic boxes where Im W < 0 is certified
(s near 0, delta near 0, omega in [3, 3 + 1/1024]: W ~ zeta^3 with arg ~ 3 arctan(3) ~ 3.75 in (pi, 2pi)), and on a
synthetic Im W > 0 box (omega in [1/2, 1/2 + 1/1024]):
  G-a principal Arg forced on Im W < 0  -> rejected 'alpha-negative';
  G-b branch 'up' forced on Im W < 0    -> rejected 'branch-condition-false';
  G-c branch 'down' forced on Im W > 0  -> rejected 'branch-condition-false';
  G-d branch 'left' forced where Re W > 0 -> rejected 'branch-condition-false';
  G-e unforced checker logic on the same boxes -> certified (positive).
Writes OUT (exclusive).  Usage: python -I -B control_c4g_v1.py OUT.json
"""
import sys
import os
import json
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import dualcheck_v2 as D  # noqa: E402
from flint import acb, fmpq  # noqa: E402

OUT = sys.argv[1]
C = D.Ctx(fmpq(11, 50))
e = fmpq(1, 1024)
down_box = ((fmpq(0), e), (fmpq(0), e), (fmpq(3), fmpq(3) + e))
up_box = ((fmpq(0), e), (fmpq(0), e), (fmpq(1, 2), fmpq(1, 2) + e))


def W_of(box):
    s, d, w = D.I(*box[0]), D.I(*box[1]), D.I(*box[2])
    return D.Wfun(C, s, D.ONE / acb(1 + d, -w))


Wd, Wu = W_of(down_box), W_of(up_box)
res = {"tool": "control_c4g_v1.py", "tool_sha256": D.sha256_file(os.path.abspath(__file__))[0],
       "checker_sha256": D.sha256_file(D.__file__)[0], "at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
       "boxes": {"down": [[str(a), str(b)] for a, b in down_box], "up": [[str(a), str(b)] for a, b in up_box]},
       "preconditions": {"ImW<0 on down box": bool(Wd.imag < 0), "ImW>0 on up box": bool(Wu.imag > 0),
                         "ReW>0 on down box": bool(Wd.real > 0), "ReW>0 on up box": bool(Wu.real > 0)},
       "controls": {}}
checks = [
    ("G-a principal Arg on Im W<0", D.ev_G(C, down_box, force_branch="principal"), (False, "alpha-negative")),
    ("G-b 'up' forced on Im W<0", D.ev_G(C, down_box, force_branch="up"), (False, "branch-condition-false")),
    ("G-c 'down' forced on Im W>0", D.ev_G(C, up_box, force_branch="down"), (False, "branch-condition-false")),
]
lb = down_box if Wd.real > 0 else up_box
checks.append(("G-d 'left' forced where Re W>0", D.ev_G(C, lb, force_branch="left"), (False, "branch-condition-false")))
for name, got, want in checks:
    res["controls"][name] = {"expected": list(want), "observed": list(got), "pass": got == want}
for name, box in (("G-e unforced, down box (positive)", down_box), ("G-e unforced, up box (positive)", up_box)):
    got = D.ev_G(C, box)
    res["controls"][name] = {"expected": "certified", "observed": list(got), "pass": got[0] is True}
res["all_pass"] = all(v["pass"] for v in res["controls"].values()) and res["preconditions"]["ImW<0 on down box"] \
    and res["preconditions"]["ImW>0 on up box"]
with open(OUT, "x") as fh:
    json.dump(res, fh, indent=1)
print(json.dumps({"all_pass": res["all_pass"], "pre": res["preconditions"],
                  "obs": {k: v["observed"] for k, v in res["controls"].items()}}))
