#!/usr/bin/env python3
"""list_pending2 = list_pending with revision-11 records accepted (same predicate as summarize9).
Print pending work items (read-only), for chaining runners.
  m1split : ms06 hard tags whose cycle2/hard5 record exists but is not certified (UNKNOWN / unchecked)
            and that have no cycle2/part/<tag>/summary_batched.json -> TAG per line
  m2split : M2 ms06 hard b-indices (cycle2/m2-jobs-hard-direct.txt) whose cycle2/m2skel_drat record
            exists but is not certified and that have no cycle2/m2part_drat/ms06_bNNNNN/summary_batched.json
            -> 6:B per line
Usage: list_pending.py m1split|m2split
"""
import json
import os
import sys

LANE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C2 = os.path.join(LANE, "cycle2")


def certified(r):
    if not r or r.get("status") != "UNSAT" or not r.get("checked") or not r.get("drat_trim_verified"):
        return False
    rev = r.get("stream_check_revision")
    if rev == 11:
        return ((r.get("drat_trim") or {}).get("s_lines") == ["s VERIFIED"] and r.get("replay_ok") is True
                and r.get("reader_ok") is True and not r.get("admission_denied") and not r.get("aborted_by_sigterm"))
    if rev == 10:
        return (r.get("drat_trim") or {}).get("s_lines") == ["s VERIFIED"] and r.get("replay_sha256_matches") is True
    if rev == 9:
        return (r.get("drat_trim") or {}).get("s_lines") == ["s VERIFIED"]
    return rev == 5


def jl(p):
    try:
        return json.load(open(p))
    except (OSError, ValueError):
        return None


def main():
    mode = sys.argv[1]
    if mode == "m1split":
        for t in (l.strip() for l in open(os.path.join(C2, "tags-ms06-all-hard.txt"))):
            if not t:
                continue
            r = jl(os.path.join(C2, "hard5", t + ".json"))
            if r is not None and not certified(r) and not os.path.exists(os.path.join(C2, "part", t, "summary_batched.json")):
                print(t)
    elif mode == "m2split":
        for line in open(os.path.join(C2, "m2-jobs-hard-direct.txt")):
            mi, rng = line.strip().split(":")
            a, b = rng.split("-")
            for i in range(int(a), int(b) + 1):
                r = jl(os.path.join(C2, "m2skel_drat", "ms%02d_b%05d.json" % (int(mi), i)))
                if r is not None and not certified(r) and not os.path.exists(
                        os.path.join(C2, "m2part_drat", "ms%02d_b%05d" % (int(mi), i), "summary_batched.json")):
                    print("%d:%d" % (int(mi), i))


if __name__ == "__main__":
    main()
