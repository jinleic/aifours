#!/usr/bin/env python3
"""Turn skeletons-msXX.json files into run_cases specs (kind 'skel').
Usage: gen_skel_cases.py SKELDIR CASEDIR MS_INDEX [MS_INDEX ...]
"""
import json
import os
import sys


def main():
    skeldir, casedir = sys.argv[1], sys.argv[2]
    mis = [int(x) for x in sys.argv[3:]]
    os.makedirs(os.path.join(casedir, "specs"), exist_ok=True)
    idx_path = os.path.join(casedir, "index.json")
    index = json.load(open(idx_path)) if os.path.exists(idx_path) else {"cases": []}
    have = {c["tag"] for c in index["cases"]}
    for mi in mis:
        d = json.load(open(os.path.join(skeldir, "skeletons-ms%02d.json" % mi)))
        for si, sk in enumerate(d["skeletons"]):
            tag = "ms%02d_s%05d" % (mi, si)
            spec = {"kind": "skel", "N": d.get("N", 19), "k": d.get("k", 8), "q": d.get("q", 6),
                    "multiset_index": mi, "skel_index": si,
                    "c0": d["c0"], "special": d["special"], "L": d["L"], "skeleton": sk}
            json.dump(spec, open(os.path.join(casedir, "specs", tag + ".json"), "w"))
            if tag not in have:
                index["cases"].append({"tag": tag, "multiset": mi, "skel": si})
    index["num_cases"] = len(index["cases"])
    json.dump(index, open(idx_path, "w"), indent=1)
    print(index["num_cases"])


if __name__ == "__main__":
    main()
