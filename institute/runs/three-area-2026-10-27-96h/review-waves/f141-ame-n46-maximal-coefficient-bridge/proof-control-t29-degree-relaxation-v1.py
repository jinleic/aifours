#!/usr/bin/env python3
"""Reviewer positive control: with the per-cell degree cap relaxed (5, 6, none) do E-configurations with a
4-symbol residual alphabet appear?  Uses the same model as proof-control-t29-combinatorics-v1.py."""
import json, hashlib, subprocess, importlib.util, sys
spec = importlib.util.spec_from_file_location("m", "proof-control-t29-combinatorics-v1.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
c0 = m.clock(); runs = []
for prof in [(3,3,3,4),(4,4,4,4)]:
    for dm in (5, 6, 17):
        rr = m.solve(prof, degmax=dm, fixE=None); rr["variant"] = "degree_relaxation"; runs.append(rr)
        print({k: v for k, v in rr.items() if k != "witness_E"}, flush=True)
c1 = m.clock()
rec = {"script_sha256": hashlib.sha256(open(__file__,"rb").read()).hexdigest(), "clock_start_utc": c0, "clock_end_utc": c1, "runs": runs}
json.dump(rec, open(__file__.replace(".py","-receipt.json"),"w"), indent=1)
