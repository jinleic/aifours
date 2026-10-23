#!/usr/bin/env python3
"""Exploratory schema census (metadata only, stdlib, read-only on the lane). Writes census-v1.json (x mode).
Learns record schemas per route/revision; NOT an acceptance reader and not a verdict."""
import collections
import json
import os
import re
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from token_ro import ReadOnlyToken  # noqa: E402

LANE = "/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/packing-array19"
ACC = ("status", "solver_rc", "solver_stop", "checked", "drat_trim_verified", "checker_interrupted", "replay_ok",
       "reader_ok", "admission_denied", "aborted_by_sigterm", "ok", "kissat_rc", "cnf_matches_pass1",
       "cnf_matches_pass1_sha", "lrat_verified", "pass1_status", "mode", "encoder", "runner", "returncode", "solver")


def jl(p):
    with open(p, "rb") as f:
        return json.loads(f.read())


def val(v):
    if isinstance(v, (dict, list)):
        return "<%s>" % type(v).__name__
    s = json.dumps(v)
    return s if len(s) < 90 else s[:90] + "..."


class Agg:
    def __init__(self):
        self.n = 0
        self.sig = collections.Counter()
        self.vals = collections.defaultdict(collections.Counter)
        self.dt = collections.Counter()
        self.bad = []

    def add(self, rel, r):
        self.n += 1
        if not isinstance(r, dict):
            self.bad.append(rel)
            return
        rev = r.get("stream_check_revision")
        self.sig[(rev, tuple(sorted(r)))] += 1
        for k in ACC:
            if k in r:
                self.vals["%s|rev=%s" % (k, rev)][val(r[k])] += 1
        d = r.get("drat_trim")
        if isinstance(d, dict):
            self.dt["rev=%s|%s" % (rev, json.dumps({k: d[k] for k in sorted(d) if k != "wall_seconds"}))] += 1
        if "drat_trim_tail" in r:
            self.dt["tail|%s" % json.dumps(r["drat_trim_tail"][:-1])] += 1

    def out(self):
        return {"n": self.n, "unreadable": self.bad[:50], "n_unreadable": len(self.bad),
                "signatures": [{"rev": k[0], "keys": list(k[1]), "count": c} for k, c in self.sig.most_common()],
                "values": {k: dict(v.most_common(12)) for k, v in sorted(self.vals.items())},
                "drat_trim": dict(self.dt.most_common(40))}


def main():
    out_path = os.path.join(HERE, "census-v1.json")
    res = {"started": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "routes": {}, "split_names": {}, "ext_keys": {}}
    with ReadOnlyToken() as tok:
        res["token"] = {"name": tok.name, "acquired_at": tok.acquired_at, "waited_s": tok.waited_s}
        flat = {"pass1": "cases19skel/results", "proofcheck": "cases19skel/proofcheck",
                "proofstream": "cycle2/proofstream", "hard": "cycle2/hard", "hard5": "cycle2/hard5",
                "cell": "cycle2/cell-cover/ms06_s00468/r08_c06", "q0": "cases19q0/results",
                "m2q0c": "m2q0c/results"}
        for name, sub in flat.items():
            a = Agg()
            names = collections.Counter()
            for fn in sorted(os.listdir(os.path.join(LANE, sub))):
                names[re.sub(r"\d+", "#", fn)] += 1
                if fn.endswith(".json"):
                    try:
                        a.add(sub + "/" + fn, jl(os.path.join(LANE, sub, fn)))
                    except (OSError, ValueError) as e:
                        a.bad.append("%s/%s %r" % (sub, fn, e))
            res["routes"][name] = a.out()
            res["split_names"][name] = dict(names)
        for fam in ("a3", "part"):
            a = Agg()
            names = collections.Counter()
            ek = collections.Counter()
            per_dir = {}
            for d in sorted(os.listdir(os.path.join(LANE, "cycle2", fam))):
                dp = os.path.join(LANE, "cycle2", fam, d)
                if not os.path.isdir(dp):
                    names["<top>" + re.sub(r"\d+", "#", d)] += 1
                    continue
                pd = collections.Counter()
                for fn in sorted(os.listdir(dp)):
                    pat = re.sub(r"\d+", "#", fn)
                    names[pat] += 1
                    pd[pat] += 1
                    if not fn.endswith(".json"):
                        continue
                    p = os.path.join(dp, fn)
                    try:
                        r = jl(p)
                    except (OSError, ValueError) as e:
                        a.bad.append("%s/%s/%s %r" % (fam, d, fn, e))
                        continue
                    if fn == "ext.json":
                        ek[json.dumps({k: (type(v).__name__ if isinstance(v, list) else v) for k, v in r.items()
                                       if k != "source"} | {"source_is_tag": r.get("source") == d + ".json"})[:300]] += 1
                    elif re.fullmatch(r"(f\d+|batch_\d+_\d+)(_\w+)?\.json", fn):
                        a.add("%s/%s/%s" % (fam, d, fn), r)
                    else:
                        names["<other>%s" % pat] += 1
                per_dir[d] = dict(pd)
            res["routes"][fam] = a.out()
            res["split_names"][fam] = dict(names)
            res["ext_keys"][fam] = dict(ek.most_common(60))
            res["split_names"][fam + "_per_dir"] = per_dir
    res["ended"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    with open(out_path, "x") as f:
        json.dump(res, f, indent=1, default=str)
        f.write("\n")
    import resource
    print(json.dumps({"ok": True, "out": out_path, "maxrss_bytes": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                      "token": res["token"], "started": res["started"], "ended": res["ended"]}))


if __name__ == "__main__":
    main()
