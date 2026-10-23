#!/usr/bin/env python3
"""Finite controls for proof-ROT-few-v3.md (not premises): Steps 1-4 of Theorem ROT-FEW over all (ZP) multisets of
size R = 2p + 2kappa - k (unit-reduced, two passes), reusing part_b2 of code/check_rotfew_v2.py unchanged.
  out of scope of (F) 2p >= 5k-4: (11,6), (13,7)  (reported only; violations would be informative, not expected/forbidden)
  in scope, new with v3:           (19,8)          (claim: 0 failures; mutated bound E <= k-3-|N| must fail somewhere)
Usage: check_rotfew_v3.py OUT.jsonl
"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import check_rotfew_v2 as base

def main():
    with open(sys.argv[1], "x") as out:
        for (p, k, scope) in ((11, 6, "out"), (13, 7, "out"), (19, 8, "in")):
            for kappa in range(0, k):
                for special in (False, True):
                    t0 = time.time()
                    s = base.part_b2(p, k, kappa, out, scope, special)
                    s["sec"] = round(time.time() - t0, 1)
                    out.write(json.dumps(s) + "\n"); out.flush(); print(s, flush=True)

if __name__ == "__main__":
    main()
