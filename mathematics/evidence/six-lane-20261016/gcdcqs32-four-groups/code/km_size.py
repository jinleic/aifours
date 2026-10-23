#!/usr/bin/env python3
"""README E2: build (without solving) the Kramer–Mesner model of GROUP at group size G, record
build time, model summary and the KM CNF (exclusive create), so that kissat can be run on it with
a native time limit.  Usage: km_size.py GROUP G OUTDIR"""
import lane_guard  # noqa: F401

import json
import os
import resource
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import fresh_dir, xopen
from cqs_km import CQSKM
from lanelib import closure
import groups as grp


def main():
    group, g, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    fresh_dir(out)
    t0 = time.time()
    spec = grp.build(group, 4, g)
    G = closure(spec["gens"], 4 * g)
    km = CQSKM(4 * g, spec["group_of"], spec["gens"])
    t1 = time.time()
    cnf, rv = km.cnf()
    sha = cnf.write(os.path.join(out, "km_0.cnf"))
    rec = {"group": group, "g": g, "group_order": len(G), "km": km.summary(), "build_seconds": round(t1 - t0, 2),
           "cnf_seconds": round(time.time() - t1, 2), "km_cnf_sha256": sha, "km_vars": cnf.nv,
           "km_clauses": len(cnf.clauses), "rows_vars": len(rv),
           "peak_rss_bytes_self": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    with xopen(os.path.join(out, "km_size.json")) as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps(rec))


if __name__ == "__main__":
    main()
