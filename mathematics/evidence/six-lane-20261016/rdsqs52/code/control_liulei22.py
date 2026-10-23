#!/usr/bin/env python3
"""Positive control from published data: Liu–Lei (arXiv:2210.06214v2) Lemma 2.5, RDSQS(22)
on Z21 ∪ {∞}.  The base blocks and the two listed resolutions (at ∞ and at 0) are
parsed directly from the read-only text extraction
  mathematics/kirkman-large-sets-57-87/sources/liu-lei-2210.06214.txt
(lines 189–224), developed under Z21 exactly as the paper states, and written in
the lane certificate format with ∞ = 21.  Standard library only.
Usage: control_liulei22.py OUT_CERT
"""
import hashlib
import re
import sys

SRC = "/Users/jinleic/repos/aifours/mathematics/kirkman-large-sets-57-87/sources/liu-lei-2210.06214.txt"
INF = 21


def sets_in(line):
    out = []
    for m in re.finditer(r"\{([^}]*)\}", line):
        parts = [p.strip() for p in m.group(1).split(",")]
        out.append(tuple(INF if p == "∞" else int(p) for p in parts))
    return out


def main():
    raw = open(SRC, encoding="utf-8").read()
    lines = raw.splitlines()
    i_base = next(i for i, l in enumerate(lines) if "We construct an SQS(22)" in l)
    i_inf = next(i for i, l in enumerate(lines) if l.strip() == "Point ∞:")
    i_zero = next(i for i, l in enumerate(lines) if l.strip() == "Point 0:")
    i_end = next(i for i, l in enumerate(lines) if l.startswith("Lemma 2.6"))
    base = [s for l in lines[i_base:i_inf] for s in sets_in(l) if len(s) == 4]
    res_inf = [sets_in(l) for l in lines[i_inf + 1:i_zero] if sets_in(l)]
    res_zero = [sets_in(l) for l in lines[i_zero + 1:i_end] if sets_in(l)]
    assert len(base) == 19, len(base)
    assert len(res_inf) == 10 and all(len(r) == 7 for r in res_inf)
    assert len(res_zero) == 10 and all(len(r) == 7 for r in res_zero)
    sh = lambda p, s: INF if p == INF else (p + s) % 21
    blocks = set()
    for b in base:
        for s in range(21):
            blocks.add(tuple(sorted(sh(p, s) for p in b)))
    res = {INF: [[tuple(sorted(t)) for t in C] for C in res_inf]}
    for s in range(21):
        res[s] = [[tuple(sorted(sh(p, s) for p in t)) for t in C] for C in res_zero]
    out = ["# Liu–Lei arXiv:2210.06214v2 Lemma 2.5 RDSQS(22), transcribed from " + SRC + " (∞ = 21)",
           f"# source sha256 {hashlib.sha256(raw.encode()).hexdigest()}",
           "RDSQS 22", "BLOCKS"]
    out.extend(" ".join(map(str, b)) for b in sorted(blocks))
    for x in range(22):
        out.append(f"POINT {x}")
        for c, C in enumerate(res[x]):
            out.append(f"CLASS {c}")
            out.extend(" ".join(map(str, t)) for t in sorted(C))
    open(sys.argv[1], "w").write("\n".join(out) + "\n")
    print("blocks", len(blocks), "written", sys.argv[1])


if __name__ == "__main__":
    main()
