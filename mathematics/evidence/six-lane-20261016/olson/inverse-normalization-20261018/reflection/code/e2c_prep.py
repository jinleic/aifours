#!/usr/bin/env python3
"""E2 part C input: convert the read-only RGR avoider lists olson/evidence/was/p{5,7}_N*_all.jsonl ("all" lines:
every avoider run datum with its theta, rotation-canonical) into plain lines "p k a.. b.. l.. y.." (y from theta with the
was_verify convention y_(k-1) = 0).  Output: out/e2c_input_p{p}.txt (exclusive create)."""
import json, os, sys, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
EV = os.path.normpath(os.path.join(HERE, "..", "..", "..", "evidence", "was"))
for p, fn in ((5, "p5_N18_all.jsonl"), (7, "p7_N26_all.jsonl")):
    src = os.path.join(EV, fn)
    with open(src, "rb") as f:
        raw = f.read()
    lines = []
    for line in raw.decode().splitlines():
        d = json.loads(line)
        if d.get("all") != 1:
            continue
        k = d["k"]; a = d["a"]; b = d["b"]; l = d["l"]; th = d["theta"]
        y = [0] * k; prev = 0
        for i in range(k):
            y[i] = (prev - th[i]) % p; prev = y[i]
        assert y[k - 1] == 0
        assert sum(a) + sum(b) + sum(l) == 4 * p - 2
        lines.append(" ".join(map(str, [p, k] + a + b + l + y)))
    outp = os.path.join(HERE, "..", "out", "e2c_input_p%d.txt" % p)
    with open(outp, "x") as f:
        f.write("\n".join(lines) + "\n")
    print(p, fn, hashlib.sha256(raw).hexdigest(), len(lines))
