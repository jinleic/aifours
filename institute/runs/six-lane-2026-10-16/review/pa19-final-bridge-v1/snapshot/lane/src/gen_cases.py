#!/usr/bin/env python3
"""Generate all normalized case specs for PA(N,k,q) (README normalization).

Position rule: col0, col1 = two columns of minimum excess (for N=19: two P0 columns;
every multiset has >= 5). Positions 2..k-1 = remaining columns by excess
non-increasing, ties broken by profile tuple descending (fixed convention).
Case = (multiset index, M-class index). Writes cases/<tag>/specs/*.json + index.json.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mclasses  # noqa: E402
import profiles  # noqa: E402


def main():
    N, k, q = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    outdir = sys.argv[4]
    os.makedirs(os.path.join(outdir, "specs"), exist_ok=True)
    P = profiles.enumerate_profiles(N, k, q)
    kmin = P["kappa_min"]
    cache = {}
    index = []
    for mi, ms in enumerate(P["multisets"]):
        profs = [tuple(p) for p in ms["profiles"]]
        ex = lambda p: profiles.kappa(p) - kmin  # noqa: E731
        asc = sorted(profs, key=lambda p: (ex(p), [-x for x in p]))
        c0, c1 = asc[0], asc[1]
        rest = list(profs)
        rest.remove(c0)
        rest.remove(c1)
        rest.sort(key=lambda p: (-ex(p), [-x for x in p]))
        pos = [list(c0), list(c1)] + [list(p) for p in rest]
        key = (c0, c1)
        if key not in cache:
            cache[key] = mclasses.classes(list(c0), list(c1))
        for ci, (canon, nmat) in enumerate(cache[key]):
            M = [list(r) for r in canon]
            tag = "ms%02d_m%03d" % (mi, ci)
            spec = {"N": N, "k": k, "q": q, "multiset_index": mi, "mclass_index": ci,
                    "excess": ms["excess"], "profiles": pos, "M": M,
                    "mclass_orbit_matrices": nmat}
            json.dump(spec, open(os.path.join(outdir, "specs", tag + ".json"), "w"))
            index.append({"tag": tag, "multiset": mi, "mclass": ci, "excess": ms["excess"],
                          "profiles": pos})
    json.dump({"N": N, "k": k, "q": q, "num_cases": len(index),
               "num_multisets": len(P["multisets"]),
               "mclass_counts": {"%s|%s" % (",".join(map(str, a)), ",".join(map(str, b))):
                                 len(v) for (a, b), v in cache.items()},
               "cases": index}, open(os.path.join(outdir, "index.json"), "w"), indent=1)
    print(len(index), {"%s|%s" % (a, b): len(v) for (a, b), v in cache.items()})


if __name__ == "__main__":
    main()
