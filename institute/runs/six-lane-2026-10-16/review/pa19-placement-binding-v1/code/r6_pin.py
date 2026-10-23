#!/usr/bin/env python3
"""R6 pin: freeze hashes of the sources, inputs and stored placement lists used by the R6 replay.
Read-only on the parent snapshot S and the live lane L. Writes OUT/<name> with mode x.
Usage (research venv, for the networkx pin): python -B r6_pin.py pin-v1.json
"""
import hashlib
import json
import os
import platform
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
S = "/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/pa19-parent-cover-replay-v1/inputs"
PARENT_PIN = os.path.join(os.path.dirname(S), "pin-result.json")
L = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
VENV_PY = "/Users/jinleic/.local/state/research-explorer/venv/bin/python"

SRC = ["extend_p1.py", "extend_p1q.py", "extend_b.py", "encode_skel.py", "encode_e1.py", "compare_skel.py",
       "gen_skel.py", "gen_skel_b.py", "gen_skel_cases.py", "run_hard.py", "run_hard2.py", "run_hard3.py",
       "run_hard4.py", "run_hard5.py", "run_hard6.py", "run_hard7.py", "run_hard8.py", "run_m2part.py",
       "run_m2partbatch.py", "run_m2partbatch2.py", "run_m2partbatch3.py", "run_m2partbatch4.py",
       "run_m2partbatch5.py", "summarize3.py", "summarize5.py", "summarize6.py", "bind_check.py"]
DATA = ["cases19skel/index.json", "skeletons/skeletons-ms01.json", "skeletons/skeletons-ms09.json",
        "cycle2/skel-b/skeletons-b-ms01.json", "cycle2/skel-b/skeletons-b-ms09.json",
        "cycle2/skel-b/compare-map-ms01.json", "cycle2/skel-b/compare-map-ms09.json",
        "cycle2/skel-b/compare-ms01.json", "cycle2/skel-b/compare-ms09.json",
        "cycle2/hard-tags-ms01.txt", "cycle2/tags-ms09.txt", "cycle2/hard-tags-ms06-ms09.txt",
        "cycle2/m2-jobs-part.txt", "data/profiles-19-8-6.json"]


def now():
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def fsha(path):
    if not os.path.isfile(path):
        return None
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def finfo(path):
    if not os.path.isfile(path):
        return {"exists": False}
    st = os.stat(path)
    return {"exists": True, "size": st.st_size, "mtime": time.strftime("%Y-%m-%dT%H:%M:%S%z", time.localtime(st.st_mtime)),
            "mtime_ns": st.st_mtime_ns, "sha256": fsha(path)}


def pair(rel_s, rel_l, parent_files):
    a = finfo(os.path.join(S, rel_s)) if rel_s else {"exists": False}
    b = finfo(os.path.join(L, rel_l))
    out = {"S_path": rel_s, "L_path": rel_l, "S": a, "L": b,
           "S_equals_L": a.get("sha256") is not None and a.get("sha256") == b.get("sha256")}
    if rel_s and rel_s in parent_files:
        out["S_equals_parent_pin"] = parent_files[rel_s] == a.get("sha256")
    return out


def networkx_pin():
    import networkx
    root = os.path.dirname(networkx.__file__)
    lines = []
    for dp, dn, fn in os.walk(root):
        dn.sort()
        for f in sorted(fn):
            if f.endswith(".py"):
                p = os.path.join(dp, f)
                lines.append("%s\t%s\n" % (os.path.relpath(p, root), fsha(p)))
    lines.sort()
    key = {}
    for rel in ("algorithms/graph_hashing.py", "algorithms/isomorphism/isomorph.py",
                "algorithms/isomorphism/isomorphvf2.py", "algorithms/isomorphism/vf2pp.py"):
        key[rel] = fsha(os.path.join(root, rel))
    return {"version": networkx.__version__, "root": root, "py_files": len(lines),
            "tree_digest_sha256": hashlib.sha256("".join(lines).encode()).hexdigest(), "key_files": key}


