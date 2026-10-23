#!/usr/bin/env python3
"""README E0: the cyclic mcDSQS(32) of Tan-Zhou arXiv:2503.11934v1, Appendix B (standard library).

extract TEXT OUT.json      parse the pinned pdftotext file: base blocks = text lines 1326-1332,
                           derived-design parts = text lines 1341-1372 taken in consecutive pairs
                           (16 parts); anchor lines 1321 and 1334 are checked first.
check JSON                 the base blocks develop under Z32 to exactly 1240 blocks forming an
                           SQS(32); the 16 parts partition the derived STS(31) at 0 into partial
                           parallel classes; the translates (parts + a) do so at every a.
controls JSON OUTDIR       4 corrupted copies (retained) must be rejected by `check`.
"""
import hashlib
import json
import os
import re
import sys
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lane_guard  # noqa: F401,E402
from lane_guard import fresh_dir, xopen  # noqa: E402

TRIPLE_OR_QUAD = re.compile(r"\{([0-9, ]+)\}")


def sets_on(line):
    return [tuple(int(t) for t in m.split(",")) for m in TRIPLE_OR_QUAD.findall(line)]


def extract(text_path, out):
    raw = open(text_path, "rb").read()
    L = raw.decode("utf-8").split("\n")
    line = lambda k: L[k - 1]  # 1-based like `awk NR`
    assert "we construct a cyclic SQS(32) on point set Z32" in line(1321), "anchor line 1321 moved"
    assert "The above cyclic SQS(32) is an mcDSQS(32)" in line(1334), "anchor line 1334 moved"
    base = [b for k in range(1326, 1333) for b in sets_on(line(k))]
    parts = [sets_on(line(k)) + sets_on(line(k + 1)) for k in range(1341, 1373, 2)]
    rec = {"source": "Tan-Zhou arXiv:2503.11934v1 Appendix B (Lemma 3.4), printed pp. 23-24",
           "text": text_path, "text_sha256": hashlib.sha256(raw).hexdigest(),
           "base_block_lines": "1326-1332", "part_lines": "1341-1372 (consecutive pairs)",
           "base_blocks": [list(b) for b in base], "derived_at": 0,
           "parts": [[list(t) for t in P] for P in parts]}
    with xopen(out) as fh:
        json.dump(rec, fh, indent=1)
    print(out, "base blocks", len(base), "parts", len(parts), "triples", sum(len(P) for P in parts))


def check(rec):
    v = 32
    base = [tuple(b) for b in rec["base_blocks"]]
    assert all(len(b) == 4 and len(set(b)) == 4 and all(0 <= p < v for p in b) for b in base), "bad base block"
    blocks = {tuple(sorted((p + i) % v for p in b)) for b in base for i in range(v)}
    orbit_len = sorted(len({tuple(sorted((p + i) % v for p in b)) for i in range(v)}) for b in base)
    assert len(blocks) == v * (v - 1) * (v - 2) // 24, f"{len(blocks)} blocks, expected 1240"
    cover = {}
    for b in blocks:
        for t in combinations(b, 3):
            cover[t] = cover.get(t, 0) + 1
    assert set(cover) == set(combinations(range(v), 3)) and set(cover.values()) == {1}, "not an SQS(32)"
    parts = [[tuple(sorted(t)) for t in P] for P in rec["parts"]]
    assert len(parts) == 16, "not 16 parts"
    for a in range(v):
        der = {tuple(p for p in b if p != a) for b in blocks if a in b}
        seen = set()
        for P in parts:
            Q = [tuple(sorted((p + a) % v for p in t)) for t in P]
            pts = [p for t in Q for p in t]
            assert len(pts) == len(set(pts)), "part is not a partial parallel class"
            for t in Q:
                assert t in der and t not in seen, "part triple not derived or repeated"
                seen.add(t)
        assert seen == der, "parts do not cover the derived design"
    return {"blocks": len(blocks), "base_orbit_lengths": dict((n, orbit_len.count(n)) for n in sorted(set(orbit_len))),
            "derived_triples": len(der), "parts": len(parts), "part_sizes": [len(P) for P in parts],
            "result": "PASS: SQS(32); 16 PPCs at every point (translates)"}


def controls(path, outdir):
    rec = json.load(open(path))
    fresh_dir(outdir)
    muts = {
        "base_block_digit": lambda d: d["base_blocks"].__setitem__(5, [0, 1, 7, 31]),
        "drop_base_block": lambda d: d["base_blocks"].pop(12),
        "part_triple_digit": lambda d: d["parts"][15].__setitem__(7, [23, 24, 28]),
        "parts_move_triple": lambda d: d["parts"][0].append(d["parts"][1].pop(0)),
    }
    res = {}
    for name, f in muts.items():
        d = json.loads(json.dumps(rec))
        f(d)
        p = os.path.join(outdir, name + ".json")
        with xopen(p) as fh:
            json.dump(d, fh)
        try:
            check(d)
            res[name] = "ACCEPTED (control failed)"
        except AssertionError as e:
            res[name] = "rejected: " + str(e)
    with xopen(os.path.join(outdir, "control-results.json")) as fh:
        json.dump(res, fh, indent=1)
    print(json.dumps(res, indent=1))
    return all(r.startswith("rejected") for r in res.values())


def main():
    cmd = sys.argv[1]
    if cmd == "extract":
        extract(sys.argv[2], sys.argv[3])
    elif cmd == "check":
        print(json.dumps(check(json.load(open(sys.argv[2])))))
    elif cmd == "controls":
        sys.exit(0 if controls(sys.argv[2], sys.argv[3]) else 1)
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
