#!/usr/bin/env python3
"""classes_report.py -- report the covering rotation classes found by Impl A (cs_neck .found file) at one length:
membership of a reference sequence's rotation class (e.g. the CPro1 length-36 sequence), and the grouping of the
rotation classes into orbits under reversal and complement (the full symmetry group of the covering property:
rotations, reversal, complement).  Read-only on its inputs; writes OUT (exclusive).

Usage: classes_report.py A_FOUND L REFERENCE_TOKENS_FILE OUT.json
  REFERENCE_TOKENS_FILE: whitespace-separated 0/1 tokens (x_0 first), e.g. the CPro1 tab-separated file.
"""
import json
import sys


def lexmin(xs):
    L = len(xs)
    return min(tuple(xs[(t + i) % L] for i in range(L)) for t in range(L))


def to_r(tup):
    r = 0
    for b in tup:
        r = (r << 1) | b
    return r


def main(argv):
    if len(argv) != 5:
        print(__doc__, file=sys.stderr)
        return 2
    found_path, L, ref_path, out = argv[1], int(argv[2]), argv[3], argv[4]
    reps = []
    for line in open(found_path):
        if not line.strip():
            continue
        r_hex, s_hex, per = line.split()
        s = int(s_hex, 16)
        xs = [(s >> i) & 1 for i in range(L)]
        assert to_r(tuple(xs)) == int(r_hex, 16), "r/s mismatch"
        assert lexmin(xs) == tuple(xs), "representative is not lex-minimal"
        reps.append(tuple(xs))
    rep_set = set(reps)
    ref = [int(t) for t in open(ref_path).read().split()]
    assert len(ref) == L and set(ref) <= {0, 1}
    ref_class = lexmin(ref)
    orbits = {}
    for xs in reps:
        images = {lexmin(list(xs)), lexmin(list(reversed(xs))), lexmin([1 - b for b in xs]),
                  lexmin([1 - b for b in reversed(xs)])}
        key = min(images)
        orbits.setdefault(key, set()).update(images)
    closed = all(all(img in rep_set for img in imgs) for imgs in orbits.values())
    res = {
        "L": L,
        "rotation_classes": len(reps),
        "reference_rotation_class_r_hex": hex(to_r(ref_class)),
        "reference_class_found": ref_class in rep_set,
        "orbits_under_reversal_and_complement": len(orbits),
        "orbit_sizes_in_rotation_classes": sorted(len(v) for v in orbits.values()),
        "set_closed_under_reversal_and_complement": closed,
        "orbit_representatives": ["".join(map(str, k)) for k in sorted(orbits)],
    }
    with open(out, "x") as f:
        json.dump(res, f, indent=1)
        f.write("\n")
    print(json.dumps({k: res[k] for k in res if k != "orbit_representatives"}))
    return 0 if res["reference_class_found"] and closed else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