def main():
    name = sys.argv[1]
    parent = json.load(open(PARENT_PIN))
    pf = parent["files"]
    hard01 = open(os.path.join(S, "cycle2/hard-tags-ms01.txt")).read().split()
    ms09 = open(os.path.join(S, "cycle2/tags-ms09.txt")).read().split()
    jobs = open(os.path.join(S, "cycle2/m2-jobs-part.txt")).read().split()
    cmap = {mi: json.load(open(os.path.join(S, "cycle2/skel-b/compare-map-ms%02d.json" % mi))) for mi in (1, 9)}
    cases = []
    for tag in hard01 + ms09:
        mi, si = int(tag[2:4]), int(tag[6:])
        bi = cmap[mi]["a_to_b"][si]
        m1sub = "a3" if mi == 1 else "part"
        cases.append({"tag": tag, "multiset": mi, "skel_index": si, "b_index": bi,
                      "spec": pair("cases19skel/specs/%s.json" % tag, "cases19skel/specs/%s.json" % tag, pf),
                      "m1_ext": pair("cycle2/%s/%s/ext.json" % (m1sub, tag), "cycle2/%s/%s/ext.json" % (m1sub, tag), pf),
                      "m2_ext_m2part_drat": finfo(os.path.join(L, "cycle2/m2part_drat/ms%02d_b%05d/ext.json" % (mi, bi))),
                      "m2_ext_m2part_legacy": finfo(os.path.join(L, "cycle2/m2part/ms%02d_b%05d/ext.json" % (mi, bi)))})
    st = os.statvfs(L)
    res = {"recorded_at": now(), "S": S, "L": L, "parent_pin": {"path": PARENT_PIN, "sha256": fsha(PARENT_PIN),
                                                                "recorded_at_pt": parent.get("recorded_at_pt")},
           "pin_script_sha256": fsha(os.path.abspath(__file__)),
           "python": {"executable": sys.executable, "realpath": os.path.realpath(sys.executable),
                      "version": sys.version, "platform": platform.platform()},
           "venv_python": {"path": VENV_PY, "realpath": os.path.realpath(VENV_PY)},
           "networkx": networkx_pin(),
           "sources": {f: pair("src/" + f if os.path.isfile(os.path.join(S, "src", f)) else None, "src/" + f, pf)
                       for f in SRC},
           "src_delta_file": finfo(os.path.join(L, "cycle2/src-delta-vs-parent-inputs-20261017T133454.txt")),
           "data": {f: pair(f, f, pf) for f in DATA},
           "m2_jobs_equal_a_to_b_of_hard_tags": jobs == ["%d:%d" % (c["multiset"], c["b_index"]) for c in cases],
           "compare_map_flags": {mi: {k: cmap[mi][k] for k in ("count_a", "count_b", "a_each_matched_once",
                                                             "b_each_matched_once", "bijection")} for mi in (1, 9)},
           "cases": cases,
           "free_bytes": st.f_bavail * st.f_frsize}
    res["summary"] = {
        "cases": len(cases),
        "m1_ext_present_L": sum(1 for c in cases if c["m1_ext"]["L"]["exists"]),
        "m1_ext_present_S": sum(1 for c in cases if c["m1_ext"]["S"]["exists"]),
        "m1_ext_S_equals_L_where_both": all(c["m1_ext"]["S_equals_L"] for c in cases
                                            if c["m1_ext"]["S"]["exists"] and c["m1_ext"]["L"]["exists"]),
        "m2_ext_present_m2part_drat": sum(1 for c in cases if c["m2_ext_m2part_drat"]["exists"]),
        "m2_ext_present_m2part_legacy": sum(1 for c in cases if c["m2_ext_m2part_legacy"]["exists"]),
        "specs_S_equal_L": all(c["spec"]["S_equals_L"] for c in cases),
        "specs_S_equal_parent_pin": all(c["spec"].get("S_equals_parent_pin") for c in cases),
        "sources_S_equal_L": {f: v["S_equals_L"] for f, v in res["sources"].items() if v["S"]["exists"]},
        "sources_live_only": [f for f, v in res["sources"].items() if not v["S"]["exists"]],
        "data_S_equal_L": {f: v["S_equals_L"] for f, v in res["data"].items()},
    }
    with open(os.path.join(OUT, name), "x") as f:
        json.dump(res, f, indent=1)
    print(json.dumps(res["summary"], indent=1))


if __name__ == "__main__":
    main()
