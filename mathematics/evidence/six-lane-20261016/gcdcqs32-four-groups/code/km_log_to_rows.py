#!/usr/bin/env python3
"""Three-phase KM (README §4, 10:11 memory note): turn a kissat log of a KM CNF written by
code/km_size.py (row variables are 1..len(CQSKM.rows), created first) into a summary file usable
by pipeline2.py --rows-from OUT.json:0.  The KM model is rebuilt to re-check the exact cover and
the CNF sha256 recorded in km_size.json.  Usage: km_log_to_rows.py GROUP G KM_DIR OUT.json"""
import lane_guard  # noqa: F401

import collections
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lane_guard import xopen
from lanelib import parse_status, sha256_file
from cqs_km import CQSKM
import groups as grp


def main():
    group, g, kmdir, out = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
    rec = json.load(open(os.path.join(kmdir, "km_size.json")))
    assert sha256_file(os.path.join(kmdir, "km_0.cnf")) == rec["km_cnf_sha256"]
    st, model = parse_status(open(os.path.join(kmdir, "km_0.cnf.log")).read())
    assert st == "SAT", st
    spec = grp.build(group, 4, g)
    km = CQSKM(4 * g, spec["group_of"], spec["gens"])
    rows = [j for j in range(len(km.rows)) if (j + 1) in model]
    cover = collections.Counter(c for j in rows for c in km.rows[j][1])
    assert sorted(cover) == list(range(len(km.tcols))) and set(cover.values()) == {1}, "not an exact cover"
    summ = {"group": group, "g": g, "km": km.summary(), "source": kmdir,
            "samples": [{"sample": 0, "km_status": "SAT", "km_method": "kissat (three-phase)", "rows": rows}]}
    with xopen(out) as fh:
        json.dump(summ, fh)
    print(out, len(rows), "rows")


if __name__ == "__main__":
    main()
