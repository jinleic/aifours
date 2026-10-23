#!/usr/bin/env python3
"""Re-express a recorded design (KM rows of group FROM) as KM rows of a larger group TO after
checking that the block set is TO-invariant.  Writes a summary JSON usable by
pipeline2.py --rows-from OUT.json:0 (exclusive create).
Usage: regroup_design.py SUMMARY.json:IDX FROM TO OUT.json"""
import lane_guard  # noqa: F401

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import xopen
from cqs_km import CQSKM
from derived_io import load_design
import groups as grp


def main():
    src, frm, to, out = sys.argv[1:5]
    spec, v, g, blocks = load_design(frm, src)
    B = set(tuple(sorted(b)) for b in blocks)
    spec2 = grp.build(to, 4, g)
    for gen in spec2["gens"]:
        assert all(tuple(sorted(gen[p] for p in b)) in B for b in B), f"design is not {to}-invariant"
    km = CQSKM(v, spec2["group_of"], spec2["gens"])
    rows = [j for j, (lab, _) in enumerate(km.rows) if tuple(int(x) for x in km.Q[lab]) in B]
    assert sorted(tuple(sorted(b)) for b in km.blocks_of(rows)) == sorted(B)
    rec = {"group": to, "g": g, "source": f"{src} ({frm}) re-expressed over {to}",
           "samples": [{"sample": 0, "km_status": "REGROUPED", "rows": rows}]}
    with xopen(out) as fh:
        json.dump(rec, fh)
    print(f"{src}: {to}-invariant, {len(rows)} KM rows over {to}")


if __name__ == "__main__":
    main()
