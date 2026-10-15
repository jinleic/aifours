"""Group oracle rules into run-length 'skeleton' families for inspection.

Usage: python3 work/families.py evidence/oracle/FILE.jsonl
Prints, for each LHS skeleton (sequence of run letters), the list of
(LHS exponents -> RHS run-length word).
"""
import itertools
import json
import sys
from collections import defaultdict


def runs(w):
    return [(c, len(list(g))) for c, g in itertools.groupby(w)]


def rl(w):
    return " ".join(c if k == 1 else f"{c}^{k}" for c, k in runs(w))


def main():
    fams = defaultdict(list)
    for line in open(sys.argv[1]):
        d = json.loads(line)
        if "lhs" not in d:
            print("#", {k: d[k] for k in ("irreducible_counts", "match", "delta", "nrules") if k in d})
            continue
        sk = "".join(c for c, _ in runs(d["lhs"]))
        fams[sk].append((tuple(k for _, k in runs(d["lhs"])), d["rhs"]))
    for sk in sorted(fams, key=lambda s: (min(sum(e) for e, _ in fams[sk]), s)):
        items = fams[sk]
        print(f"[{sk}] {len(items)} rules")
        for e, rhs in items[:8]:
            print("    ", e, "->", rl(rhs))
        if len(items) > 8:
            print("     ...")


if __name__ == "__main__":
    main()
